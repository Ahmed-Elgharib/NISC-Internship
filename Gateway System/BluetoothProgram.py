from bluepy.btle import Peripheral
from bluepy.btle import Scanner
from datetime import datetime
from threading import Thread
from subprocess import Popen
from time import sleep
from json import loads
import requests

scanner = None
post_id = {}

def RefreshBluetooth():
    Popen(["hciconfig","hci0","down"])
    Popen(["hciconfig","hci0","up"])
    Popen(["service","bluetooth","restart"])

def BTScanner():
    global scanner,scanning
    while(True):
        try:
            scanner = Scanner()
            scanner.scan(0,True)
        except:
            print("Error: Failed to initiate bluetooth scanner, retrying again...")
            RefreshBluetooth()

def JSONRequest(mac,info={}):
    global post_id
    url = "http://computer:3000/readings/"
    try:
        if mac not in post_id:
            req = requests.post(url,json={"mac":mac})
            if not req.ok: return
            post_id[mac] = loads(req.text)['id']
        else:
            req = requests.patch("".join((url,str(post_id[mac]))),data=info)
            if not req.ok:
                req = requests.post(url,json={"mac":mac})
                if not req.ok: return
                post_id[mac] = loads(req.text)['id']
    except: return
def EstablishedBTDevice(btd,mac):
    Thread(target=JSONRequest,args=(mac,)).start()
    val = b'\x01'
    info = {}
    while(btd.getState() == "conn"):
        btd.writeCharacteristic(0x0020,val)
        btd.writeCharacteristic(0x0022,val)
        info['led0'] = btd.readCharacteristic(0x0020)
        info['led1'] = btd.readCharacteristic(0x0022)
        info['last-update'] = datetime.now()
        Thread(target=JSONRequest,args=(mac,info)).start()
        if val == b'\x01': val = b'\x00'
        else: val = b'\x01'
        sleep(0.5)
                
def MainProgram():
    global scanner,scanning
    Thread(target=BTScanner).start()
    while(scanner is None): pass
    mac_list = ["b0:91:22:69:ff:fe","54:6c:0e:9b:69:be"]
    while(True):
        if len(scanner.scanned) < 1: continue
        avail_mac = mac_list & scanner.scanned.keys()
        if len(avail_mac) < 1: continue
        for mac in avail_mac:
            print(f"Available MAC: {mac} ({scanner.scanned[mac].addrType}) with RSSI: {scanner.scanned[mac].rssi} dB")
            Thread(target=EstablishedBTDevice,args=(Peripheral(mac,"public"),mac)).start()
            del scanner.scanned[mac]
                
Thread(target=MainProgram).start()
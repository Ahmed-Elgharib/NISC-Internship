from bluetooth.ble import GATTRequester
from bluepy.btle import Peripheral
from bluepy.btle import Scanner
from datetime import datetime
from threading import Thread
from subprocess import run
from time import sleep
from json import loads
import requests

scanner = Scanner()
refreshing = False

def RefreshBluetooth():
    global refreshing
    refreshing = True
    run("hciconfig hci0 down")
    run("hciconfig hci0 up")
    run("service bluetooth restart")
    refreshing = False

refbt = Thread(target=RefreshBluetooth)

def MainProgram():
    global refreshing
    global scanner
                
    scnbtd.start()

    mac_list = ["b0:91:22:69:ff:fe","54:6c:0e:9b:69:be"]

    while(True):
        if len(scanner.scanned) < 1: continue
        nextscan = next(iter(scanner.scanned))
        device = scanner.scanned[nextscan]
        print(f"MAC: {device.addr} ({device.addrType}) with RSSI {device.rssi} dB")
        del scanner.scanned[nextscan]
        if (nextscan not in mac_list): continue
        #device = scanner.scanned.pop(nextscan)
        try:
            req = GATTRequester(nextscan,False)
            req.connect(True)
            Thread(target=EstablishedBTDevice,args=(req,nextscan)).start()
        except: pass
        
main = Thread(target=MainProgram)

def ScanBTDevices():
    global refreshing
    global scanner
    while(True):
        try:
            scanner.start(passive=True)
            scanner.process(0)
        except:
            try:
                scanner.stop()
                scanner.clear()
            except:
                while(True):
                    try:
                        scanner = Scanner()
                        break
                    except:
                        if Refreshing == False:
                            refbt.start()
        
scnbtd = Thread(target=ScanBTDevices)

def EstablishedBTDevice(req,mac):
    try:
        url = "http://computer:3000/readings/"
        _id = loads(requests.post(url,json={"mac":mac}).text)['id']
        url = "".join((url,str(_id)))
        val = b'\x01'
        info = {}
        while(req.is_connected()):
            req.write_by_handle(0x0020,val)
            req.write_by_handle(0x0022,val)
            info['led0'] = req.read_by_handle(0x0020)
            info['led1'] = req.read_by_handle(0x0022)
            info['last-update'] = datetime.now()
            requests.patch(url,data=info)
            sleep(0.5)
            if(val==b'\x01'):
                val = b'\x00'
            else:
                val = b'\x01'
    except: return
                
main.start()

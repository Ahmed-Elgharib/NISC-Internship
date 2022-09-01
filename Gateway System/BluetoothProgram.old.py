from bluetooth.ble import GATTRequester
from bluetooth.ble import DiscoveryService
from threading import Thread
from subprocess import run
from time import time,sleep
from json import loads
import requests

Refreshing = False
srvc = DiscoveryService()
dvcs = None

print(srvc)

def RefreshBluetooth():
    global Refreshing
    Refreshing = True
    run(["hciconfig","hci0","down"])
    run(["hciconfig","hci0","up"])
    run(["service","bluetooth","restart"])

refbt = Thread(target=RefreshBluetooth)

def MainProgram():
    global srvc,dvcs
    
    while(True):
        try:
            dvcs = srvc.discover(2)
            Refreshing = False
            break
        except:
            if Refreshing == False:
                refbt.start()
                
                    
    disbtd.start()

    mac_list = ["B0:91:22:69:FF:FE","54:6C:0E:9B:69:BE"]

    while(dvcs is not None):
        for mac,name in dvcs.items():
            print("Found available device -> MAC Address:",mac)
            if (mac not in mac_list): continue
            try:
                req = GATTRequester(mac,False)
                req.connect(True)
                Thread(target=EstablishedBTDevice,args=(req,)).start()
            except: pass
        print("----------End of Line----------")
            
main = Thread(target=MainProgram)

def DiscoverBTDevices():
    global srvc,dvcs
    print("Started Discovery Service Thread")
    while(True):
        for mac,name in dvcs.items():
            print("Found available device -> MAC Address:",mac)
        try:
            dvcs = srvc.discover(2)
            Refreshing = False
        except:
            if Refreshing == False:
                refbt.start()
        print("----------End of Line----------")
        
disbtd = Thread(target=DiscoverBTDevices)

def EstablishedBTDevice(req):
    try:
        url = "http://computer:3000/readings/"
        _id = loads(requests.post(url,json={"last-update":time()}).text)['id']
        url = "".join((url,str(_id)))
        val = b'\x01'
        while(req.is_connected()):
            req.write_by_handle(0x0020,val)
            req.write_by_handle(0x0022,val)
            led0 = req.read_by_handle(0x0020)
            led1 = req.read_by_handle(0x0022)
            requests.patch(url,data={"led0":led0,"led1":led1,"last-update":time()})
            sleep(0.5)
            if(val==b'\x01'):
                val = b'\x00'
            else:
                val = b'\x01'
    except: return
                
main.start()

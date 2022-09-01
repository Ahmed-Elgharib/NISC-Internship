from bluepy.btle import Scanner#, DefaultDelegate
from threading import Thread
from sys import stdout

'''class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("New device is discovered with address:",dev.addr)
        elif isNewData:
            print("New data is received from device with address:",dev.addr)'''

scanner = Scanner()#.withDelegate(ScanDelegate())

def ViewDevices():
    global scanner
    
    mac_list = ["b0:91:22:69:ff:fe","54:6c:0e:9b:69:be"]
    
    while(True):
        if len(scanner.scanned) < 1: continue
        for device in list(scanner.getDevices()):
            print(f"MAC: {device.addr} ({device.addrType}) with RSSI {device.rssi} dB")
        print("\n")
        
vwdvcs = Thread(target=ViewDevices)
vwdvcs.start()
        
scanner.start(passive=True)
scanner.process(0)
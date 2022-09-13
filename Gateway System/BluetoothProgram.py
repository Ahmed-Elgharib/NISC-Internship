from bluepy.btle import Peripheral
from bluepy.btle import Scanner
from pymongo import MongoClient
from datetime import datetime
from threading import Thread
from subprocess import Popen
from time import sleep
from json import loads
import requests

scanner = None
dev_data = {}


def RefreshBluetooth():
    Popen(["hciconfig", "hci0", "down"])
    Popen(["hciconfig", "hci0", "up"])
    Popen(["service", "bluetooth", "restart"])


def BTScanner():
    global scanner
    while (True):
        try:
            scanner = Scanner()
            scanner.scan(0, True)
        except:
            print("Error: Failed to initiate bluetooth scanner, retrying again...")
            RefreshBluetooth()


def MongoDBClient():
    global dev_data
    while (True):
        try:
            clnt = MongoClient("mongodb://computer/")
            db = clnt["mydb"]
            col = db["readings"]
            print("Connected to Mongo DataBase!")
            while (True):
                for mac in dev_data:
                    if not list(col.find({"mac": mac})):
                        col.insert_one({"mac": mac})
                    for var in dev_data[mac]:
                        col.update_one(
                            {"mac": mac}, {"$set": {var: dev_data[mac][var]}})
                        del dev_data[mac][var]
                    col.update_one(
                        {"mac": mac}, {"$set": {"last-updated": datetime.now()}})
        except:
            print("Error connecting to Mongo DataBase, retrying...")


def JSONDBClient():
    global dev_data
    url = "http://computer:3000/readings"
    while (True):
        sleep(1)
        while (not dev_data):
            pass
        while (True):
            try:
                req = requests.get(url)
                if req.ok:
                    break
            except:
                pass
        for info in loads(req.text):
            requests.delete("".join((url, "/", str(info['id']))))
        for mac in dev_data:
            req = requests.post(url, data=dev_data[mac])
            dur = req.elapsed.total_seconds()*1000
            print("Time taken for uploading data into database:", dur, "ms")


def EstablishedBTDevice(btd, mac):
    global dev_data
    val = b'\x01'
    print("Bluetooth connection established with device MAC Address:", mac)
    while (btd.getState() == "conn"):
        btd.writeCharacteristic(0x0020, val)
        btd.writeCharacteristic(0x0022, val)
        if mac not in dev_data:
            dev_data[mac] = {}
        dev_data[mac]['led0'] = btd.readCharacteristic(0x0020)
        dev_data[mac]['led1'] = btd.readCharacteristic(0x0022)
        if val == b'\x01':
            val = b'\x00'
        else:
            val = b'\x01'
        sleep(0.5)


Thread(target=BTScanner).start()
Thread(target=MongoDBClient).start()
Thread(target=JSONDBClient).start()
while (scanner is None):
    pass
mac_list = ["b0:91:22:69:ff:fe", "54:6c:0e:9b:69:be"]
while (True):
    avail_mac = mac_list & scanner.scanned.keys()
    for mac in avail_mac:
        if mac not in dev_data:
            dev_data[mac] = {}
        dev_data[mac]['addrType'] = scanner.scanned[mac].addrType
        dev_data[mac]['rssi'] = scanner.scanned[mac].rssi
        print("Found device with MAC Address:", mac,
              "and RSSI:", scanner.scanned[mac].rssi, "dBs")
        # The scanner keeps reading the device information until the connection is established (As tested)
        try:
            Thread(target=EstablishedBTDevice, args=(
                Peripheral(mac), mac)).start()
        except:
            del scanner.scanned[mac]

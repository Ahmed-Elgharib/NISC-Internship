from bluepy.btle import Peripheral
from bluepy.btle import Scanner
from pymongo import MongoClient
from datetime import datetime
from threading import Thread
from subprocess import Popen
from time import sleep
from json import loads
import requests

# Global variables
scanner = None
dev_data = {}


def RefreshBluetooth(): # Warning: This function is risky as the program may stop, better refresh manually
    Popen(["hciconfig", "hci0", "down"])  # Shut down the bluetooth driver
    Popen(["hciconfig", "hci0", "up"])  # Start up the bluetooth driver
    Popen(["service", "bluetooth", "restart"])  # Restart bluetooth service


def BTScanner():
    global scanner
    # RefreshBluetooth() # Refresh the bluetooth initially (Disabled here)
    while (True):
        try:
            scanner = Scanner()  # Initialize the scanner
            scanner.scan(0, True) # Start scanning for infinity with passive set to True
        except:
            print("Error: Failed to initiate bluetooth scanner, retrying again...")
            RefreshBluetooth()  # Try refreshing the bluetooth itself in case errors or failures


def MongoDBClient():  # For the Mongo Database Storage Document
    global dev_data
    while (True):
        try:
            clnt = MongoClient("mongodb://computer/") # Connect to the Mongo Database link
            print("Connected to Mongo database!")
        except:
            print("Error connecting to Mongo database, retrying...")
            continue
        try:
            col = clnt["mydb"]["readings"] # Select from database "mydb" collection named "readings"
            while (True):
                for mac in dev_data:
                    if not list(col.find({"mac": mac})):
                        col.insert_one(dev_data[mac]) # Insert data initially when does not exist
                    for var in dev_data[mac]:
                        col.update_one({"mac": mac}, {"$set": {var: dev_data[mac][var]}}) # Update every variable inside data document
                    col.update_one({"mac": mac}, {"$set": {"last-updated": datetime.now().ctime()}}) # Give out the last date and time the data document was updated
        except: print("Error updating data to Mongo database, reconnecting...")


def JSONDBClient():  # For the JSON Database Web Document
    global dev_data
    url = "http://computer:3000/readings"  # Link for JSON Server Database
    while (True):
        sleep(1)  # Iterate the loop every 1 second
        while (not dev_data): pass  # Pause as long as there is no data entered yet from devices
        while (True):
            try:
                req = requests.get(url)  # Check if is able to get data by request
                if req.ok: break  # Break the loop once successful
            except: pass
        for info in loads(req.text):
            requests.delete("".join((url, "/", str(info['id'])))) # Delete all the old data document
        for mac in dev_data:
            req = requests.post(url, data=dev_data[mac]) # Enter the new data into web document
            dur = req.elapsed.total_seconds()*1000 # Get the total time it took from start of post till response
            dev_data[mac]["RTT"] = dur # Set the round trip time taken for the specific data post request
            print("Time taken for uploading data into JSON database:", dur, "ms")


def EstablishedBTDevice(btd, mac, addrType, rssi):
    global dev_data  # Initialization
    # Below is to create a new dictionary list for the new MAC address device with scanner information
    dev_data[mac] = {"node-id": "-", "protocol": "ble", "addrType": addrType,
                     "rssi": rssi, "mac": mac, "sensor-id": "-", "value": "-",
                     "magnitude": "-", "gate-id": "-", "network-id": "-"}
    print("Bluetooth connection established with device MAC Address:", mac)
    try:
        while (btd.getState() == "conn"):  # Do while loop until connection is lost
            reading = btd.readCharacteristic(0x002c) # Read the data value from given characteristic handle
            # reading_hex = b2a_hex(reading).decode() # Filter the reading to give out hex numbers only
            # reading_int = int(reading_hex,16) # Convert hex into integer
            reading_int = int.from_bytes(bytearray(reading), byteorder="little") # Enhanced version of converting hex into integer
            num_bytes = (reading_int.bit_length()+7)//8 # Get total number of bytes
            reading_str = reading_int.to_bytes(num_bytes, "little").decode()  # Get it in string format
            dev_data[mac]['sensor-id'] = "Temperature" # Set sensor id name to "Temperature"
            dev_data[mac]['value'] = reading_str # We need to read it as a string here
            dev_data[mac]['magnitude'] = "Celcius" # Set magnitude named "Celcius"
        del dev_data[mac]  # Delete when loop ends
    except: del dev_data[mac]  # Delete when error happens

Thread(target=BTScanner).start()
Thread(target=MongoDBClient).start()
Thread(target=JSONDBClient).start()
while (scanner is None): pass
mac_list = ["b0:91:22:69:ff:fe", "54:6c:0e:9b:69:be"]
while (True):
    avail_mac = mac_list & scanner.scanned.keys()  # Get the matched MAC addresses
    for mac in avail_mac:  # Go iterate through all the founded MAC addresses
        # These data will be displayed and kept changing until the connection is established
        addrType = scanner.scanned[mac].addrType # Store address type in temporary variable
        rssi = scanner.scanned[mac].rssi # Store RSSI in temporary variable as well
        print("Found device with MAC Address:", mac,"Type:", addrType, "and RSSI:", rssi, "dBs")
        try: Thread(target=EstablishedBTDevice, args=(Peripheral(mac), mac, addrType, rssi)).start()  # Start the connection thread
        except: del scanner.scanned[mac] # Remove the MAC address from scanner until shown again

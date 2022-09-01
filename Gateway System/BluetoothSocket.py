import bluetooth.ble

sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

try: #using MAC Address 54:6C:0E:9B:69:BE as an example
    sock.connect(("54:6C:0E:9B:69:BE", 0x1001))
    print("Connected to the device successfully")
except:
    print("Error connecting to device")
    
while True:
    sleep(0.5)
    try:
        sock.send(b"ping")
    except:
        break

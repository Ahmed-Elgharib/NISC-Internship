from bluetooth.ble import DiscoveryService
from subprocess import run
#import bluetooth.ble

'''fnd_dev = bluetooth.discover_devices(duration=8, lookup_names=True)

if len(fnd_dev) > 0:
    print("Bluetooth devices found:")
for i in range(len(fnd_dev)):
    print(f"{i+1}. MAC: {fnd_dev[i][0]} | Name: {fnd_dev[i][1]}")'''

#srvc = bluetooth.find_service(address=None)

run(["sudo","hciconfig","hci0","down"])
run(["sudo","hciconfig","hci0","up"])
run(["sudo","service","bluetooth","restart"])


srvc, dvcs = DiscoveryService(), None
    
count = 1
while(True):
    try:
        print("Still trying trial num",count)
        count += 1
        dvcs = srvc.discover(90)
        break
    except: continue

i = 1
if len(dvcs.items()) > 0:
    print("List of devices:")
for mac,name in dvcs.items():
    print(f"{i}. Name: {name} | MAC: {mac}")
    i += 1
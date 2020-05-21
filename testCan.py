import sys

if (sys.version_info.major < 3) or ((sys.version_info.major <= 3) and (sys.version_info.minor < 7)): 
   print ( "You must run this program with python 3.7 or greater" ) 
assert sys.version_info >= (3,7) 
print (str(sys.version_info))
import can 

bus = can.interface.Bus(channel='can0', bustype='socketcan_native') 
msg = can.Message(arbitration_id=0x7de,data=[0, 25, 0, 1, 3, 1, 4, 1])  
bus.send(msg)
notifier = can.Notifier(bus, [can.Printer()])
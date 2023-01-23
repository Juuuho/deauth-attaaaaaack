import argparse
from scapy.all import *
import sys
import random
import threading

def Ap_Broadcast():
    return 0

def Ap_Unicast():
    return 0

def Auth_Attack():
    return 0

if __name__ == '__main__':

    argument = sys.argv
    del argument[0]
    print(f'Argument : {argument}')

    if len(argument) < 2:
        print("syntax : deauth-attack <interface> <ap mac> [<station mac> [-auth]]\nsample : deauth-attack mon0 00:11:22:33:44:55 66:77:88:99:AA:BB")
        quit()
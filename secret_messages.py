"""
Author: Bar Assulin
Date: 25/1/24
"""

from scapy.all import *
import logging


#contant
MY_IP = "10.0.0.23"


def main():
    message = str(input("Enter your message: "))
    for mes in message:
        port = ord(mes)
        send((IP(dst=MY_IP) / UDP(dport=port)))


if __name__ == "__main__":
    #logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)


    main()

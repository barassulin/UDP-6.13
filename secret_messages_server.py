"""
Author: Bar Assulin
Date: 25/1/24
"""

import sys
from scapy.all import *
import logging


def empty_udp_filter(packet):
    if packet.haslayer(UDP) and not packet[UDP].payload:
        return True
    else:
        return False


def main():
    string = ""
    while True:
        capture = sniff(filter="udp", count=1, lfilter=empty_udp_filter)
        char = chr(capture[0][UDP].dport)
        logging.debug("captured: "+char)
        string = string + char
        print(string)


if __name__ == "__main__":
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

    main()

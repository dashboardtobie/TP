from scapy.all import *

gateway_ip = "10.2.1.254"  #IP de la passerelle
attacker_mac = "00:0c:29:d8:10:be" # MAC de l'attaquant

ip_packet = IP(dst=gateway_ip, src="10.2.1.104") # Pacquet IP

arp_request = ARP(pdst=gateway_ip) # Requete ARP pour decouvrir la MAC de la passerelle
answered, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / arp_request, timeout=5) 

if answered:
    gateway_mac = answered[0][1].hwsrc
    print("[+] Adresse MAC trouvee. Envoi du ping vers la passerelle...")
    ethernet_frame = Ether(dst=gateway_mac, src=attacker_mac)
    icmp_request = ICMP(type=8) 
    packet = ethernet_frame / ip_packet / icmp_request
    answered, unanswered = srp(packet, timeout=5)
    if answered:
        print("[+] Réponse reçue :")
        for send, receive in answered:
            receive.show()
    else:
        print("[-] Aucun pong reçu. Vérifiez votre réseau et votre configuration.")
else :
    print("[-] Echec de l decouverte de l'adresse MAC")

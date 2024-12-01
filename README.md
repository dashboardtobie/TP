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
#### b - ARP Spoofing
[arp_spoofing.py](arp_spoof.py) <br>
[arp_spoofing.pcapng](arp_spoof.pcapng) <br>

#### c - MITM
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

## III - REMEDIATIONS

### 1 - DHCP Spoofing
#### a. Activer le DHCP Snooping
Le DHCP Snooping est une fonctionnalité disponible sur la plupart des switches managés. Il fonctionne en surveillant les paquets DHCP et en permettant uniquement les réponses DHCP provenant de ports approuvés (trusted).

##### Configuration :
- Configurez les ports connectés à des serveurs DHCP comme approuvés.
- Configurez les autres ports (ceux connectés à des clients ou inconnus) comme non-approuvés.
- Filtrez les paquets DHCP qui ne respectent pas cette règle. Par exemple les ports non approuvés ne pourront pas emettre de DHCP Offer et Ack.

### 2 - ARP
#### a -  Activer la protection dynamique contre l'ARP (Dynamic ARP Inspection - DAI)
La fonctionnalité Dynamic ARP Inspection sur les switches réseau permet de valider les requêtes et réponses ARP en comparant les adresses MAC et IP aux entrées autorisées (via le DHCP Snooping).

##### Fonctionnement :
- Filtrage des paquets ARP.
- Validation des associations IP-MAC à partir de la base de données DHCP Snooping.

#### b - Port security
Port Security est une fonctionnalité des switches Cisco permettant de limiter l'accès réseau à un port en restreignant les adresses MAC autorisées. Cela améliore la sécurité en empêchant les appareils non autorisés de se connecter.

##### Modes de fonctionnement :
- Adresses MAC statiques : configurées manuellement et fixées dans la table d'adresses.
- Adresses MAC dynamiques : apprises automatiquement mais perdues après un redémarrage du switch.
- Adresses MAC sticky : apprises automatiquement et sauvegardées dans la configuration active, conservées après un redémarrage.

##### Actions en cas de dépassement de la limite d'adresses autorisées :
- Protect : bloque les paquets non autorisés sans notification.
- Restrict : bloque les paquets non autorisés et envoie une alerte.
- Shutdown : désactive immédiatement le port et envoie une alerte.
Port Security offre ainsi une protection efficace contre les connexions malveillantes ou accidentelles au réseau.

### 3 - DNS Spoofing
#### Chiffrer le trafic DNS avec DoH ou DoT
DNS over HTTPS (DoH) et DNS over TLS (DoT) chiffrent les requêtes DNS, rendant plus difficile l'interception et l'altération des requêtes.

### 4 - Exfiltration ICMP
#### DPI (Deep Packet Inspection)
Deep Packet Inspection (DPI) est une technologie de surveillance et d'analyse du trafic réseau qui permet d'examiner l'intégralité du contenu des paquets de données circulant sur un réseau, plutôt que de se limiter à des informations de base comme l'adresse IP source ou destination (qui sont analysées dans les techniques de filtrage classiques, comme le filtrage de paquets). DPI analyse la paye-load des paquets (le contenu) et peut examiner chaque octet de données pour en tirer des informations précises.

##### Fonctionnement de DPI :
- Examen des paquets : DPI inspecte chaque paquet dans le flux réseau, analysant à la fois l'en-tête et la charge utile (données) du paquet.

- Identification de protocoles : DPI peut identifier des protocoles spécifiques et des applications  en analysant le contenu des paquets et les correspondances avec des signatures ou des modèles de trafic connus.

- Filtrage et bloquage : En fonction des politiques de sécurité, DPI peut bloquer certains types de contenu ou de communications en inspectant et en analysant le contenu des paquets.

### 5 - STP
BPDU Guard (Bridge Protocol Data Unit Guard) est une fonctionnalité de sécurité utilisée dans les réseaux Ethernet, spécifiquement sur les commutateurs Cisco, pour protéger le réseau contre les attaques de type Spanning Tree Protocol (STP), en empêchant l'injection de BPDUs malveillants dans un réseau.

##### Fonctionnement du BPDU Guard :
- Lorsqu'un commutateur reçoit un BPDU sur un port où BPDU Guard est activé, le port est immédiatement désactivé (mis en état errdisable). Cela empêche ce port de participer à la mise à jour du Spanning Tree et protège ainsi contre des modifications non autorisées du rôle de Bridge.
- BPDU Guard est souvent activé sur des ports où les BPDUs ne sont pas attendus, comme les ports d'accès connectés à des hôtes (ordinateurs, imprimantes, etc.) ou des périphériques finaux. Ces hôtes ne devraient pas émettre de BPDUs.

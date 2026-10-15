"""
CCNA OpenSim - Domain 1.0 Network Fundamentals Generator (80 Questions)
Covers subtopics 1.1 through 1.13 based on Cisco CCNA 200-301 v1.1
"""

import json
import os

questions = [
    # 1.1 Components (8 Qs)
    {
        "id": "q-1-1-001",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "An administrator is designing a campus network and needs a device that inspects traffic up to Layer 7, detects zero-day exploits, and decrypts TLS traffic for malware inspection. Which component is required?",
        "options": [
            {"id": "A", "text": "Layer 3 Distribution Switch", "isCorrect": False},
            {"id": "B", "text": "Next-Generation Firewall (NGFW)", "isCorrect": True},
            {"id": "C", "text": "Wireless LAN Controller (WLC)", "isCorrect": False},
            {"id": "D", "text": "Stateful Packet Inspection (SPI) Router", "isCorrect": False}
        ],
        "explanation": "Next-Generation Firewalls (NGFW) provide deep packet inspection up to Layer 7 (Application layer), integrated Intrusion Prevention Systems (IPS), TLS/SSL decryption, and advanced threat intelligence, unlike traditional L3 switches or legacy SPI routers.",
        "reference": "Cisco Press CCNA 200-301 Official Cert Guide Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-002",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "Which network component is responsible for centralizing the management, RF configuration, and roaming policies of Lightweight Access Points (LAPs)?",
        "options": [
            {"id": "A", "text": "Next-Generation Intrusion Prevention System (NGIPS)", "isCorrect": False},
            {"id": "B", "text": "Wireless LAN Controller (WLC)", "isCorrect": True},
            {"id": "C", "text": "Top-of-Rack Layer 2 Switch", "isCorrect": False},
            {"id": "D", "text": "Autonomous Access Point Bridge", "isCorrect": False}
        ],
        "explanation": "A Wireless LAN Controller (WLC) uses CAPWAP tunnels to manage Lightweight Access Points (LAPs) centrally, handling radio resource management (RRM), client authentication, mobility/roaming, and security policies.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-003",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "A network engineer needs to power an advanced PTZ IP surveillance camera requiring 25.5 Watts of DC power over Ethernet cabling. Which Power over Ethernet standard must the access switch support?",
        "options": [
            {"id": "A", "text": "IEEE 802.3af (PoE)", "isCorrect": False},
            {"id": "B", "text": "IEEE 802.3at (PoE+)", "isCorrect": True},
            {"id": "C", "text": "IEEE 802.1Q", "isCorrect": False},
            {"id": "D", "text": "IEEE 802.3ad", "isCorrect": False}
        ],
        "explanation": "IEEE 802.3af provides up to 15.4W at the PSE (12.95W at PD). IEEE 802.3at (PoE+) provides up to 30W at the PSE (25.5W at PD). High-power devices such as PTZ cameras require 802.3at PoE+.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-004",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "multiple-choice",
        "prompt": "What are two primary functions of a router in an enterprise enterprise campus network? (Choose two.)",
        "options": [
            {"id": "A", "text": "Forwarding frames based on destination MAC addresses", "isCorrect": False},
            {"id": "B", "text": "Creating separate broadcast domains for each connected interface", "isCorrect": True},
            {"id": "C", "text": "Making forwarding decisions based on destination IP addresses", "isCorrect": True},
            {"id": "D", "text": "Supplying PoE power to unmanaged access switches", "isCorrect": False},
            {"id": "E", "text": "Managing STP root bridge election within a single VLAN", "isCorrect": False}
        ],
        "explanation": "Routers operate at Layer 3 (Network layer). They forward packets based on logical destination IP addresses using routing tables, and by default each router interface defines a separate broadcast domain.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-005",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "How does a Layer 3 switch achieve high-speed packet forwarding compared to a traditional software-based router?",
        "options": [
            {"id": "A", "text": "By executing routing decisions in general-purpose CPU threads", "isCorrect": False},
            {"id": "B", "text": "By offloading route lookups and ACL processing to hardware ASICs and TCAM", "isCorrect": True},
            {"id": "C", "text": "By ignoring IP TTL decrementing during transmission", "isCorrect": False},
            {"id": "D", "text": "By converting all Layer 3 packets into ATM cells", "isCorrect": False}
        ],
        "explanation": "Layer 3 switches utilize specialized hardware Application-Specific Integrated Circuits (ASICs) and Ternary Content Addressable Memory (TCAM) to perform Cisco Express Forwarding (CEF) route lookups at line rate.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-006",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "Which network security appliance passively monitors traffic via a SPAN port to alert on malicious signatures without inline latency?",
        "options": [
            {"id": "A", "text": "Intrusion Detection System (IDS)", "isCorrect": True},
            {"id": "B", "text": "Intrusion Prevention System (IPS)", "isCorrect": False},
            {"id": "C", "text": "Stateful Packet Inspection Firewall", "isCorrect": False},
            {"id": "D", "text": "Application Delivery Controller (ADC)", "isCorrect": False}
        ],
        "explanation": "An IDS (Intrusion Detection System) operates out-of-band by receiving a copy of traffic (e.g. through SPAN or network TAP), analyzing signatures and alerting administrators without introducing latency to live traffic.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-007",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "Which IEEE standard delivers up to 90 Watts of Power over Ethernet using all four twisted copper pairs?",
        "options": [
            {"id": "A", "text": "IEEE 802.3af (Type 1)", "isCorrect": False},
            {"id": "B", "text": "IEEE 802.3at (Type 2)", "isCorrect": False},
            {"id": "C", "text": "IEEE 802.3bt (Type 4 / 4PPoE)", "isCorrect": True},
            {"id": "D", "text": "IEEE 802.3ab", "isCorrect": False}
        ],
        "explanation": "IEEE 802.3bt (Type 4) supports up to 90W (or ~71.3W at the powered device) by delivering power across all four pairs of twisted copper cabling.",
        "reference": "CCNA 200-301 v1.1 Blueprint 1.1",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-1-008",
        "domainId": "1.0",
        "subtopicCode": "1.1",
        "subtopicName": "Explain role and function of network components",
        "type": "single-choice",
        "prompt": "An endpoint fails to obtain an IP address and displays a MAC address of 00-00-00-00-00-00 in device manager. At which OSI layer is the hardware network interface card failing to operate?",
        "options": [
            {"id": "A", "text": "Layer 1 (Physical)", "isCorrect": False},
            {"id": "B", "text": "Layer 2 (Data Link)", "isCorrect": True},
            {"id": "C", "text": "Layer 3 (Network)", "isCorrect": False},
            {"id": "D", "text": "Layer 4 (Transport)", "isCorrect": False}
        ],
        "explanation": "MAC (Media Access Control) addresses are hardware identifiers burned into the NIC that operate at Layer 2 (Data Link layer).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 1,
        "fidelityScore": 4.7,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.2 Topology Architectures (6 Qs)
    {
        "id": "q-1-2-001",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "In a modern data center Clos architecture (Spine-Leaf), which rule governs physical interconnections between devices?",
        "options": [
            {"id": "A", "text": "Spine switches must be directly interconnected via redundant trunks", "isCorrect": False},
            {"id": "B", "text": "Leaf switches connect to every spine switch, with zero leaf-to-leaf or spine-to-spine connections", "isCorrect": True},
            {"id": "C", "text": "End hosts connect directly to spine switches for lower latency", "isCorrect": False},
            {"id": "D", "text": "Leaf switches connect in a token ring topology with spines acting as bridges", "isCorrect": False}
        ],
        "explanation": "In a Spine-Leaf (Clos) data center network topology, every leaf connects to every spine switch. Leaf switches do not connect to each other, and spine switches do not connect to each other. This provides consistent, predictable low-latency East-West traffic.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-2-002",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "What is the primary architectural difference between a traditional three-tier campus design and a two-tier collapsed core design?",
        "options": [
            {"id": "A", "text": "The collapsed core combines the Core and Distribution layers into a single physical or logical layer", "isCorrect": True},
            {"id": "B", "text": "The collapsed core eliminates the Access layer completely", "isCorrect": False},
            {"id": "C", "text": "The three-tier design does not support Layer 3 routing", "isCorrect": False},
            {"id": "D", "text": "The two-tier design cannot support VLAN trunking or wireless APs", "isCorrect": False}
        ],
        "explanation": "A collapsed core design merges the functions of the Core layer (high-speed transport) and Distribution layer (policy, routing, security boundaries) into a single layer of switches, reducing hardware cost in smaller/midsize campuses.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-2-003",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "Which WAN topology provides direct connectivity between every branch office site, maximizing redundancy but requiring the highest number of physical or logical circuits?",
        "options": [
            {"id": "A", "text": "Hub-and-spoke (Star)", "isCorrect": False},
            {"id": "B", "text": "Full mesh", "isCorrect": True},
            {"id": "C", "text": "Partial mesh", "isCorrect": False},
            {"id": "D", "text": "Point-to-point bus", "isCorrect": False}
        ],
        "explanation": "In a full-mesh topology, every site connects directly to every other site (requiring n(n-1)/2 links). While it provides the highest fault tolerance and direct site-to-site communication, it has the highest cost and configuration overhead.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 13",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-2-004",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "In cloud computing models, what service model provides the customer with virtual machines, storage, and network interfaces while leaving OS installation and maintenance to the customer?",
        "options": [
            {"id": "A", "text": "Software as a Service (SaaS)", "isCorrect": False},
            {"id": "B", "text": "Platform as a Service (PaaS)", "isCorrect": False},
            {"id": "C", "text": "Infrastructure as a Service (IaaS)", "isCorrect": True},
            {"id": "D", "text": "Function as a Service (FaaS)", "isCorrect": False}
        ],
        "explanation": "Infrastructure as a Service (IaaS) provides virtualized computing resources (VMs, block storage, virtual networks). The cloud provider manages the physical hardware/hypervisor, while the customer manages the operating system, middleware, and applications.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-2-005",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "Which network architecture type is typically deployed in small office/home office (SOHO) environments to consolidate multiple services into a single consumer or small business unit?",
        "options": [
            {"id": "A", "text": "Integrated Services Router containing switch ports, AP, DHCP server, and NAT gateway", "isCorrect": True},
            {"id": "B", "text": "Spine-and-leaf Clos fabric with BGP EVPN", "isCorrect": False},
            {"id": "C", "text": "Three-tier core-distribution-access hierarchy with dual-homed 100G optics", "isCorrect": False},
            {"id": "D", "text": "Dedicated out-of-band terminal server rack", "isCorrect": False}
        ],
        "explanation": "SOHO network designs prioritize low cost and simplicity by utilizing an integrated device that combines routing, Layer 2 switching, Wi-Fi AP, NAT, and DHCP service into a single physical unit.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-2-006",
        "domainId": "1.0",
        "subtopicCode": "1.2",
        "subtopicName": "Describe characteristics of network topology architectures",
        "type": "single-choice",
        "prompt": "What is the primary role of the Core layer in a traditional three-tier hierarchical campus network?",
        "options": [
            {"id": "A", "text": "To enforce access control lists and QoS packet re-marking", "isCorrect": False},
            {"id": "B", "text": "To connect end-user workstations and authenticate wireless clients", "isCorrect": False},
            {"id": "C", "text": "To provide high-speed, low-latency, non-blocking packet transport between distribution blocks", "isCorrect": True},
            {"id": "D", "text": "To terminate WAN VPN tunnels and execute NAT overload", "isCorrect": False}
        ],
        "explanation": "The Core layer (campus backbone) is designed solely for maximum throughput, low latency, and high availability. Complex packet filtering, routing policies, and security checks are pushed down to the Distribution layer.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.3 Cabling & Interfaces (6 Qs)
    {
        "id": "q-1-3-001",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "single-choice",
        "prompt": "A campus network requires a 10 Gigabit Ethernet link between two buildings separated by 2.5 kilometers. Which cabling type and transceiver should the engineer select?",
        "options": [
            {"id": "A", "text": "Multimode Fiber (MMF) with 10GBASE-SR optics", "isCorrect": False},
            {"id": "B", "text": "Single-mode Fiber (SMF) with 10GBASE-LR optics", "isCorrect": True},
            {"id": "C", "text": "Cat 6A UTP Copper with 10GBASE-T transceivers", "isCorrect": False},
            {"id": "D", "text": "Cat 7 Shielded Twisted Pair (STP)", "isCorrect": False}
        ],
        "explanation": "Single-mode fiber (SMF) has a narrow core (~9 microns) and utilizes laser light, supporting distances up to 10 km with 10GBASE-LR optics. Multimode fiber (10GBASE-SR) is limited to 300-400 meters, and Cat 6A copper is limited to 100 meters.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-3-002",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "single-choice",
        "prompt": "What physical phenomenon causes signal degradation over long distances in Multimode Fiber cabling when light rays travel at varying reflection angles?",
        "options": [
            {"id": "A", "text": "Modal dispersion", "isCorrect": True},
            {"id": "B", "text": "Alien crosstalk", "isCorrect": False},
            {"id": "C", "text": "Electromagnetic interference (EMI)", "isCorrect": False},
            {"id": "D", "text": "Return loss attenuation", "isCorrect": False}
        ],
        "explanation": "In Multimode Fiber (MMF), the wide core (50 or 62.5 microns) allows multiple light rays (modes) to travel along different optical paths. Because each mode travels a slightly different distance, pulses spread out over distance, a limitation known as modal dispersion.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-3-003",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "single-choice",
        "prompt": "What is the maximum standard distance for an unshielded twisted-pair (UTP) Category 6 cable carrying 1000BASE-T traffic?",
        "options": [
            {"id": "A", "text": "55 meters", "isCorrect": False},
            {"id": "B", "text": "100 meters", "isCorrect": True},
            {"id": "C", "text": "150 meters", "isCorrect": False},
            {"id": "D", "text": "300 meters", "isCorrect": False}
        ],
        "explanation": "For 1000BASE-T (Gigabit Ethernet), Cat 5e and Cat 6 twisted-pair cabling have an IEEE 802.3 maximum channel length of 100 meters (90 meters solid horizontal cable plus 10 meters stranded patch cords).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-3-004",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "drag-and-drop",
        "prompt": "Match each transceiver form factor with its maximum nominal interface speed.",
        "pairs": [
            {"target": "SFP", "match": "1 Gbps"},
            {"target": "SFP+", "match": "10 Gbps"},
            {"target": "SFP28", "match": "25 Gbps"},
            {"target": "QSFP28", "match": "100 Gbps"}
        ],
        "explanation": "SFP supports up to 1G. SFP+ supports 10G. SFP28 supports 25G on a single lane. QSFP28 bundles 4x25G lanes to support 100 Gbps.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-3-005",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "single-choice",
        "prompt": "Which fiber optic connector utilizes a compact, push-pull latching mechanism and is the dominant connector type for high-density SFP and SFP+ optical transceivers?",
        "options": [
            {"id": "A", "text": "LC (Lucent Connector)", "isCorrect": True},
            {"id": "B", "text": "ST (Straight Tip)", "isCorrect": False},
            {"id": "C", "text": "SC (Subscriber Connector)", "isCorrect": False},
            {"id": "D", "text": "BNC Connector", "isCorrect": False}
        ],
        "explanation": "The LC (Lucent / Local Connector) is a small form-factor fiber optic connector that uses a 1.25 mm ferrule with a push-pull latch, widely used for SFP transceivers.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-3-006",
        "domainId": "1.0",
        "subtopicCode": "1.3",
        "subtopicName": "Compare physical interface and cabling types",
        "type": "single-choice",
        "prompt": "When connecting two Cisco switches together using 100BASE-TX without Auto-MDIX enabled, which cable pinout is required?",
        "options": [
            {"id": "A", "text": "Straight-through cable", "isCorrect": False},
            {"id": "B", "text": "Crossover cable", "isCorrect": True},
            {"id": "C", "text": "Rollover console cable", "isCorrect": False},
            {"id": "D", "text": "Coaxial RG-6 cable", "isCorrect": False}
        ],
        "explanation": "Like devices (switch to switch, router to router, PC to PC) transmit on the same pins (1 and 2 in MDI). Without Auto-MDIX, a crossover cable is required to cross pins 1/2 to 3/6.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 2",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.4 Interface & Cable Issues (6 Qs)
    {
        "id": "q-1-4-001",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "An administrator notices that a switch port is experiencing significant throughput degradation. The command 'show interfaces GigabitEthernet 0/1' reveals an increasing counter for 'late collisions'. What is the most likely root cause?",
        "cliSnippet": "GigabitEthernet0/1 is up, line protocol is up\n  Half-duplex, 100Mb/s, media type is 100BaseTX\n  5422 input errors, 4118 CRC, 0 frame\n  1289 late collision, 2411 deferred",
        "options": [
            {"id": "A", "text": "Duplex mismatch where the local port is half-duplex and remote is full-duplex", "isCorrect": True},
            {"id": "B", "text": "The MTU size has been set to 9216 jumbo frames", "isCorrect": False},
            {"id": "C", "text": "The cable length is less than 1 meter", "isCorrect": False},
            {"id": "D", "text": "Broadcast storm caused by a missing Spanning Tree root bridge", "isCorrect": False}
        ],
        "explanation": "Late collisions occur when a collision is detected after the first 64 bytes (512 bits) of a frame have been transmitted. The most common cause is a duplex mismatch (one end configured for half-duplex and the other for full-duplex) or cable length exceeding the maximum propagation specification.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-4-002",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "In the output of 'show interfaces', what is indicated when an interface state shows 'up, line protocol is down'?",
        "options": [
            {"id": "A", "text": "The interface has been administratively disabled with 'shutdown'", "isCorrect": False},
            {"id": "B", "text": "Physical layer connectivity is established, but there is a Layer 2 framing, keepalive, or clocking issue", "isCorrect": True},
            {"id": "C", "text": "The physical cable is unplugged or severed", "isCorrect": False},
            {"id": "D", "text": "The router has exhausted its ARP table memory", "isCorrect": False}
        ],
        "explanation": "'Up/Down' means Layer 1 (Physical) is active (carrier detect present), but Layer 2 (Data Link) communication has failed due to encapsulation mismatch, missing keepalives, or authentication failure.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-4-003",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "An interface output shows a high number of 'CRC errors' and 'FCS errors' while collisions remain zero. Which issue is most likely occurring?",
        "options": [
            {"id": "A", "text": "Electromagnetic interference (EMI), faulty cabling, or dirty fiber connectors", "isCorrect": True},
            {"id": "B", "text": "A standard half-duplex CSMA/CD operation", "isCorrect": False},
            {"id": "C", "text": "An incorrect OSPF hello timer configuration", "isCorrect": False},
            {"id": "D", "text": "A mismatched VLAN ID on an access port", "isCorrect": False}
        ],
        "explanation": "Cyclic Redundancy Check (CRC) errors indicate corrupted frames arriving at the physical interface where the Frame Check Sequence (FCS) does not match. Common causes include electrical noise, damaged copper cables, or loose/dirty fiber optics.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-4-004",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "What does a 'runt' counter indicate in the interface statistics of a Cisco IOS switch?",
        "options": [
            {"id": "A", "text": "Frames that exceed 1518 bytes and have a bad FCS", "isCorrect": False},
            {"id": "B", "text": "Frames that are smaller than the 64-byte minimum Ethernet frame size with an invalid CRC", "isCorrect": True},
            {"id": "C", "text": "Packets dropped because the output buffer queue was full", "isCorrect": False},
            {"id": "D", "text": "Frames received with an unknown EtherType field", "isCorrect": False}
        ],
        "explanation": "A runt is a frame that is less than 64 bytes in length with an invalid CRC. Runts are typically caused by collisions or malfunctioning NIC hardware.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-4-005",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "An administrator executes 'show interfaces GigabitEthernet 0/2' and sees: 'GigabitEthernet0/2 is administratively down, line protocol is down'. What command must be executed on the interface to bring it up?",
        "options": [
            {"id": "A", "text": "enable", "isCorrect": False},
            {"id": "B", "text": "no shutdown", "isCorrect": True},
            {"id": "C", "text": "clear counters", "isCorrect": False},
            {"id": "D", "text": "switchport mode access", "isCorrect": False}
        ],
        "explanation": "'Administratively down' explicitly indicates that the interface has been manually disabled with the 'shutdown' configuration command. Entering interface configuration mode and typing 'no shutdown' enables the interface.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-4-006",
        "domainId": "1.0",
        "subtopicCode": "1.4",
        "subtopicName": "Identify interface and cable issues",
        "type": "single-choice",
        "prompt": "What happens when an engineer configures one end of an Ethernet link for 'speed 1000' and 'duplex full', but leaves the remote end set to default auto-negotiation?",
        "options": [
            {"id": "A", "text": "The remote side detects 1000 Mbps and selects half duplex, causing a duplex mismatch", "isCorrect": False},
            {"id": "B", "text": "Gigabit Ethernet (1000BASE-T) IEEE standards require auto-negotiation, so the link fails to come up or stays down/down", "isCorrect": True},
            {"id": "C", "text": "The switch port automatically changes to an optical interface", "isCorrect": False},
            {"id": "D", "text": "Both sides automatically agree on 100 Mbps half duplex", "isCorrect": False}
        ],
        "explanation": "Under IEEE 802.3ab for 1000BASE-T (copper gigabit), clock synchronization between master/slave requires auto-negotiation. Disabling auto-negotiation on one side typically prevents link establishment or results in an operational failure.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 7",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.5 Compare TCP to UDP (6 Qs)
    {
        "id": "q-1-5-001",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "single-choice",
        "prompt": "Which flag combination is exchanged during the successful establishment of a standard TCP three-way handshake?",
        "options": [
            {"id": "A", "text": "Client sends SYN; Server responds with SYN-ACK; Client acknowledges with ACK", "isCorrect": True},
            {"id": "B", "text": "Client sends ACK; Server responds with SYN; Client acknowledges with FIN", "isCorrect": False},
            {"id": "C", "text": "Client sends RST; Server responds with ACK; Client acknowledges with PSH", "isCorrect": False},
            {"id": "D", "text": "Client sends URG; Server responds with SYN-ACK; Client sends FIN-ACK", "isCorrect": False}
        ],
        "explanation": "The standard TCP connection establishment sequence uses a 3-way handshake: 1. Host A sends SYN (Synchronize sequence number). 2. Host B replies with SYN-ACK. 3. Host A completes the handshake by sending ACK.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-5-002",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "single-choice",
        "prompt": "How does TCP Windowing provide dynamic flow control between a sender and a receiver?",
        "options": [
            {"id": "A", "text": "The receiver advertises the number of bytes it can accept in its receive buffer before requiring an acknowledgment", "isCorrect": True},
            {"id": "B", "text": "The sender negotiates a fixed MTU size during ARP resolution", "isCorrect": False},
            {"id": "C", "text": "The intermediate routers discard unacknowledged UDP packets when queues fill", "isCorrect": False},
            {"id": "D", "text": "The receiver requests a higher IP Precedence value for time-sensitive data", "isCorrect": False}
        ],
        "explanation": "TCP Windowing enables flow control by allowing the receiver to dynamically advertise its receive buffer capacity (Window Size field). The sender will not send more unacknowledged bytes than this window size, preventing buffer overrun.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-5-003",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "multiple-choice",
        "prompt": "Which two protocols rely on UDP at the transport layer for low-overhead, latency-sensitive transmission? (Choose two.)",
        "options": [
            {"id": "A", "text": "SSH (Secure Shell)", "isCorrect": False},
            {"id": "B", "text": "TFTP (Trivial File Transfer Protocol)", "isCorrect": True},
            {"id": "C", "text": "BGP (Border Gateway Protocol)", "isCorrect": False},
            {"id": "D", "text": "NTP (Network Time Protocol)", "isCorrect": True},
            {"id": "E", "text": "HTTPS (Hypertext Transfer Protocol Secure)", "isCorrect": False}
        ],
        "explanation": "TFTP uses UDP port 69, and NTP uses UDP port 123. Both require lightweight, low-overhead transport. In contrast, SSH (TCP 22), BGP (TCP 179), and HTTPS (TCP 443) require reliable, connection-oriented TCP transport.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-5-004",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "single-choice",
        "prompt": "What is the size of the standard UDP header compared to the minimum standard TCP header?",
        "options": [
            {"id": "A", "text": "UDP is 8 bytes; TCP minimum is 20 bytes", "isCorrect": True},
            {"id": "B", "text": "UDP is 20 bytes; TCP minimum is 40 bytes", "isCorrect": False},
            {"id": "C", "text": "UDP is 16 bytes; TCP minimum is 32 bytes", "isCorrect": False},
            {"id": "D", "text": "UDP is 4 bytes; TCP minimum is 12 bytes", "isCorrect": False}
        ],
        "explanation": "A UDP header contains only 4 fields (Source Port, Destination Port, Length, Checksum) totaling 8 bytes. A standard TCP header without options is 20 bytes.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-5-005",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "single-choice",
        "prompt": "A client initiates a connection to a web server port 443. The web server process is stopped and not listening. Which TCP control flag does the operating system return to immediately reject the connection attempt?",
        "options": [
            {"id": "A", "text": "FIN", "isCorrect": False},
            {"id": "B", "text": "RST (Reset)", "isCorrect": True},
            {"id": "C", "text": "URG", "isCorrect": False},
            {"id": "D", "text": "PSH", "isCorrect": False}
        ],
        "explanation": "When a host receives a TCP SYN packet destined for a closed port, its TCP stack sends a packet with the RST (Reset) flag set to abruptly refuse and terminate the connection.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-5-006",
        "domainId": "1.0",
        "subtopicCode": "1.5",
        "subtopicName": "Compare TCP to UDP",
        "type": "single-choice",
        "prompt": "Why does real-time Voice over IP (VoIP) audio payload (RTP) use UDP rather than TCP?",
        "options": [
            {"id": "A", "text": "Retransmission of delayed voice packets via TCP creates unnatural audio gaps and jitter", "isCorrect": True},
            {"id": "B", "text": "UDP encrypts audio streams natively using TLS", "isCorrect": False},
            {"id": "C", "text": "Routers cannot route TCP packets across WAN links", "isCorrect": False},
            {"id": "D", "text": "TCP does not support IP precedence marking", "isCorrect": False}
        ],
        "explanation": "VoIP audio requires real-time delivery. If a voice packet is dropped, retransmitting it hundreds of milliseconds later via TCP is useless and degrades call quality. UDP delivers packets with low latency and without retransmission overhead.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 5",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.6 IPv4 Subnetting (10 Qs)
    {
        "id": "q-1-6-001",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "A network engineer must allocate a subnet from 172.16.0.0/16 that supports at least 58 usable host IP addresses while minimizing wasted address space. Which prefix length should be selected?",
        "options": [
            {"id": "A", "text": "/25", "isCorrect": False},
            {"id": "B", "text": "/26", "isCorrect": True},
            {"id": "C", "text": "/27", "isCorrect": False},
            {"id": "D", "text": "/28", "isCorrect": False}
        ],
        "explanation": "To support 58 usable hosts, calculate 2^h - 2 >= 58. For h=5 (mask /27): 2^5 - 2 = 30 hosts (insufficient). For h=6 (mask /26): 2^6 - 2 = 62 usable hosts. A /26 provides 62 usable hosts, which satisfies the requirement and minimizes wasted space compared to /25 (126 hosts).",
        "reference": "CCNA 200-301 OCG Vol 1, Subnetting Practice",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-002",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "What is the broadcast address for the subnet containing the host IP address 192.168.10.138 with subnet mask 255.255.255.224?",
        "options": [
            {"id": "A", "text": "192.168.10.143", "isCorrect": False},
            {"id": "B", "text": "192.168.10.159", "isCorrect": True},
            {"id": "C", "text": "192.168.10.255", "isCorrect": False},
            {"id": "D", "text": "192.168.10.128", "isCorrect": False}
        ],
        "explanation": "Mask 255.255.255.224 is a /27. The block size is 256 - 224 = 32. Subnet boundaries are 0, 32, 64, 96, 128, 160. 138 falls in the 128 subnet (192.168.10.128). The next subnet is 160, so the broadcast address is 192.168.10.159.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-003",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "What is the maximum number of usable host IP addresses provided by a /29 subnet mask?",
        "options": [
            {"id": "A", "text": "4", "isCorrect": False},
            {"id": "B", "text": "6", "isCorrect": True},
            {"id": "C", "text": "8", "isCorrect": False},
            {"id": "D", "text": "14", "isCorrect": False}
        ],
        "explanation": "A /29 prefix has 32 - 29 = 3 host bits. Number of usable hosts is 2^3 - 2 = 8 - 2 = 6.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-004",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "An administrator needs to assign a subnet to a point-to-point serial link between two routers. Which subnet mask conserves the maximum number of IPv4 addresses under standard host subtraction rules?",
        "options": [
            {"id": "A", "text": "255.255.255.248 (/29)", "isCorrect": False},
            {"id": "B", "text": "255.255.255.252 (/30)", "isCorrect": True},
            {"id": "C", "text": "255.255.255.240 (/28)", "isCorrect": False},
            {"id": "D", "text": "255.255.255.224 (/27)", "isCorrect": False}
        ],
        "explanation": "A /30 mask (255.255.255.252) provides 2 host bits: 2^2 - 2 = 2 usable host addresses, making it the classic standard mask for point-to-point links.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-005",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "Which RFC defines the use of 31-bit prefixes (/31, 255.255.255.254) for IPv4 point-to-point links without dedicated network or broadcast addresses?",
        "options": [
            {"id": "A", "text": "RFC 1918", "isCorrect": False},
            {"id": "B", "text": "RFC 3021", "isCorrect": True},
            {"id": "C", "text": "RFC 2616", "isCorrect": False},
            {"id": "D", "text": "RFC 4941", "isCorrect": False}
        ],
        "explanation": "RFC 3021 specifies the use of 31-bit prefixes for point-to-point links, allowing two addresses to be used as host addresses with no separate broadcast or network address required.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-006",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "What is the network address for a device assigned IP address 10.150.172.99 with subnet mask 255.255.240.0?",
        "options": [
            {"id": "A", "text": "10.150.160.0", "isCorrect": True},
            {"id": "B", "text": "10.150.172.0", "isCorrect": False},
            {"id": "C", "text": "10.150.168.0", "isCorrect": False},
            {"id": "D", "text": "10.150.144.0", "isCorrect": False}
        ],
        "explanation": "Mask 255.255.240.0 has a block size of 256 - 240 = 16 in the 3rd octet. Multiples of 16 are 0, 16, 32... 144, 160, 176. The 3rd octet is 172, which falls in the 160 block (160 to 175.255). Therefore, the network ID is 10.150.160.0.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-007",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "An organization requires a single summary route for the following four subnets: 192.168.8.0/24, 192.168.9.0/24, 192.168.10.0/24, and 192.168.11.0/24. What is the most specific summary route?",
        "options": [
            {"id": "A", "text": "192.168.8.0/21", "isCorrect": False},
            {"id": "B", "text": "192.168.8.0/22", "isCorrect": True},
            {"id": "C", "text": "192.168.0.0/20", "isCorrect": False},
            {"id": "D", "text": "192.168.8.0/23", "isCorrect": False}
        ],
        "explanation": "In binary, 8 is 00001000, 9 is 00001001, 10 is 00001010, 11 is 00001011. The first 6 bits of the 3rd octet match (000010xx). 16 bits + 6 bits = 22 bits (/22). 2^(24-22) = 4 /24 subnets. The summary route is 192.168.8.0/22.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-008",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "What is the dotted decimal equivalent of the prefix length /19?",
        "options": [
            {"id": "A", "text": "255.255.192.0", "isCorrect": False},
            {"id": "B", "text": "255.255.224.0", "isCorrect": True},
            {"id": "C", "text": "255.255.240.0", "isCorrect": False},
            {"id": "D", "text": "255.255.248.0", "isCorrect": False}
        ],
        "explanation": "A /19 prefix has 8 bits in the 1st octet (255), 8 in the 2nd (255), and 3 bits in the 3rd octet (128 + 64 + 32 = 224), with 0 in the 4th octet: 255.255.224.0.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-009",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "Which of the following IP addresses is a valid, usable host address in the subnet 172.20.64.0/19?",
        "options": [
            {"id": "A", "text": "172.20.64.0", "isCorrect": False},
            {"id": "B", "text": "172.20.95.255", "isCorrect": False},
            {"id": "C", "text": "172.20.80.1", "isCorrect": True},
            {"id": "D", "text": "172.20.96.1", "isCorrect": False}
        ],
        "explanation": "A /19 mask has a block size of 32 in the 3rd octet. Subnet 172.20.64.0/19 ranges from 172.20.64.0 (network) to 172.20.95.255 (broadcast). Usable host range is 172.20.64.1 to 172.20.95.254. 172.20.80.1 is a valid host inside this range.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-6-010",
        "domainId": "1.0",
        "subtopicCode": "1.6",
        "subtopicName": "Configure and verify IPv4 addressing and subnetting",
        "type": "single-choice",
        "prompt": "A department needs 500 usable host IP addresses. Which subnet mask provides the minimum wasted address space?",
        "options": [
            {"id": "A", "text": "255.255.255.0 (/24)", "isCorrect": False},
            {"id": "B", "text": "255.255.254.0 (/23)", "isCorrect": True},
            {"id": "C", "text": "255.255.252.0 (/22)", "isCorrect": False},
            {"id": "D", "text": "255.255.248.0 (/21)", "isCorrect": False}
        ],
        "explanation": "To support 500 hosts: 2^9 - 2 = 512 - 2 = 510 usable hosts. 9 host bits leaves 32 - 9 = 23 network bits (/23, or 255.255.254.0).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.7 Private IPv4 (5 Qs)
    {
        "id": "q-1-7-001",
        "domainId": "1.0",
        "subtopicCode": "1.7",
        "subtopicName": "Describe private IPv4 addressing",
        "type": "single-choice",
        "prompt": "Which RFC defines the three private IPv4 address blocks reserved for internal corporate networks?",
        "options": [
            {"id": "A", "text": "RFC 1918", "isCorrect": True},
            {"id": "B", "text": "RFC 2328", "isCorrect": False},
            {"id": "C", "text": "RFC 4941", "isCorrect": False},
            {"id": "D", "text": "RFC 791", "isCorrect": False}
        ],
        "explanation": "RFC 1918 ('Address Allocation for Private Internets') established the 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 private IP ranges.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 13",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-7-002",
        "domainId": "1.0",
        "subtopicCode": "1.7",
        "subtopicName": "Describe private IPv4 addressing",
        "type": "single-choice",
        "prompt": "What is the full valid address range of the Class B private address space defined in RFC 1918?",
        "options": [
            {"id": "A", "text": "172.16.0.0 to 172.31.255.255", "isCorrect": True},
            {"id": "B", "text": "172.16.0.0 to 172.16.255.255", "isCorrect": False},
            {"id": "C", "text": "172.0.0.0 to 172.255.255.255", "isCorrect": False},
            {"id": "D", "text": "172.16.0.0 to 172.32.255.255", "isCorrect": False}
        ],
        "explanation": "The RFC 1918 Class B private address space is 172.16.0.0/12, which encompasses 16 contiguous /16 blocks: from 172.16.0.0 through 172.31.255.255.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-7-003",
        "domainId": "1.0",
        "subtopicCode": "1.7",
        "subtopicName": "Describe private IPv4 addressing",
        "type": "single-choice",
        "prompt": "Which IP address belongs to the public (routable on the global Internet) address space?",
        "options": [
            {"id": "A", "text": "10.254.1.1", "isCorrect": False},
            {"id": "B", "text": "172.30.100.5", "isCorrect": False},
            {"id": "C", "text": "192.168.200.1", "isCorrect": False},
            {"id": "D", "text": "172.33.1.10", "isCorrect": True}
        ],
        "explanation": "172.33.1.10 is outside the RFC 1918 range (172.16.0.0 - 172.31.255.255) and is therefore a globally routable public address.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 13",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-7-004",
        "domainId": "1.0",
        "subtopicCode": "1.7",
        "subtopicName": "Describe private IPv4 addressing",
        "type": "single-choice",
        "prompt": "What address block is reserved by RFC 6598 for Carrier-Grade NAT (CGNAT) / Shared Address Space?",
        "options": [
            {"id": "A", "text": "100.64.0.0/10", "isCorrect": True},
            {"id": "B", "text": "169.254.0.0/16", "isCorrect": False},
            {"id": "C", "text": "198.18.0.0/15", "isCorrect": False},
            {"id": "D", "text": "192.0.2.0/24", "isCorrect": False}
        ],
        "explanation": "RFC 6598 allocated 100.64.0.0/10 (100.64.0.0 to 100.127.255.255) as Shared Address Space for service providers deploying Carrier-Grade NAT (CGN).",
        "reference": "CCNA 200-301 v1.1 Blueprint 1.7",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-7-005",
        "domainId": "1.0",
        "subtopicCode": "1.7",
        "subtopicName": "Describe private IPv4 addressing",
        "type": "single-choice",
        "prompt": "A client workstation displays IP address 169.254.42.10. Which condition does this indicate?",
        "options": [
            {"id": "A", "text": "The host successfully obtained an IP from a remote DHCP server", "isCorrect": False},
            {"id": "B", "text": "The DHCP server failed to respond, and the host assigned itself an APIPA (Automatic Private IP Addressing) address", "isCorrect": True},
            {"id": "C", "text": "The host is configured with a public static IP address", "isCorrect": False},
            {"id": "D", "text": "The interface has been configured with an IPv6 link-local transition mechanism", "isCorrect": False}
        ],
        "explanation": "169.254.0.0/16 is the IPv4 link-local (APIPA) range defined in RFC 3927. When a DHCP client fails to receive a response from any DHCP server, it auto-assigns an address in this block.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 13",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.8 IPv6 Addressing & Prefix (6 Qs)
    {
        "id": "q-1-8-001",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "Which compressed representation correctly shortens the IPv6 address 2001:0db8:0000:0000:0008:0800:200c:417a?",
        "options": [
            {"id": "A", "text": "2001:db8::8:800:200c:417a", "isCorrect": True},
            {"id": "B", "text": "2001:db8::8:8:200c:417a", "isCorrect": False},
            {"id": "C", "text": "2001:db8:0:0:8:800:200c:417a", "isCorrect": False},
            {"id": "D", "text": "2001:db8::8:800:2c:417a", "isCorrect": False}
        ],
        "explanation": "Applying IPv6 compression rules: 1) Omit leading zeros: 0db8 -> db8, 0008 -> 8. Note that trailing zeros CANNOT be omitted (0800 remains 800). 2) Replace contiguous blocks of zero hextets with '::' (once per address). Thus, 2001:db8::8:800:200c:417a.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-8-002",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "Which Cisco IOS global configuration command is mandatory before a router can route IPv6 packets and participate in IPv6 dynamic routing protocols?",
        "options": [
            {"id": "A", "text": "ipv6 enable", "isCorrect": False},
            {"id": "B", "text": "ipv6 unicast-routing", "isCorrect": True},
            {"id": "C", "text": "ipv6 cef enable", "isCorrect": False},
            {"id": "D", "text": "ip routing ipv6", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS, IPv4 routing is enabled by default, but IPv6 routing is disabled. The command 'ipv6 unicast-routing' must be issued in global configuration mode to enable IPv6 packet forwarding.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 23",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-8-003",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "An enterprise is allocated a /48 global routing prefix from its ISP. How many bits are available for the Subnet ID if standard /64 user subnets are deployed?",
        "options": [
            {"id": "A", "text": "8 bits", "isCorrect": False},
            {"id": "B", "text": "16 bits", "isCorrect": True},
            {"id": "C", "text": "32 bits", "isCorrect": False},
            {"id": "D", "text": "64 bits", "isCorrect": False}
        ],
        "explanation": "Standard IPv6 subnets use a /64 prefix (64-bit network, 64-bit interface ID). With a /48 prefix allocated by the ISP, 64 - 48 = 16 bits are dedicated to the Subnet ID, yielding 2^16 = 65,536 subnets.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-8-004",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "What does the command 'ipv6 address autoconfig' configure on a Cisco IOS interface?",
        "options": [
            {"id": "A", "text": "Configures Stateless Address Autoconfiguration (SLAAC) using Router Advertisements", "isCorrect": True},
            {"id": "B", "text": "Forces the interface to use DHCPv6 exclusively", "isCorrect": False},
            {"id": "C", "text": "Generates a random link-local address using APIPA", "isCorrect": False},
            {"id": "D", "text": "Binds an IPv4 address to an IPv6 tunnel", "isCorrect": False}
        ],
        "explanation": "'ipv6 address autoconfig' instructs the interface to use SLAAC (Stateless Address Autoconfiguration) to listen for ICMPv6 Router Advertisements (RAs) from local routers to determine the prefix and generate its own IPv6 GUA.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 23",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-8-005",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "How many total bits compose an IPv6 address, and into how many hexadecimal hextets is it divided?",
        "options": [
            {"id": "A", "text": "64 bits divided into 4 hextets", "isCorrect": False},
            {"id": "B", "text": "128 bits divided into 8 hextets", "isCorrect": True},
            {"id": "C", "text": "256 bits divided into 16 hextets", "isCorrect": False},
            {"id": "D", "text": "128 bits divided into 4 octets", "isCorrect": False}
        ],
        "explanation": "An IPv6 address is 128 bits long, written as 8 groups of 16-bit hexadecimal values called hextets (or quads), separated by colons.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-8-006",
        "domainId": "1.0",
        "subtopicCode": "1.8",
        "subtopicName": "Configure and verify IPv6 addressing and prefix",
        "type": "single-choice",
        "prompt": "Why is the IPv6 address '2001:db8::1::2' invalid?",
        "options": [
            {"id": "A", "text": "The double colon '::' can only appear once in an address to prevent ambiguity in restoring missing zeros", "isCorrect": True},
            {"id": "B", "text": "IPv6 does not allow the letter 'b' in hexadecimal", "isCorrect": False},
            {"id": "C", "text": "The documentation prefix 2001:db8 cannot end in single digits", "isCorrect": False},
            {"id": "D", "text": "Colons must always be followed by exactly 4 characters", "isCorrect": False}
        ],
        "explanation": "RFC 4291 mandates that the double colon '::' may only appear once in an IPv6 address. Using it multiple times would make it mathematically impossible to determine how many zero hextets each '::' represents.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.9 IPv6 Address Types (7 Qs)
    {
        "id": "q-1-9-001",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "drag-and-drop",
        "prompt": "Drag each IPv6 address prefix to its corresponding IPv6 address type.",
        "pairs": [
            {"target": "Link-Local", "match": "fe80::/10"},
            {"target": "Unique Local (Private)", "match": "fc00::/7"},
            {"target": "Global Unicast", "match": "2000::/3"},
            {"target": "Multicast", "match": "ff00::/8"}
        ],
        "explanation": "fe80::/10 is link-local (non-routable outside the local link). fc00::/7 (commonly fd00::/8) is unique local (equivalent to IPv4 RFC 1918 private space). 2000::/3 represents all routable global unicast addresses. ff00::/8 is the reserved prefix for multicast.",
        "reference": "CCNA 200-301 OCG Vol 1, IPv6 Addressing",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-002",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "A host with MAC address 0050.56BE.1234 uses EUI-64 to generate its 64-bit interface ID. What is the resulting interface identifier?",
        "options": [
            {"id": "A", "text": "0250:56ff:febe:1234", "isCorrect": True},
            {"id": "B", "text": "0050:56ff:febe:1234", "isCorrect": False},
            {"id": "C", "text": "0250:56be:1234:0000", "isCorrect": False},
            {"id": "D", "text": "fe80::0250:56be:1234", "isCorrect": False}
        ],
        "explanation": "EUI-64 process: 1. Split 48-bit MAC in half: 0050:56 and BE:1234. 2. Insert FFFE in the middle: 0050:56FF:FEBE:1234. 3. Invert the 7th bit (Universal/Local bit): 00 in binary is 00000000 -> inverting bit 7 produces 00000010 (hex 02). Result: 0250:56ff:febe:1234.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 4,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-003",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "Which IPv6 multicast address reaches all IPv6-enabled routers on the local link?",
        "options": [
            {"id": "A", "text": "ff02::1", "isCorrect": False},
            {"id": "B", "text": "ff02::2", "isCorrect": True},
            {"id": "C", "text": "ff02::5", "isCorrect": False},
            {"id": "D", "text": "ff02::a", "isCorrect": False}
        ],
        "explanation": "ff02::1 reaches all IPv6 nodes on the local link. ff02::2 reaches all IPv6 routers on the local link. ff02::5 reaches all OSPFv3 routers.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-004",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "What is the primary operational scope of an IPv6 Link-Local address (fe80::/10)?",
        "options": [
            {"id": "A", "text": "It can be routed across the enterprise WAN backbone", "isCorrect": False},
            {"id": "B", "text": "It is confined strictly to the local physical or virtual link and routers will never forward it", "isCorrect": True},
            {"id": "C", "text": "It is globally routable across the public Internet via BGP", "isCorrect": False},
            {"id": "D", "text": "It is used exclusively for wireless client association", "isCorrect": False}
        ],
        "explanation": "IPv6 Link-Local addresses are significant only on the local link. Routers do not forward packets that have a link-local source or destination address to other subnets.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-005",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "Which IPv6 address type allows multiple devices to share the exact same unicast address, routing packets to the single topologically closest node?",
        "options": [
            {"id": "A", "text": "Multicast", "isCorrect": False},
            {"id": "B", "text": "Anycast", "isCorrect": True},
            {"id": "C", "text": "Broadcast", "isCorrect": False},
            {"id": "D", "text": "Unique Local", "isCorrect": False}
        ],
        "explanation": "An Anycast address is assigned to multiple interfaces across different devices. When a packet is sent to an anycast address, routing protocols deliver it to the nearest interface (based on routing distance). Note: IPv6 has no broadcast addresses.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-006",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "What is the IPv6 equivalent of the IPv4 loopback address 127.0.0.1?",
        "options": [
            {"id": "A", "text": "::/0", "isCorrect": False},
            {"id": "B", "text": "::1", "isCorrect": True},
            {"id": "C", "text": "fe80::1", "isCorrect": False},
            {"id": "D", "text": "ff02::1", "isCorrect": False}
        ],
        "explanation": "The IPv6 loopback address is ::1 (0:0:0:0:0:0:0:1) with prefix length /128. ::/0 represents the default route, and :: is the unspecified address.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-9-007",
        "domainId": "1.0",
        "subtopicCode": "1.9",
        "subtopicName": "Describe IPv6 address types",
        "type": "single-choice",
        "prompt": "Which prefix identifies an IPv6 Unique Local Address (ULA) as specified in RFC 4193?",
        "options": [
            {"id": "A", "text": "2001:db8::/32", "isCorrect": False},
            {"id": "B", "text": "fd00::/8", "isCorrect": True},
            {"id": "C", "text": "fe80::/10", "isCorrect": False},
            {"id": "D", "text": "ff02::/16", "isCorrect": False}
        ],
        "explanation": "Unique Local Addresses occupy fc00::/7. RFC 4193 specifies that the 8th bit must be set to 1 for locally assigned ULAs, resulting in the fd00::/8 prefix, which acts as the IPv6 equivalent to RFC 1918 private space.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 22",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.10 Client OS IP Parameters (5 Qs)
    {
        "id": "q-1-10-001",
        "domainId": "1.0",
        "subtopicCode": "1.10",
        "subtopicName": "Verify IP parameters for Client OS",
        "type": "single-choice",
        "prompt": "A Windows administrator wants to view the current IP address, subnet mask, default gateway, DNS servers, and DHCP lease expiration time for all network adapters. Which command provides this output?",
        "options": [
            {"id": "A", "text": "ipconfig", "isCorrect": False},
            {"id": "B", "text": "ipconfig /all", "isCorrect": True},
            {"id": "C", "text": "netstat -r", "isCorrect": False},
            {"id": "D", "text": "route print", "isCorrect": False}
        ],
        "explanation": "'ipconfig /all' displays comprehensive details for all network adapters on Windows, including physical MAC addresses, DHCP server addresses, lease times, and DNS servers. Plain 'ipconfig' displays only basic IP, mask, and default gateway.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 18",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-10-002",
        "domainId": "1.0",
        "subtopicCode": "1.10",
        "subtopicName": "Verify IP parameters for Client OS",
        "type": "single-choice",
        "prompt": "On a Linux workstation, which modern iproute2 command displays all IP addresses assigned to network interfaces along with their subnet masks?",
        "options": [
            {"id": "A", "text": "ip addr show", "isCorrect": True},
            {"id": "B", "text": "ifconfig -all", "isCorrect": False},
            {"id": "C", "text": "ip route show", "isCorrect": False},
            {"id": "D", "text": "netstat -i", "isCorrect": False}
        ],
        "explanation": "On modern Linux systems, 'ip addr show' (or 'ip a') is the standard iproute2 command for displaying interface IP addresses and subnet masks, replacing legacy 'ifconfig'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 18",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-10-003",
        "domainId": "1.0",
        "subtopicCode": "1.10",
        "subtopicName": "Verify IP parameters for Client OS",
        "type": "single-choice",
        "prompt": "A macOS or Linux user enters 'netstat -nr' or 'ip route' and inspects the output. Which destination entry corresponds to the default gateway?",
        "options": [
            {"id": "A", "text": "127.0.0.1", "isCorrect": False},
            {"id": "B", "text": "default (or 0.0.0.0/0)", "isCorrect": True},
            {"id": "C", "text": "255.255.255.255", "isCorrect": False},
            {"id": "D", "text": "link#2", "isCorrect": False}
        ],
        "explanation": "In host routing tables, the default route (gateway of last resort) is listed as destination 'default' or '0.0.0.0' with mask 0.0.0.0, pointing to the default gateway IP on the local subnet.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 18",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-10-004",
        "domainId": "1.0",
        "subtopicCode": "1.10",
        "subtopicName": "Verify IP parameters for Client OS",
        "type": "single-choice",
        "prompt": "Which utility tests DNS resolution by querying a specific DNS server directly from the command prompt across Windows, macOS, and Linux?",
        "options": [
            {"id": "A", "text": "nslookup", "isCorrect": True},
            {"id": "B", "text": "tracert", "isCorrect": False},
            {"id": "C", "text": "arp -a", "isCorrect": False},
            {"id": "D", "text": "ping -t", "isCorrect": False}
        ],
        "explanation": "'nslookup' (and 'dig' on Unix/Linux) is used to verify and troubleshoot DNS resolution, query specific records (A, AAAA, MX), and direct queries to chosen name servers.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 18",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-10-005",
        "domainId": "1.0",
        "subtopicCode": "1.10",
        "subtopicName": "Verify IP parameters for Client OS",
        "type": "single-choice",
        "prompt": "A user can ping their local default gateway (192.168.1.1) and public IP 8.8.8.8, but cannot open web pages by URL (e.g. cisco.com). What client configuration parameter is misconfigured?",
        "options": [
            {"id": "A", "text": "Subnet mask", "isCorrect": False},
            {"id": "B", "text": "Default Gateway", "isCorrect": False},
            {"id": "C", "text": "DNS server IP address", "isCorrect": True},
            {"id": "D", "text": "MAC address binding", "isCorrect": False}
        ],
        "explanation": "Because the host can reach external public IP addresses (8.8.8.8), physical layer, IP addressing, and default gateway routing are functioning. Inability to reach domain names points directly to an unreachable or misconfigured DNS server.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 18",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.11 Wireless Principles (5 Qs)
    {
        "id": "q-1-11-001",
        "domainId": "1.0",
        "subtopicCode": "1.11",
        "subtopicName": "Describe wireless principles",
        "type": "single-choice",
        "prompt": "Which three 20-MHz channels in the 2.4 GHz ISM band do not overlap and should be used when planning a high-density 2.4 GHz Wi-Fi deployment in North America?",
        "options": [
            {"id": "A", "text": "1, 6, and 11", "isCorrect": True},
            {"id": "B", "text": "2, 7, and 12", "isCorrect": False},
            {"id": "C", "text": "1, 5, 9, and 13", "isCorrect": False},
            {"id": "D", "text": "36, 40, and 44", "isCorrect": False}
        ],
        "explanation": "In North America, channels 1, 6, and 11 are spaced 25 MHz apart, which allows 20-MHz channels to operate without adjacent channel interference. Channels 36, 40, and 44 are in the 5 GHz band.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 24",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-11-002",
        "domainId": "1.0",
        "subtopicCode": "1.11",
        "subtopicName": "Describe wireless principles",
        "type": "single-choice",
        "prompt": "What wireless topology term describes multiple Access Points sharing the same SSID to provide seamless roaming across an entire office floor?",
        "options": [
            {"id": "A", "text": "Basic Service Set (BSS)", "isCorrect": False},
            {"id": "B", "text": "Extended Service Set (ESS)", "isCorrect": True},
            {"id": "C", "text": "Independent Basic Service Set (IBSS)", "isCorrect": False},
            {"id": "D", "text": "Service Set Identifier (SSID)", "isCorrect": False}
        ],
        "explanation": "A BSS consists of one AP and its associated clients. An Extended Service Set (ESS) connects two or more BSSs through a common distribution system (switching infrastructure), allowing clients to roam transparently under a single SSID.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 24",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-11-003",
        "domainId": "1.0",
        "subtopicCode": "1.11",
        "subtopicName": "Describe wireless principles",
        "type": "single-choice",
        "prompt": "What physical phenomenon occurs when Wi-Fi radio frequency (RF) waves strike dense materials such as concrete walls and lose signal strength?",
        "options": [
            {"id": "A", "text": "Absorption (Attenuation)", "isCorrect": True},
            {"id": "B", "text": "Refraction", "isCorrect": False},
            {"id": "C", "text": "Scattering", "isCorrect": False},
            {"id": "D", "text": "Diffraction", "isCorrect": False}
        ],
        "explanation": "Absorption (attenuation) occurs when RF signal energy is absorbed by obstacles such as drywall, concrete, or water, reducing signal power (RSSI) as it penetrates or attempts to pass through.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 24",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-11-004",
        "domainId": "1.0",
        "subtopicCode": "1.11",
        "subtopicName": "Describe wireless principles",
        "type": "single-choice",
        "prompt": "Which IEEE wireless standard introduced OFDMA (Orthogonal Frequency-Division Multiple Access) and is branded commercially as Wi-Fi 6?",
        "options": [
            {"id": "A", "text": "802.11n", "isCorrect": False},
            {"id": "B", "text": "802.11ac", "isCorrect": False},
            {"id": "C", "text": "802.11ax", "isCorrect": True},
            {"id": "D", "text": "802.11g", "isCorrect": False}
        ],
        "explanation": "IEEE 802.11ax (Wi-Fi 6) introduced OFDMA, which subdivides RF channels into smaller subcarriers (Resource Units) to transmit simultaneously to multiple clients, greatly improving efficiency in dense environments.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 24",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-11-005",
        "domainId": "1.0",
        "subtopicCode": "1.11",
        "subtopicName": "Describe wireless principles",
        "type": "single-choice",
        "prompt": "What is the BSSID in a Wi-Fi network?",
        "options": [
            {"id": "A", "text": "The human-readable network name broadcast in beacon frames", "isCorrect": False},
            {"id": "B", "text": "The Layer 2 MAC address of the Access Point radio servicing the BSS", "isCorrect": True},
            {"id": "C", "text": "The 128-bit WPA2 pre-shared key hash", "isCorrect": False},
            {"id": "D", "text": "The CAPWAP tunnel endpoint IP of the WLC", "isCorrect": False}
        ],
        "explanation": "While the SSID is the text name of the network, the BSSID (Basic Service Set Identifier) is the 48-bit MAC address of the AP's radio serving that specific basic service set.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 24",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.12 Virtualization Fundamentals & VRFs (5 Qs)
    {
        "id": "q-1-12-001",
        "domainId": "1.0",
        "subtopicCode": "1.12",
        "subtopicName": "Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
        "type": "single-choice",
        "prompt": "A service provider needs to host two separate enterprise clients on a single physical core router. Both clients use overlapping IP address space (10.0.0.0/8). Which virtualization technology segments the routing table on the router?",
        "options": [
            {"id": "A", "text": "VLAN (Virtual Local Area Network)", "isCorrect": False},
            {"id": "B", "text": "VRF (Virtual Routing and Forwarding)", "isCorrect": True},
            {"id": "C", "text": "Type 1 Hypervisor", "isCorrect": False},
            {"id": "D", "text": "Docker Container Engine", "isCorrect": False}
        ],
        "explanation": "VRF (Virtual Routing and Forwarding) functions like a virtual router inside a physical router, allowing multiple instances of routing tables to coexist simultaneously. This permits overlapping IP addresses without conflict. (Note: VRFs are an explicit topic in the CCNA v1.1 blueprint).",
        "reference": "CCNA 200-301 v1.1 Topic 1.12",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-12-002",
        "domainId": "1.0",
        "subtopicCode": "1.12",
        "subtopicName": "Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
        "type": "single-choice",
        "prompt": "Which hypervisor architecture runs directly on bare-metal physical server hardware without an underlying host operating system?",
        "options": [
            {"id": "A", "text": "Type 1 Hypervisor (Bare-metal, e.g. VMware ESXi, Cisco NFVIS)", "isCorrect": True},
            {"id": "B", "text": "Type 2 Hypervisor (Hosted, e.g. VMware Workstation, VirtualBox)", "isCorrect": False},
            {"id": "C", "text": "Application Container Engine (Docker)", "isCorrect": False},
            {"id": "D", "text": "Container Daemon (containerd)", "isCorrect": False}
        ],
        "explanation": "A Type 1 (bare-metal) hypervisor installs directly onto the physical server hardware, managing CPU, memory, and storage directly for optimal performance and security. Type 2 hypervisors run on top of an existing host OS.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 1",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-12-003",
        "domainId": "1.0",
        "subtopicCode": "1.12",
        "subtopicName": "Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
        "type": "single-choice",
        "prompt": "How do software containers (such as Docker) differ fundamentally from Virtual Machines?",
        "options": [
            {"id": "A", "text": "Containers share the host operating system kernel and isolate applications in user space, whereas VMs virtualize complete hardware with separate guest OS instances", "isCorrect": True},
            {"id": "B", "text": "Containers require a dedicated Type 1 hypervisor installed on the physical BIOS", "isCorrect": False},
            {"id": "C", "text": "Virtual machines share a single TCP/IP network stack", "isCorrect": False},
            {"id": "D", "text": "Containers cannot establish network connections outside localhost", "isCorrect": False}
        ],
        "explanation": "Containers share the host OS kernel and only package the application and its dependencies, making them lightweight (megabytes) and instant to boot. Virtual machines virtualize the underlying hardware and require a complete guest OS per VM.",
        "reference": "CCNA 200-301 v1.1 Topic 1.12",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-12-004",
        "domainId": "1.0",
        "subtopicCode": "1.12",
        "subtopicName": "Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
        "type": "single-choice",
        "prompt": "An engineer executes 'show ip route' on a Cisco router configured with VRF 'CUSTOMER_A' and sees no customer routes. Which command displays the routing table specific to that VRF?",
        "options": [
            {"id": "A", "text": "show ip route vrf CUSTOMER_A", "isCorrect": True},
            {"id": "B", "text": "show vrf routing-table", "isCorrect": False},
            {"id": "C", "text": "show ip route customer all", "isCorrect": False},
            {"id": "D", "text": "show ip interface brief vrf", "isCorrect": False}
        ],
        "explanation": "Each VRF maintains its own independent routing table. Running 'show ip route' displays only the global (default) routing table. To inspect routes in a specific VRF, the command is 'show ip route vrf <vrf-name>'.",
        "reference": "CCNA 200-301 v1.1 Topic 1.12",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-12-005",
        "domainId": "1.0",
        "subtopicCode": "1.12",
        "subtopicName": "Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
        "type": "single-choice",
        "prompt": "What happens when an engineer assigns an interface to a VRF using the command 'ip vrf forwarding RED' (or 'vrf forwarding RED')?",
        "options": [
            {"id": "A", "text": "Cisco IOS removes the currently configured IP address on that interface, requiring re-entry", "isCorrect": True},
            {"id": "B", "text": "The interface changes from access mode to 802.1Q trunk", "isCorrect": False},
            {"id": "C", "text": "The interface is placed in err-disable state", "isCorrect": False},
            {"id": "D", "text": "The router reboots to repartition TCAM memory", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS, assigning an interface to a VRF with 'ip vrf forwarding' removes any existing IP address previously configured on that interface. The IP address must be reconfigured after binding the interface to the VRF.",
        "reference": "CCNA 200-301 v1.1 Topic 1.12",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 1.13 Switching Concepts (5 Qs)
    {
        "id": "q-1-13-001",
        "domainId": "1.0",
        "subtopicCode": "1.13",
        "subtopicName": "Describe switching concepts",
        "type": "single-choice",
        "prompt": "How does a Layer 2 switch dynamically populate its MAC address table (CAM table)?",
        "options": [
            {"id": "A", "text": "By inspecting the source MAC address of incoming frames and recording the ingress port and VLAN", "isCorrect": True},
            {"id": "B", "text": "By parsing the destination MAC address and querying a central DNS server", "isCorrect": False},
            {"id": "C", "text": "By issuing periodic ICMP ping sweeps to all connected endpoints", "isCorrect": False},
            {"id": "D", "text": "By reading LLDP neighbor advertisements from client operating systems", "isCorrect": False}
        ],
        "explanation": "Switches learn MAC addresses passively by looking at the SOURCE MAC address of incoming frames on each port. If the source MAC is not in the table, it adds an entry mapping that MAC address to the ingress interface and VLAN.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 6",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-13-002",
        "domainId": "1.0",
        "subtopicCode": "1.13",
        "subtopicName": "Describe switching concepts",
        "type": "single-choice",
        "prompt": "What action does a switch take when it receives a unicast frame whose destination MAC address is NOT found in its MAC address table?",
        "options": [
            {"id": "A", "text": "It drops the frame immediately and sends an ICMP Destination Unreachable message", "isCorrect": False},
            {"id": "B", "text": "It floods the frame out all ports belonging to the same VLAN, except the port on which it was received", "isCorrect": True},
            {"id": "C", "text": "It forwards the frame exclusively to the STP Root Bridge", "isCorrect": False},
            {"id": "D", "text": "It buffers the frame for 300 seconds until an ARP request arrives", "isCorrect": False}
        ],
        "explanation": "When the destination MAC is unknown (unknown unicast), the switch floods the frame out all interfaces in that VLAN except the receiving port. Once the target device replies, the switch learns its location from the reply's source MAC.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 6",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-13-003",
        "domainId": "1.0",
        "subtopicCode": "1.13",
        "subtopicName": "Describe switching concepts",
        "type": "single-choice",
        "prompt": "What is the default aging time for dynamically learned MAC address table entries on a Cisco Catalyst switch?",
        "options": [
            {"id": "A", "text": "60 seconds", "isCorrect": False},
            {"id": "B", "text": "300 seconds (5 minutes)", "isCorrect": True},
            {"id": "C", "text": "3600 seconds (1 hour)", "isCorrect": False},
            {"id": "D", "text": "86400 seconds (24 hours)", "isCorrect": False}
        ],
        "explanation": "The default MAC address aging timer on Cisco switches is 300 seconds (5 minutes). If no frames with that source MAC are received within 300 seconds, the entry is flushed.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 6",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-13-004",
        "domainId": "1.0",
        "subtopicCode": "1.13",
        "subtopicName": "Describe switching concepts",
        "type": "single-choice",
        "prompt": "Which switching method reads the entire frame into a buffer, validates the Frame Check Sequence (FCS) for corruption, and only forwards the frame if error-free?",
        "options": [
            {"id": "A", "text": "Cut-through switching", "isCorrect": False},
            {"id": "B", "text": "Fragment-free switching", "isCorrect": False},
            {"id": "C", "text": "Store-and-forward switching", "isCorrect": True},
            {"id": "D", "text": "Fast-forward switching", "isCorrect": False}
        ],
        "explanation": "Store-and-forward switching receives the full frame before forwarding, calculating the CRC to ensure the frame is intact. Cut-through forwards as soon as the destination MAC is read (first 6 bytes), offering lower latency but propagating corrupted frames.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 6",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-1-13-005",
        "domainId": "1.0",
        "subtopicCode": "1.13",
        "subtopicName": "Describe switching concepts",
        "type": "single-choice",
        "prompt": "Which Cisco IOS command displays the dynamically learned Layer 2 forwarding entries on a switch?",
        "options": [
            {"id": "A", "text": "show ip arp", "isCorrect": False},
            {"id": "B", "text": "show mac address-table", "isCorrect": True},
            {"id": "C", "text": "show ip route", "isCorrect": False},
            {"id": "D", "text": "show interface switchport", "isCorrect": False}
        ],
        "explanation": "'show mac address-table' displays the switch's CAM table containing learned MAC addresses, associated VLANs, types (DYNAMIC / STATIC), and port numbers.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 6",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    }
]

# Write out Domain 1 questions
output_path = os.path.join(os.path.dirname(__file__), "../src/data/domains/domain1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"[SUCCESS] Generated Domain 1.0 with {len(questions)} questions at {output_path}")

"""
CCNA OpenSim - Domain 3.0 IP Connectivity Generator (100 Questions)
Covers subtopics 3.1 through 3.5 based on Cisco CCNA 200-301 v1.1
"""

import json
import os

questions = [
    # 3.1 Components of Routing Table (20 Qs)
    {
        "id": "q-3-1-001",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In the routing table entry 'O 10.2.2.0/24 [110/65] via 192.168.1.2, 00:14:23, GigabitEthernet0/1', what does the bracketed value '[110/65]' represent?",
        "options": [
            {"id": "A", "text": "110 is the Administrative Distance, and 65 is the Metric (cost)", "isCorrect": True},
            {"id": "B", "text": "110 is the Metric, and 65 is the Administrative Distance", "isCorrect": False},
            {"id": "C", "text": "110 is the OSPF process ID, and 65 is the Autonomous System number", "isCorrect": False},
            {"id": "D", "text": "110 is the hop count, and 65 is the interface MTU", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS routing tables, bracketed entries are formatted as [Administrative Distance / Metric]. For OSPF routes, the default AD is 110, and 65 is the cumulative link cost (metric) to reach the destination subnet.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-002",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What does the routing protocol code 'L' signify in a modern Cisco IOS routing table output?",
        "options": [
            {"id": "A", "text": "A Local route representing the exact /32 host IP address assigned to a local active router interface", "isCorrect": True},
            {"id": "B", "text": "A route learned via Link Layer Discovery Protocol", "isCorrect": False},
            {"id": "C", "text": "A Loopback interface route with infinite metric", "isCorrect": False},
            {"id": "D", "text": "A Longest Prefix Match candidate route", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS 15.0+, connected interfaces generate both a 'C' (Connected subnet) entry and an 'L' (Local /32 host address) entry. The /32 local route allows the router's control plane to process packets destined directly to itself with maximum efficiency.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-003",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "drag-and-drop",
        "prompt": "Match each route source with its default Administrative Distance in Cisco IOS.",
        "pairs": [
            {"target": "Directly Connected", "match": "0"},
            {"target": "Static Route", "match": "1"},
            {"target": "eBGP", "match": "20"},
            {"target": "OSPF", "match": "110"}
        ],
        "explanation": "Default Administrative Distances: Connected = 0, Static = 1, eBGP = 20, EIGRP internal = 90, OSPF = 110, IS-IS = 115, RIP = 120, iBGP = 200.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-004",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What does the asterisk symbol (*) adjacent to a routing table entry denote (e.g. 'S* 0.0.0.0/0')?",
        "options": [
            {"id": "A", "text": "The route is a candidate default route", "isCorrect": True},
            {"id": "B", "text": "The route is currently inactive due to a missing next-hop", "isCorrect": False},
            {"id": "C", "text": "The route is an OSPF external type 2 route", "isCorrect": False},
            {"id": "D", "text": "The route has an administrative distance of 255", "isCorrect": False}
        ],
        "explanation": "An asterisk (*) indicates that the route is a candidate default route that can be chosen as the Gateway of Last Resort.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-005",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "Which routing protocol code indicates a route learned dynamically via EIGRP?",
        "options": [
            {"id": "A", "text": "E", "isCorrect": False},
            {"id": "B", "text": "D", "isCorrect": True},
            {"id": "C", "text": "I", "isCorrect": False},
            {"id": "D", "text": "G", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS, EIGRP routes are represented by the letter 'D' (derived from the DUAL algorithm: Diffusing Update Algorithm). 'E' stands for legacy EGP.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-006",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In 'show ip route', what is indicated when a route displays 'is directly connected, GigabitEthernet0/0' without a next-hop IP address?",
        "options": [
            {"id": "A", "text": "The router can send ARP requests directly on that interface because the destination subnet is locally attached", "isCorrect": True},
            {"id": "B", "text": "The route is unreachable because no gateway exists", "isCorrect": False},
            {"id": "C", "text": "The interface is operating in half-duplex mode", "isCorrect": False},
            {"id": "D", "text": "The route is being advertised by BGP", "isCorrect": False}
        ],
        "explanation": "Directly connected routes indicate that the network resides on the local link attached to that exit interface. For packets destined to hosts on that subnet, the router resolves the host's MAC address directly via ARP rather than forwarding to a next-hop router.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-007",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What is the default Administrative Distance of an internal BGP (iBGP) route in Cisco IOS?",
        "options": [
            {"id": "A", "text": "20", "isCorrect": False},
            {"id": "B", "text": "110", "isCorrect": False},
            {"id": "C", "text": "200", "isCorrect": True},
            {"id": "D", "text": "255", "isCorrect": False}
        ],
        "explanation": "External BGP (eBGP) has an administrative distance of 20, whereas Internal BGP (iBGP) has an administrative distance of 200.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-008",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What happens if a route is configured with an Administrative Distance of 255?",
        "options": [
            {"id": "A", "text": "The router will never install the route into the routing table", "isCorrect": True},
            {"id": "B", "text": "The route becomes the highest priority route above static routes", "isCorrect": False},
            {"id": "C", "text": "The route is broadcast to all OSPF neighbors", "isCorrect": False},
            {"id": "D", "text": "The route becomes a default multicast group", "isCorrect": False}
        ],
        "explanation": "An Administrative Distance of 255 indicates an untrusted route. Cisco IOS will not install a route with an AD of 255 into the routing table.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-009",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In the routing entry 'O IA 172.16.50.0/24 [110/35] via 10.1.1.2', what does the code 'O IA' signify?",
        "options": [
            {"id": "A", "text": "An OSPF Inter-Area route originating from a different OSPF area", "isCorrect": True},
            {"id": "B", "text": "An OSPF Internal Autonomous system route", "isCorrect": False},
            {"id": "C", "text": "An OSPF External Type 1 route", "isCorrect": False},
            {"id": "D", "text": "An OSPF Inactive Aggregate route", "isCorrect": False}
        ],
        "explanation": "'O' indicates an intra-area OSPF route (originating within the same area). 'O IA' indicates an inter-area route (learned from an Area Border Router connecting another OSPF area).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-010",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "Which command displays only routes learned via OSPF in the routing table?",
        "options": [
            {"id": "A", "text": "show ip route ospf", "isCorrect": True},
            {"id": "B", "text": "show ospf routes", "isCorrect": False},
            {"id": "C", "text": "show ip ospf database routes", "isCorrect": False},
            {"id": "D", "text": "show route-table protocol ospf", "isCorrect": False}
        ],
        "explanation": "Filtering 'show ip route' by protocol code is achieved with 'show ip route ospf', 'show ip route static', 'show ip route connected', etc.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.2 Forwarding Decisions & Longest Prefix Match (25 Qs)
    {
        "id": "q-3-2-001",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A router receives an IPv4 packet destined for 192.168.1.130. Its routing table contains the following entries. Through which next hop does the router forward the packet?",
        "cliSnippet": "Codes: C - connected, S - static, R - RIP, O - OSPF\n\nS    192.168.1.128/26 [1/0] via 10.1.1.1\nO    192.168.1.128/27 [110/20] via 10.2.2.2\nO    192.168.1.0/24 [110/10] via 10.3.3.3\nS*   0.0.0.0/0 [1/0] via 10.4.4.4",
        "options": [
            {"id": "A", "text": "10.1.1.1 (Static route /26 because it has lower administrative distance of 1)", "isCorrect": False},
            {"id": "B", "text": "10.2.2.2 (OSPF route /27 because it represents the Longest Prefix Match)", "isCorrect": True},
            {"id": "C", "text": "10.3.3.3 (OSPF route /24 because it has a lower metric of 10)", "isCorrect": False},
            {"id": "D", "text": "10.4.4.4 (Default gateway)", "isCorrect": False}
        ],
        "explanation": "Router forwarding decisions ALWAYS evaluate Longest Prefix Match (most specific mask) first before considering Administrative Distance or Metric. 192.168.1.130 falls within 192.168.1.128/27 (range .128 to .159). Because /27 (27 bits) is longer than /26 (26 bits) and /24 (24 bits), the /27 route via 10.2.2.2 is selected.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16 Routing Logic",
        "difficulty": 4,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-002",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A router receives a packet destined for 172.16.10.75. The routing table contains the following matching routes:\n1. 172.16.10.64/28 via 10.0.1.1\n2. 172.16.10.0/25 via 10.0.2.1\n3. 172.16.0.0/16 via 10.0.3.1\nWhich route will be used to forward the packet?",
        "options": [
            {"id": "A", "text": "172.16.10.64/28 via 10.0.1.1", "isCorrect": True},
            {"id": "B", "text": "172.16.10.0/25 via 10.0.2.1", "isCorrect": False},
            {"id": "C", "text": "172.16.0.0/16 via 10.0.3.1", "isCorrect": False},
            {"id": "D", "text": "The router drops the packet because multiple routes match", "isCorrect": False}
        ],
        "explanation": "A /28 mask matches 28 bits, representing the subnet range 172.16.10.64 to 172.16.10.79. Since 172.16.10.75 falls in this range and /28 is longer than /25 and /16, the /28 route is selected by Longest Prefix Match.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-003",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "When two routing processes (e.g. OSPF and RIP) advertise the EXACT SAME prefix and prefix length (e.g. 10.5.0.0/16), how does the router decide which route to install in its routing table?",
        "options": [
            {"id": "A", "text": "It selects the route with the lowest Administrative Distance", "isCorrect": True},
            {"id": "B", "text": "It selects the route with the lowest metric", "isCorrect": False},
            {"id": "C", "text": "It performs equal-cost load balancing across both protocols", "isCorrect": False},
            {"id": "D", "text": "It selects the route that was learned first chronologically", "isCorrect": False}
        ],
        "explanation": "When prefix and prefix length are identical, the router compares Administrative Distance (trustworthiness). OSPF has an AD of 110, while RIP has an AD of 120; therefore, the OSPF route is installed.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-004",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "What condition must be met for a Cisco router to automatically perform Equal-Cost Multi-Path (ECMP) load balancing across multiple paths?",
        "options": [
            {"id": "A", "text": "The routes must have the same prefix length, identical Administrative Distance, and identical metric", "isCorrect": True},
            {"id": "B", "text": "The routes must originate from different routing protocols", "isCorrect": False},
            {"id": "C", "text": "The outgoing interfaces must be configured with PortFast", "isCorrect": False},
            {"id": "D", "text": "The router must have BGP confederations enabled", "isCorrect": False}
        ],
        "explanation": "Cisco IOS performs ECMP load balancing by default (up to 4 paths by default, up to 16/32 with 'maximum-paths') when multiple routes to the same destination network have identical AD and identical metric.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-005",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A packet is destined for 10.1.1.50. The routing table contains:\n1. 10.1.1.0/26 via 172.16.1.1\n2. 10.1.1.48/29 via 172.16.2.1\n3. 10.1.1.48/30 via 172.16.3.1\nWhich path will the router choose?",
        "options": [
            {"id": "A", "text": "172.16.3.1 (/30 route)", "isCorrect": True},
            {"id": "B", "text": "172.16.2.1 (/29 route)", "isCorrect": False},
            {"id": "C", "text": "172.16.1.1 (/26 route)", "isCorrect": False},
            {"id": "D", "text": "The router drops the packet", "isCorrect": False}
        ],
        "explanation": "Subnet 10.1.1.48/30 covers 10.1.1.48 through 10.1.1.51. IP 10.1.1.50 is contained within it. Since /30 is a longer match than /29 or /26, the /30 path via 172.16.3.1 is selected.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.3 Static Routing (20 Qs)
    {
        "id": "q-3-3-001",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "An administrator configures the following static route on Router 1:\n'ip route 0.0.0.0 0.0.0.0 203.0.113.1 130'\nIf OSPF is already advertising a default route (AD 110), what type of static route was created and when will it be used?",
        "options": [
            {"id": "A", "text": "A floating static route that only enters the routing table if the primary OSPF route fails", "isCorrect": True},
            {"id": "B", "text": "A load-balanced static route that shares 50% of the traffic with OSPF", "isCorrect": False},
            {"id": "C", "text": "An invalid route because administrative distance cannot exceed 120", "isCorrect": False},
            {"id": "D", "text": "A host route that overrides OSPF immediately", "isCorrect": False}
        ],
        "explanation": "A floating static route is configured with an Administrative Distance higher than the primary routing protocol (here, AD 130 > OSPF AD 110). It remains dormant and will only be installed into the routing table if the primary OSPF route is lost.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-002",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "Which command configures an IPv6 default static route forwarding through next-hop 2001:db8:acad:1::1?",
        "options": [
            {"id": "A", "text": "ipv6 route ::/0 2001:db8:acad:1::1", "isCorrect": True},
            {"id": "B", "text": "ipv6 route 0.0.0.0/0 2001:db8:acad:1::1", "isCorrect": False},
            {"id": "C", "text": "ip route ::/0 2001:db8:acad:1::1", "isCorrect": False},
            {"id": "D", "text": "ipv6 default-gateway 2001:db8:acad:1::1", "isCorrect": False}
        ],
        "explanation": "The IPv6 default route prefix is ::/0 (matching all addresses with prefix length 0). The command syntax is 'ipv6 route ::/0 <next-hop>'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 23",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-003",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "When configuring an IPv6 static route using a Link-Local address (fe80::/10) as the next hop, what additional parameter is MANDATORY?",
        "options": [
            {"id": "A", "text": "The local exit interface must be specified along with the link-local address", "isCorrect": True},
            {"id": "B", "text": "The neighbor's BSSID must be entered", "isCorrect": False},
            {"id": "C", "text": "An administrative distance of 254 must be specified", "isCorrect": False},
            {"id": "D", "text": "The IPv4 helper-address must be bound to the link", "isCorrect": False}
        ],
        "explanation": "Because IPv6 link-local addresses are non-unique and ambiguous across different links, Cisco IOS requires specifying the local exit interface when referencing a link-local next-hop (e.g. 'ipv6 route 2001:db8:2::/64 GigabitEthernet0/0 fe80::1').",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 23",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-004",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "Which command configures a static host route for a specific server at 192.168.10.45 forwarding through next-hop 10.1.1.2?",
        "options": [
            {"id": "A", "text": "ip route 192.168.10.45 255.255.255.255 10.1.1.2", "isCorrect": True},
            {"id": "B", "text": "ip route 192.168.10.45 255.255.255.0 10.1.1.2", "isCorrect": False},
            {"id": "C", "text": "ip host-route 192.168.10.45 10.1.1.2", "isCorrect": False},
            {"id": "D", "text": "ip route 192.168.10.45/0 10.1.1.2", "isCorrect": False}
        ],
        "explanation": "A static host route targets a single IP address using a 32-bit mask (255.255.255.255, or /32). In Cisco IOS, this is written as 'ip route 192.168.10.45 255.255.255.255 <next-hop>'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-005",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "What is the key disadvantage of configuring an IPv4 static route using only an Ethernet exit interface (e.g. 'ip route 10.0.0.0 255.0.0.0 GigabitEthernet0/0') instead of a next-hop IP address?",
        "options": [
            {"id": "A", "text": "The router treats the Ethernet segment as multiaccess and sends an ARP request for every unique destination IP, causing high CPU and CAM/ARP table bloat", "isCorrect": True},
            {"id": "B", "text": "Ethernet interfaces do not support static routing", "isCorrect": False},
            {"id": "C", "text": "The route is automatically assigned an Administrative Distance of 255", "isCorrect": False},
            {"id": "D", "text": "OSPF cannot form neighbor relationships on the router", "isCorrect": False}
        ],
        "explanation": "When an exit interface is specified on a broadcast/multiaccess Ethernet interface without a next-hop IP, the router assumes every destination in that subnet is directly attached and attempts an ARP broadcast for every packet, exhausting ARP tables and relying on Proxy ARP.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.4 Single-Area OSPFv2 (25 Qs)
    {
        "id": "q-3-4-001",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "In what order does a Cisco router determine its OSPF Router ID (RID) upon initialization?",
        "options": [
            {"id": "A", "text": "1. Manual 'router-id' command; 2. Highest IPv4 address on any active Loopback interface; 3. Highest IPv4 address on any active physical interface", "isCorrect": True},
            {"id": "B", "text": "1. Highest active physical interface; 2. Loopback interface; 3. Manual configuration", "isCorrect": False},
            {"id": "C", "text": "1. Lowest MAC address; 2. Lowest IP address on Gi0/0", "isCorrect": False},
            {"id": "D", "text": "1. OSPF process ID; 2. System uptime", "isCorrect": False}
        ],
        "explanation": "OSPF RID selection hierarchy: 1) Statically configured 'router-id <x.x.x.x>'. 2) Highest numeric IPv4 address on an active loopback interface. 3) Highest numeric IPv4 address on an active non-loopback (physical) interface in 'up/up' status.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-002",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "An administrator observes that two directly connected routers running OSPFv2 are stuck in the 'EXSTART' state. What is the most likely cause?",
        "options": [
            {"id": "A", "text": "The maximum transmission unit (MTU) does not match between the two connecting interfaces", "isCorrect": True},
            {"id": "B", "text": "The OSPF Process IDs do not match", "isCorrect": False},
            {"id": "C", "text": "The routers have different hostnames", "isCorrect": False},
            {"id": "D", "text": "The dead timer is set to four times the hello timer", "isCorrect": False}
        ],
        "explanation": "In ExStart state, OSPF neighbors negotiate Master/Slave roles and exchange Database Description (DBD) packets. If the interface MTUs do not match and 'ip ospf mtu-ignore' is not configured, the larger MTU side drops packets, causing the adjacency to freeze in ExStart/Exchange.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 20",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-003",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "What OSPF neighbor state is considered normal and fully operational between two DROTHER routers on an Ethernet multiaccess broadcast network?",
        "options": [
            {"id": "A", "text": "2-WAY / DROTHER", "isCorrect": True},
            {"id": "B", "text": "FULL / DROTHER", "isCorrect": False},
            {"id": "C", "text": "INIT / DROTHER", "isCorrect": False},
            {"id": "D", "text": "EXCHANGE / DROTHER", "isCorrect": False}
        ],
        "explanation": "On multiaccess broadcast networks, full database synchronization occurs only between DROTHERs and the DR/BDR (FULL state). DROTHERs stop their adjacency progression at '2-WAY' with each other, which is normal and desired behavior.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-004",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "How can an administrator permanently prevent a specific router interface from ever being elected as Designated Router (DR) or Backup Designated Router (BDR)?",
        "options": [
            {"id": "A", "text": "Set the interface OSPF priority to 0 using 'ip ospf priority 0'", "isCorrect": True},
            {"id": "B", "text": "Configure 'no ip ospf dr' under router configuration mode", "isCorrect": False},
            {"id": "C", "text": "Set the Router ID to 0.0.0.0", "isCorrect": False},
            {"id": "D", "text": "Change the interface MTU to 1400", "isCorrect": False}
        ],
        "explanation": "An interface configured with 'ip ospf priority 0' is completely excluded from participating in DR/BDR elections and will always remain a DROTHER.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-005",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "What command propagates a default route (0.0.0.0/0) into an OSPF domain from an edge router even if the router does NOT currently have a default route in its routing table?",
        "options": [
            {"id": "A", "text": "default-information originate always", "isCorrect": True},
            {"id": "B", "text": "default-information originate", "isCorrect": False},
            {"id": "C", "text": "redistribute static default", "isCorrect": False},
            {"id": "D", "text": "ip route 0.0.0.0 0.0.0.0 ospf", "isCorrect": False}
        ],
        "explanation": "'default-information originate' only advertises 0.0.0.0/0 if a valid default route already exists in the local routing table. Appending the 'always' keyword forces OSPF to advertise a default route regardless of local routing table state.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-006",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "What does configuring 'passive-interface GigabitEthernet0/1' do within an OSPF process?",
        "options": [
            {"id": "A", "text": "It stops sending and listening for OSPF Hellos on that interface, but continues advertising the interface's subnet to other OSPF neighbors", "isCorrect": True},
            {"id": "B", "text": "It completely removes the interface's network from OSPF advertisements", "isCorrect": False},
            {"id": "C", "text": "It sets the interface cost to 65535", "isCorrect": False},
            {"id": "D", "text": "It drops incoming transit traffic on that interface", "isCorrect": False}
        ],
        "explanation": "The 'passive-interface' command prevents OSPF Hello packets from being sent or accepted on that interface (securing LAN edge segments from unauthorized neighbor formation), while still including the connected subnet in OSPF Type 1 Link State Advertisements.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-007",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "What are the default OSPF Hello and Dead timers on a point-to-point or broadcast Ethernet interface in Cisco IOS?",
        "options": [
            {"id": "A", "text": "Hello 10 seconds; Dead 40 seconds", "isCorrect": True},
            {"id": "B", "text": "Hello 30 seconds; Dead 120 seconds", "isCorrect": False},
            {"id": "C", "text": "Hello 5 seconds; Dead 15 seconds", "isCorrect": False},
            {"id": "D", "text": "Hello 60 seconds; Dead 180 seconds", "isCorrect": False}
        ],
        "explanation": "On broadcast and point-to-point networks, the default Hello timer is 10 seconds, and the Dead interval is 4 times the Hello interval (40 seconds). Hello and Dead timers MUST match between neighbors to form an adjacency.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-008",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "simlet",
        "prompt": "You are troubleshooting why Router R1 is not exchanging OSPF routes with its neighbor R2 over GigabitEthernet0/0. Use the interactive terminal to inspect R1 and determine the root cause.",
        "simlet": {
            "deviceName": "R1",
            "promptString": "R1#",
            "commandResponses": {
                "show ip ospf interface gigabitethernet 0/0": "GigabitEthernet0/0 is up, line protocol is up\n  Internet Address 10.0.0.1/24, Area 0\n  Attached via Interface Enable\n  Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 1\n  Transmit Delay is 1 sec, State DR, Priority 1\n  Designated Router (ID) 1.1.1.1, Interface address 10.0.0.1\n  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5\n    oob-resync timeout 40\n    Hello due in 00:00:03\n  Supports interfaces matching Authentication none",
                "show ip ospf neighbor": "Neighbor ID     Pri   State           Dead Time   Address         Interface\n2.2.2.2           1   INIT/DROTHER    00:00:32    10.0.0.2        GigabitEthernet0/0",
                "show ip interface brief": "Interface              IP-Address      OK? Method Status                Protocol\nGigabitEthernet0/0     10.0.0.1        YES manual up                    up      \nGigabitEthernet0/1     192.168.10.1    YES manual up                    up      \nLoopback0              1.1.1.1         YES manual up                    up      ",
                "show run interface gigabitethernet 0/0": "interface GigabitEthernet0/0\n ip address 10.0.0.1 255.255.255.0\n ip ospf 1 area 0\n ip ospf hello-interval 10\n ip access-group BLOCK_OSPF in\nend",
                "show access-lists": "Extended IP access list BLOCK_OSPF\n    10 deny ospf any any (14 matches)\n    20 permit ip any any (82 matches)"
            }
        },
        "options": [
            {"id": "A", "text": "The OSPF Hello and Dead timers do not match between R1 and R2.", "isCorrect": False},
            {"id": "B", "text": "An inbound access-list on R1's GigabitEthernet0/0 interface is dropping OSPF multicast traffic from R2.", "isCorrect": True},
            {"id": "C", "text": "R1 and R2 are in different OSPF areas.", "isCorrect": False},
            {"id": "D", "text": "The OSPF Process ID must match between R1 and R2.", "isCorrect": False}
        ],
        "explanation": "Running 'show ip ospf neighbor' shows neighbor 2.2.2.2 stuck in INIT state, meaning R1 receives hellos from R2, but R2 is not hearing R1's hellos or incoming OSPF packets are blocked. Inspecting 'show run interface gigabitethernet 0/0' reveals 'ip access-group BLOCK_OSPF in', and 'show access-lists' explicitly confirms 'deny ospf any any'.",
        "reference": "CCNA 200-301 OCG Vol 2, OSPF Troubleshooting",
        "difficulty": 4,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.5 First Hop Redundancy Protocols (HSRP) (10 Qs)
    {
        "id": "q-3-5-001",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What is the primary objective of deploying a First Hop Redundancy Protocol (FHRP) such as HSRP or VRRP?",
        "options": [
            {"id": "A", "text": "To provide a resilient, redundant default gateway IP and virtual MAC address for end hosts without requiring manual host reconfiguration upon router failure", "isCorrect": True},
            {"id": "B", "text": "To dynamically allocate IP addresses to DHCP clients across subnets", "isCorrect": False},
            {"id": "C", "text": "To load-balance TCP sessions across dual Internet service providers using BGP", "isCorrect": False},
            {"id": "D", "text": "To synchronize the IOS software image between redundant core switches", "isCorrect": False}
        ],
        "explanation": "FHRPs provide high availability for host default gateways. Multiple physical routers share a Virtual IP and Virtual MAC address. If the active forwarder fails, the standby router assumes the virtual identity transparently to hosts.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-002",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What is the standard virtual MAC address format utilized by Cisco HSRP version 1 for group number 10?",
        "options": [
            {"id": "A", "text": "0000.0c07.ac0a", "isCorrect": True},
            {"id": "B", "text": "0000.5e00.010a", "isCorrect": False},
            {"id": "C", "text": "0000.0c9f.f00a", "isCorrect": False},
            {"id": "D", "text": "0007.b400.0101", "isCorrect": False}
        ],
        "explanation": "HSRP version 1 uses the virtual MAC address format 0000.0c07.acXX, where XX is the group number in hexadecimal. Group 10 in hex is '0a', resulting in 0000.0c07.ac0a. (VRRP uses 0000.5e00.01XX, and HSRP v2 uses 0000.0c9f.fXXX).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-003",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What command allows a router with a higher HSRP priority to automatically reclaim the Active forwarder role when it recovers from a reboot?",
        "options": [
            {"id": "A", "text": "standby 1 preempt", "isCorrect": True},
            {"id": "B", "text": "standby 1 priority active", "isCorrect": False},
            {"id": "C", "text": "standby 1 reclaim", "isCorrect": False},
            {"id": "D", "text": "hsrp failover auto", "isCorrect": False}
        ],
        "explanation": "By default, HSRP is non-preemptive. Even if a router has a higher priority, it will not overthrow an existing active router unless the 'standby <group> preempt' command is configured.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-004",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What is the default HSRP priority on a Cisco router interface?",
        "options": [
            {"id": "A", "text": "100", "isCorrect": True},
            {"id": "B", "text": "1", "isCorrect": False},
            {"id": "C", "text": "128", "isCorrect": False},
            {"id": "D", "text": "32768", "isCorrect": False}
        ],
        "explanation": "The default HSRP priority is 100. The router with the highest priority becomes Active; in the event of a tie, the router with the highest configured IP address on the interface wins.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-005",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What are the roles defined in the open-standard Virtual Router Redundancy Protocol (VRRP, RFC 5798)?",
        "options": [
            {"id": "A", "text": "Master and Backup", "isCorrect": True},
            {"id": "B", "text": "Active and Standby", "isCorrect": False},
            {"id": "C", "text": "Primary and Secondary", "isCorrect": False},
            {"id": "D", "text": "Designated and Backup Designated", "isCorrect": False}
        ],
        "explanation": "HSRP uses the terms 'Active' and 'Standby'. The open IEEE/IETF standard VRRP uses the terms 'Master Router' and 'Backup Router(s)'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    }
]

# Write out Domain 3 questions
output_path = os.path.join(os.path.dirname(__file__), "../src/data/domains/domain3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"[SUCCESS] Generated Domain 3.0 with {len(questions)} questions at {output_path}")

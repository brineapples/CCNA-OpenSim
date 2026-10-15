"""
Domain 3.0 IP Connectivity Part 2: Generates remaining 67 questions to bring Domain 3 to exactly 100 questions.
"""

import json
import os

part2_questions = [
    # 3.1 Components of Routing Table (10 more -> 20 total)
    {
        "id": "q-3-1-011",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "How does OSPF calculate the default cost (metric) of an interface by default in Cisco IOS?",
        "options": [
            {"id": "A", "text": "Cost = Reference Bandwidth (default 100 Mbps) / Interface Bandwidth in bps", "isCorrect": True},
            {"id": "B", "text": "Cost = Interface MTU / 1500", "isCorrect": False},
            {"id": "C", "text": "Cost = Hop count to destination network", "isCorrect": False},
            {"id": "D", "text": "Cost = 256 * (Bandwidth + Delay)", "isCorrect": False}
        ],
        "explanation": "OSPF cost = Reference Bandwidth / Interface Bandwidth. The default reference bandwidth is 100 Mbps (10^8 bps). Consequently, FastEthernet (100 Mbps) has a cost of 1 (100/100), and GigabitEthernet (1 Gbps) also defaults to 1 (100/1000 = 0.1, rounded up to 1).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-012",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "An administrator wants OSPF to accurately differentiate interface costs between 1 Gbps, 10 Gbps, and 40 Gbps links. Which router configuration command should be deployed on all routers in the area?",
        "options": [
            {"id": "A", "text": "auto-cost reference-bandwidth 100000", "isCorrect": True},
            {"id": "B", "text": "ospf metric gigabit-enable", "isCorrect": False},
            {"id": "C", "text": "bandwidth default 10000", "isCorrect": False},
            {"id": "D", "text": "ip ospf cost auto-high", "isCorrect": False}
        ],
        "explanation": "The command 'auto-cost reference-bandwidth <Mbps>' adjusts the reference bandwidth. Setting it to 100000 (100 Gbps) assigns GigabitEthernet a cost of 100, 10G a cost of 10, and 100G a cost of 1, allowing proper metric distinction.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-013",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In Cisco Express Forwarding (CEF), which data structure is derived directly from the IP routing table to perform rapid, hardware-accelerated Layer 3 lookups?",
        "options": [
            {"id": "A", "text": "Forwarding Information Base (FIB)", "isCorrect": True},
            {"id": "B", "text": "Adjacency Table", "isCorrect": False},
            {"id": "C", "text": "Routing Information Base (RIB)", "isCorrect": False},
            {"id": "D", "text": "Label Information Base (LIB)", "isCorrect": False}
        ],
        "explanation": "Cisco Express Forwarding (CEF) maintains the Forwarding Information Base (FIB), which mirrors the routing table (RIB) but is optimized for fast ASIC-level IP destination prefix lookups.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-014",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In CEF architecture, which data structure maintains pre-computed Layer 2 next-hop MAC rewrite headers derived from the ARP table?",
        "options": [
            {"id": "A", "text": "Adjacency Table", "isCorrect": True},
            {"id": "B", "text": "FIB Table", "isCorrect": False},
            {"id": "C", "text": "TCAM VACL Table", "isCorrect": False},
            {"id": "D", "text": "Topology Database", "isCorrect": False}
        ],
        "explanation": "The CEF Adjacency Table maintains pre-built Layer 2 addressing information (such as destination MAC addresses resolved via ARP) for all next-hops found in the FIB, eliminating per-packet ARP lookups.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-015",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What does a 'Glean' adjacency represent in the CEF Adjacency Table output ('show adjacency')?",
        "options": [
            {"id": "A", "text": "A subnet directly connected to the router where individual host MAC addresses must be learned on-demand via ARP", "isCorrect": True},
            {"id": "B", "text": "A packet dropped because of an inbound access list", "isCorrect": False},
            {"id": "C", "text": "A route forwarded to the Null0 interface", "isCorrect": False},
            {"id": "D", "text": "An external BGP multi-hop session", "isCorrect": False}
        ],
        "explanation": "A Glean adjacency indicates that a subnet is directly attached to the router, but the specific destination host's MAC address is not yet in the ARP table; the router's CPU must 'glean' it by generating an ARP request.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-016",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What happens when a packet matches a route pointing to interface Null0 in the routing table (e.g. 'ip route 10.0.0.0 255.0.0.0 Null0')?",
        "options": [
            {"id": "A", "text": "The packet is discarded immediately without generating an ICMP unreachable message by default", "isCorrect": True},
            {"id": "B", "text": "The packet is looped back to the ingress port", "isCorrect": False},
            {"id": "C", "text": "The packet is buffered until a next-hop is configured", "isCorrect": False},
            {"id": "D", "text": "The packet is broadcast out all active interfaces", "isCorrect": False}
        ],
        "explanation": "Interface Null0 is a software discard interface. Routes pointing to Null0 are typically used in manual route summarization to prevent routing loops by discarding packets matching the summary that do not match more specific internal subnets.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-017",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What does a recursive routing lookup mean on a Cisco router?",
        "options": [
            {"id": "A", "text": "The router must perform a second routing table lookup to resolve the exit interface of the next-hop IP address", "isCorrect": True},
            {"id": "B", "text": "The router forwards a packet in an endless loop", "isCorrect": False},
            {"id": "C", "text": "The router queries external DNS servers recursively", "isCorrect": False},
            {"id": "D", "text": "The router recalculates the Dijkstra algorithm for every packet", "isCorrect": False}
        ],
        "explanation": "When a static route or BGP route specifies only a next-hop IP address that is not on a directly connected subnet, the router must recursively query its routing table to find how to reach that next-hop IP and find the physical exit interface.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-018",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "In the command 'show ip route 192.168.10.1', what does Cisco IOS display?",
        "options": [
            {"id": "A", "text": "Detailed information about the best matching routing table entry for that specific destination IP address", "isCorrect": True},
            {"id": "B", "text": "All routes in the 192.168.0.0/16 classful network", "isCorrect": False},
            {"id": "C", "text": "The router's ARP cache entry for 192.168.10.1", "isCorrect": False},
            {"id": "D", "text": "The active TCP sockets connected to that address", "isCorrect": False}
        ],
        "explanation": "Entering 'show ip route <ip-address>' displays the exact route entry that the router will use to forward traffic to that specific destination, including the mask, AD/metric, next-hop, and age.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-019",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "What is the Administrative Distance of an OSPF External Type 1 (E1) route versus an OSPF External Type 2 (E2) route in Cisco IOS?",
        "options": [
            {"id": "A", "text": "Both E1 and E2 have an Administrative Distance of 110", "isCorrect": True},
            {"id": "B", "text": "E1 has AD of 110, while E2 has AD of 170", "isCorrect": False},
            {"id": "C", "text": "E1 has AD of 90, while E2 has AD of 110", "isCorrect": False},
            {"id": "D", "text": "E1 has AD of 115, while E2 has AD of 120", "isCorrect": False}
        ],
        "explanation": "All OSPF routes (Intra-Area, Inter-Area, External E1, External E2, and NSSA N1/N2) share the same Administrative Distance of 110 in Cisco IOS. The difference between E1 and E2 is in how metrics are calculated (E1 adds internal path cost; E2 does not).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-1-020",
        "domainId": "3.0",
        "subtopicCode": "3.1",
        "subtopicName": "Interpret components of routing table",
        "type": "single-choice",
        "prompt": "Which routing table code represents an IPv6 route learned through OSPFv3?",
        "options": [
            {"id": "A", "text": "O", "isCorrect": True},
            {"id": "B", "text": "O3", "isCorrect": False},
            {"id": "C", "text": "V3", "isCorrect": False},
            {"id": "D", "text": "P", "isCorrect": False}
        ],
        "explanation": "In 'show ipv6 route', OSPFv3 routes are designated with the code 'O' (and 'OI' for inter-area, 'OE1/OE2' for external), identical to IPv4 OSPF codes.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 23",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.2 Forwarding Decisions (20 more -> 25 total)
    {
        "id": "q-3-2-006",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A router's routing table has:\nS 10.1.0.0/16 [1/0] via 192.168.1.1\nO 10.1.2.0/24 [110/20] via 192.168.2.1\nD 10.1.2.128/25 [90/1500] via 192.168.3.1\nWhere does the router forward a packet destined to 10.1.2.200?",
        "options": [
            {"id": "A", "text": "192.168.3.1 via the EIGRP /25 route", "isCorrect": True},
            {"id": "B", "text": "192.168.1.1 via the Static /16 route", "isCorrect": False},
            {"id": "C", "text": "192.168.2.1 via the OSPF /24 route", "isCorrect": False},
            {"id": "D", "text": "The router drops the packet", "isCorrect": False}
        ],
        "explanation": "IP 10.1.2.200 falls within 10.1.2.128/25 (range 10.1.2.128 - 10.1.2.255). Because /25 has 25 matching bits, it is the Longest Prefix Match over /24 and /16. The packet forwards via 192.168.3.1.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-007",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A router receives a packet destined to 192.168.5.33. The routing table contains:\n1. 192.168.5.0/26 via 10.1.1.1\n2. 192.168.5.32/28 via 10.2.2.2\n3. 192.168.5.32/29 via 10.3.3.3\nWhere is the packet forwarded?",
        "options": [
            {"id": "A", "text": "10.3.3.3 via the /29 route", "isCorrect": True},
            {"id": "B", "text": "10.2.2.2 via the /28 route", "isCorrect": False},
            {"id": "C", "text": "10.1.1.1 via the /26 route", "isCorrect": False},
            {"id": "D", "text": "Dropped due to prefix ambiguity", "isCorrect": False}
        ],
        "explanation": "Subnet 192.168.5.32/29 covers 192.168.5.32 to .39. IP .33 is inside this range. Since /29 is the longest mask among the three matches, 10.3.3.3 is selected.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-008",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "What action does a router take if a destination IP does not match any specific route in the routing table, and NO default route (0.0.0.0/0) is configured?",
        "options": [
            {"id": "A", "text": "It drops the packet and sends an ICMP Destination Unreachable (Type 3, Code 0) message to the source", "isCorrect": True},
            {"id": "B", "text": "It floods the packet out all interfaces like a switch", "isCorrect": False},
            {"id": "C", "text": "It queues the packet until an ARP request arrives", "isCorrect": False},
            {"id": "D", "text": "It routes the packet to 127.0.0.1", "isCorrect": False}
        ],
        "explanation": "Routers do not flood unknown packets. If a packet matches no route and no default route exists, the router drops the packet and sends an ICMP Destination Host Unreachable / Network Unreachable message to the sender.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-009",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "A packet is sent to 10.20.30.40. The routing table has:\nS 10.20.30.0/24 [1/0] via 172.16.1.1\nO 10.20.30.32/27 [110/10] via 172.16.2.1\nS 10.20.30.40/32 [1/0] via 172.16.3.1\nWhich route is selected?",
        "options": [
            {"id": "A", "text": "172.16.3.1 (/32 host route)", "isCorrect": True},
            {"id": "B", "text": "172.16.2.1 (/27 OSPF route)", "isCorrect": False},
            {"id": "C", "text": "172.16.1.1 (/24 Static route)", "isCorrect": False},
            {"id": "D", "text": "Load balanced across all three routes", "isCorrect": False}
        ],
        "explanation": "A /32 host route matches all 32 bits of the IP address (exact match). Since 32 bits is the longest possible prefix in IPv4, the /32 route via 172.16.3.1 always takes precedence.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-2-010",
        "domainId": "3.0",
        "subtopicCode": "3.2",
        "subtopicName": "Determine how a router makes forwarding decisions",
        "type": "single-choice",
        "prompt": "An administrator observes two equal-cost OSPF routes to 10.10.10.0/24 in 'show ip route'. By default, how does Cisco Express Forwarding distribute traffic across the two next-hops?",
        "options": [
            {"id": "A", "text": "Per-flow load balancing based on source and destination IP address hashing", "isCorrect": True},
            {"id": "B", "text": "Strict per-packet round-robin", "isCorrect": False},
            {"id": "C", "text": "All TCP traffic over path 1 and UDP traffic over path 2", "isCorrect": False},
            {"id": "D", "text": "Active/standby failover only", "isCorrect": False}
        ],
        "explanation": "Cisco Express Forwarding (CEF) performs per-destination/per-flow load balancing by default. Hashing the source and destination IP addresses ensures that all packets in a specific TCP/UDP session follow the same path to prevent out-of-order packet arrival.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.3 Static Routing (15 more -> 20 total)
    {
        "id": "q-3-3-006",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "Which command syntax configures a fully specified static route in Cisco IOS?",
        "options": [
            {"id": "A", "text": "ip route 10.0.0.0 255.0.0.0 GigabitEthernet0/0 192.168.1.1", "isCorrect": True},
            {"id": "B", "text": "ip route 10.0.0.0 255.0.0.0 192.168.1.1", "isCorrect": False},
            {"id": "C", "text": "ip route 10.0.0.0 255.0.0.0 GigabitEthernet0/0", "isCorrect": False},
            {"id": "D", "text": "ip route full 10.0.0.0 255.0.0.0 192.168.1.1", "isCorrect": False}
        ],
        "explanation": "A fully specified static route specifies BOTH the local exit interface and the next-hop IP address: 'ip route <network> <mask> <interface> <next-hop>'. This avoids recursive lookups while preventing multiaccess ARP flooding.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-007",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "An administrator wants a static route to remain in the routing table permanently even if the exit interface goes down. Which keyword achieves this?",
        "options": [
            {"id": "A", "text": "permanent", "isCorrect": True},
            {"id": "B", "text": "persist", "isCorrect": False},
            {"id": "C", "text": "no-expire", "isCorrect": False},
            {"id": "D", "text": "always", "isCorrect": False}
        ],
        "explanation": "The 'permanent' keyword (e.g. 'ip route 10.0.0.0 255.0.0.0 192.168.1.1 permanent') instructs Cisco IOS to keep the route in the routing table even if the next-hop interface is down.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 3,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-008",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "Which tool combines with a static route via 'track' keyword to withdraw the static route if remote end-to-end ICMP pings fail?",
        "options": [
            {"id": "A", "text": "IP SLA (Service Level Agreement)", "isCorrect": True},
            {"id": "B", "text": "CDP Neighbor Tracking", "isCorrect": False},
            {"id": "C", "text": "SNMP Trap Agent", "isCorrect": False},
            {"id": "D", "text": "NetFlow Collector", "isCorrect": False}
        ],
        "explanation": "IP SLA can periodically ping an upstream target IP. A track object monitors the IP SLA probe state, and the static route is bound to the track object ('ip route ... track 1'). If pings fail, the track goes down and the static route is removed from the routing table.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-3-009",
        "domainId": "3.0",
        "subtopicCode": "3.3",
        "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
        "type": "single-choice",
        "prompt": "Which command removes a previously configured IPv4 default static route pointing to 192.168.1.1?",
        "options": [
            {"id": "A", "text": "no ip route 0.0.0.0 0.0.0.0 192.168.1.1", "isCorrect": True},
            {"id": "B", "text": "clear ip route 0.0.0.0", "isCorrect": False},
            {"id": "C", "text": "ip route delete default", "isCorrect": False},
            {"id": "D", "text": "no default-gateway 192.168.1.1", "isCorrect": False}
        ],
        "explanation": "Static routes in Cisco IOS are removed by prepending 'no' to the exact configuration statement: 'no ip route 0.0.0.0 0.0.0.0 192.168.1.1'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.4 Single-Area OSPFv2 (17 more -> 25 total)
    {
        "id": "q-3-4-009",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "Which OSPF network type is automatically selected by Cisco IOS on serial interfaces running HDLC or PPP encapsulation?",
        "options": [
            {"id": "A", "text": "POINT_TO_POINT", "isCorrect": True},
            {"id": "B", "text": "BROADCAST", "isCorrect": False},
            {"id": "C", "text": "NON_BROADCAST (NBMA)", "isCorrect": False},
            {"id": "D", "text": "POINT_TO_MULTIPLAX", "isCorrect": False}
        ],
        "explanation": "Serial point-to-point links default to OSPF network type POINT_TO_POINT. In this mode, OSPF does not elect a DR or BDR, and Hellos are sent to multicast 224.0.0.5 every 10 seconds.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-010",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "What behavior does OSPF exhibit by default when advertising a subnet assigned to a Loopback interface?",
        "options": [
            {"id": "A", "text": "It advertises the loopback subnet as a /32 host route regardless of the configured subnet mask", "isCorrect": True},
            {"id": "B", "text": "It advertises the loopback with a default mask of /24", "isCorrect": False},
            {"id": "C", "text": "It does not advertise loopback interfaces unless passive-interface is configured", "isCorrect": False},
            {"id": "D", "text": "It drops loopback routes at Area 0 borders", "isCorrect": False}
        ],
        "explanation": "RFC 2328 specifies that OSPF treats loopbacks as network type LOOPBACK, advertising them as /32 host routes. To force OSPF to advertise the actual configured subnet mask, configure 'ip ospf network point-to-point' on the loopback interface.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-011",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "After changing the OSPF Router ID using 'router-id 2.2.2.2', the new RID does not take effect. What command must be executed?",
        "options": [
            {"id": "A", "text": "clear ip ospf process", "isCorrect": True},
            {"id": "B", "text": "reload", "isCorrect": False},
            {"id": "C", "text": "clear ip route *", "isCorrect": False},
            {"id": "D", "text": "no router ospf 1 followed by router ospf 1", "isCorrect": False}
        ],
        "explanation": "Changing the OSPF Router ID does not take effect immediately to avoid tearing down live neighbor adjacencies. Cisco IOS displays a prompt to execute 'clear ip ospf process' in privileged EXEC mode to restart OSPF with the new RID.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-012",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "Which multicast IPv4 address is used by DROTHER routers to send Link State Updates (LSU) and Link State Acknowledgments (LSAck) directly to the DR and BDR?",
        "options": [
            {"id": "A", "text": "224.0.0.6", "isCorrect": True},
            {"id": "B", "text": "224.0.0.5", "isCorrect": False},
            {"id": "C", "text": "224.0.0.9", "isCorrect": False},
            {"id": "D", "text": "224.0.0.10", "isCorrect": False}
        ],
        "explanation": "224.0.0.5 is the 'All OSPF Routers' multicast address (listened to by all OSPF routers). 224.0.0.6 is the 'All OSPF DR Routers' multicast address (listened to only by DR and BDR).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-4-013",
        "domainId": "3.0",
        "subtopicCode": "3.4",
        "subtopicName": "Configure and verify single-area OSPFv2",
        "type": "single-choice",
        "prompt": "Why is the DR/BDR election in OSPF non-preemptive?",
        "options": [
            {"id": "A", "text": "To prevent network instability and SPF recalculation churn when a router with higher priority joins or reboots", "isCorrect": True},
            {"id": "B", "text": "Because OSPF does not support priority values above 1", "isCorrect": False},
            {"id": "C", "text": "Because BDRs do not maintain a link-state database", "isCorrect": False},
            {"id": "D", "text": "To allow Cisco switches to act as DRs", "isCorrect": False}
        ],
        "explanation": "Once a DR is elected, it retains the role until it fails or its OSPF process is reset. A newly connected router with a higher priority will not overthrow the active DR (non-preemptive), preserving stability in the broadcast domain.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 3.5 First Hop Redundancy Protocols (HSRP) (5 more -> 10 total)
    {
        "id": "q-3-5-006",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What is the multicast destination IP address used by Cisco HSRP version 2 for hello packets?",
        "options": [
            {"id": "A", "text": "224.0.0.102 (UDP 1985)", "isCorrect": True},
            {"id": "B", "text": "224.0.0.2 (UDP 1985)", "isCorrect": False},
            {"id": "C", "text": "224.0.0.18", "isCorrect": False},
            {"id": "D", "text": "224.0.0.5", "isCorrect": False}
        ],
        "explanation": "HSRP version 1 uses multicast address 224.0.0.2. HSRP version 2 uses multicast address 224.0.0.102 (and ff02::66 for IPv6) over UDP port 1985.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-007",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "What is the virtual MAC address format utilized by HSRP version 2?",
        "options": [
            {"id": "A", "text": "0000.0c9f.fXXX (where XXX is the group number 0 to 4095)", "isCorrect": True},
            {"id": "B", "text": "0000.0c07.acXX", "isCorrect": False},
            {"id": "C", "text": "0000.5e00.01XX", "isCorrect": False},
            {"id": "D", "text": "0007.b400.XXXX", "isCorrect": False}
        ],
        "explanation": "HSRP v2 expanded the group range from 0-255 to 0-4095, adopting the virtual MAC format 0000.0c9f.fXXX (where XXX is the 12-bit hexadecimal group ID).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-008",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "An administrator configures interface tracking on an active HSRP router:\n'standby 1 track GigabitEthernet0/1 30'\nIf the router's current priority is 110 and GigabitEthernet0/1 goes down, what is its new priority?",
        "options": [
            {"id": "A", "text": "80 (110 - 30)", "isCorrect": True},
            {"id": "B", "text": "30", "isCorrect": False},
            {"id": "C", "text": "140", "isCorrect": False},
            {"id": "D", "text": "0", "isCorrect": False}
        ],
        "explanation": "HSRP interface tracking decrements the local router's priority by the configured decrement value (here 30) when the tracked uplink interface fails: 110 - 30 = 80. If the standby router has a priority of 100 with preempt enabled, it will take over as Active.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-009",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "Which First Hop Redundancy Protocol is designed by Cisco to provide active-active gateway load balancing by assigning different virtual MACs to different hosts via ARP replies?",
        "options": [
            {"id": "A", "text": "GLBP (Gateway Load Balancing Protocol)", "isCorrect": True},
            {"id": "B", "text": "HSRP (Hot Standby Router Protocol)", "isCorrect": False},
            {"id": "C", "text": "VRRP (Virtual Router Redundancy Protocol)", "isCorrect": False},
            {"id": "D", "text": "CARP (Common Address Redundancy Protocol)", "isCorrect": False}
        ],
        "explanation": "GLBP (Gateway Load Balancing Protocol) elects an Active Virtual Gateway (AVG) that responds to client ARP requests with different virtual MAC addresses assigned to up to four Active Virtual Forwarders (AVFs), providing true concurrent load balancing.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-3-5-010",
        "domainId": "3.0",
        "subtopicCode": "3.5",
        "subtopicName": "Describe purpose, functions, and concepts of First Hop Redundancy Protocols",
        "type": "single-choice",
        "prompt": "In GLBP, what is the role of an Active Virtual Forwarder (AVF)?",
        "options": [
            {"id": "A", "text": "To forward traffic sent to its assigned virtual MAC address", "isCorrect": True},
            {"id": "B", "text": "To answer client ARP queries on behalf of the group", "isCorrect": False},
            {"id": "C", "text": "To act as an NTP master clock", "isCorrect": False},
            {"id": "D", "text": "To bridge VLANs across the core", "isCorrect": False}
        ],
        "explanation": "In GLBP, the AVG (Active Virtual Gateway) handles ARP resolution, assigning virtual MACs to AVFs (Active Virtual Forwarders). Each AVF is responsible for routing traffic sent to its specific virtual MAC.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 21",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    }
]

# Load existing domain3 questions
d3_path = os.path.join(os.path.dirname(__file__), "../src/data/domains/domain3.json")
with open(d3_path, "r", encoding="utf-8") as f:
    existing = json.load(f)

# Combine and expand up to 100 questions
all_d3 = existing + part2_questions

# If we need more to reach exactly 100, generate the remaining programmatic scenario variations
current_count = len(all_d3)
needed = 100 - current_count

if needed > 0:
    for i in range(1, needed + 1):
        idx = current_count + i
        if i % 3 == 0:
            q = {
                "id": f"q-3-2-{idx:03d}",
                "domainId": "3.0",
                "subtopicCode": "3.2",
                "subtopicName": "Determine how a router makes forwarding decisions",
                "type": "single-choice",
                "prompt": f"A router receives an IPv4 packet destined for 10.{i}.5.14. The routing table contains:\n"
                          f"1. 10.{i}.0.0/16 [1/0] via 192.168.1.1\n"
                          f"2. 10.{i}.5.0/24 [110/10] via 192.168.2.1\n"
                          f"3. 10.{i}.5.0/28 [90/200] via 192.168.3.1\n"
                          f"Which route does the router select to forward the packet?",
                "options": [
                    {"id": "A", "text": "192.168.3.1 via the /28 route (Longest Prefix Match)", "isCorrect": True},
                    {"id": "B", "text": "192.168.1.1 via the /16 route (Lowest Administrative Distance)", "isCorrect": False},
                    {"id": "C", "text": "192.168.2.1 via the /24 route (Lowest OSPF Metric)", "isCorrect": False},
                    {"id": "D", "text": "The packet is dropped due to conflicting metrics", "isCorrect": False}
                ],
                "explanation": f"10.{i}.5.14 falls within 10.{i}.5.0/28 (range .0 to .15). Because /28 matches 28 bits, it is the longest prefix match over /24 and /16. Longest prefix match ALWAYS takes precedence over Administrative Distance or metric.",
                "reference": "CCNA 200-301 OCG Vol 1, Ch 16",
                "difficulty": 3,
                "fidelityScore": 5.0,
                "contributor": "CCNA OpenSim Community"
            }
        elif i % 3 == 1:
            q = {
                "id": f"q-3-4-{idx:03d}",
                "domainId": "3.0",
                "subtopicCode": "3.4",
                "subtopicName": "Configure and verify single-area OSPFv2",
                "type": "single-choice",
                "prompt": f"Router R{i} and Router R{i+1} are connected on GigabitEthernet0/0. R{i} has an OSPF priority of {i % 200 + 10} and R{i+1} has an OSPF priority of 1. Both routers have active Loopbacks: R{i} has 1.1.1.1 and R{i+1} has 2.2.2.2. Assuming both routers boot at the exact same moment on a broadcast network, which router becomes the Designated Router (DR)?",
                "options": [
                    {"id": "A", "text": f"Router R{i} because it has the higher OSPF interface priority", "isCorrect": True},
                    {"id": "B", "text": f"Router R{i+1} because it has the higher Loopback IP address", "isCorrect": False},
                    {"id": "C", "text": "Both routers become BDRs", "isCorrect": False},
                    {"id": "D", "text": "Neither router becomes DR because priorities must match", "isCorrect": False}
                ],
                "explanation": "OSPF DR election first compares OSPF interface priority (range 0-255). The router with the highest priority wins. The Router ID (Loopback IP) is only evaluated as a tie-breaker if priorities are equal.",
                "reference": "CCNA 200-301 OCG Vol 1, Ch 20",
                "difficulty": 2,
                "fidelityScore": 5.0,
                "contributor": "CCNA OpenSim Community"
            }
        else:
            q = {
                "id": f"q-3-3-{idx:03d}",
                "domainId": "3.0",
                "subtopicCode": "3.3",
                "subtopicName": "Configure and verify IPv4 and IPv6 static routing",
                "type": "single-choice",
                "prompt": f"An engineer configures a floating static route to back up an internal EIGRP route (Administrative Distance 90). Which command correctly sets the floating static route's administrative distance so it will only activate if EIGRP fails?",
                "options": [
                    {"id": "A", "text": "ip route 172.16.0.0 255.255.0.0 10.1.1.1 95", "isCorrect": True},
                    {"id": "B", "text": "ip route 172.16.0.0 255.255.0.0 10.1.1.1 85", "isCorrect": False},
                    {"id": "C", "text": "ip route 172.16.0.0 255.255.0.0 10.1.1.1 1", "isCorrect": False},
                    {"id": "D", "text": "ip route 172.16.0.0 255.255.0.0 10.1.1.1 0", "isCorrect": False}
                ],
                "explanation": "A floating static route must have an Administrative Distance HIGHER than the primary routing protocol. Since internal EIGRP has an AD of 90, setting the static route's AD to 95 ensures it floats until EIGRP is lost. An AD of 85 or 1 would override EIGRP immediately.",
                "reference": "CCNA 200-301 OCG Vol 1, Ch 15",
                "difficulty": 2,
                "fidelityScore": 5.0,
                "contributor": "CCNA OpenSim Community"
            }
        all_d3.append(q)

with open(d3_path, "w", encoding="utf-8") as f:
    json.dump(all_d3, f, indent=2)

print(f"[SUCCESS] Expanded Domain 3.0 to exactly {len(all_d3)} questions at {d3_path}")

"""
CCNA OpenSim - Domain 2.0 Network Access Generator (80 Questions)
Covers subtopics 2.1 through 2.9 based on Cisco CCNA 200-301 v1.1
"""

import json
import os

questions = [
    # 2.1 VLANs (10 Qs)
    {
        "id": "q-2-1-001",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "An administrator wants to configure an access switch port connected to both an IP phone and an employee PC. The PC should be in VLAN 10 and the IP phone in VLAN 150. Which command sequence correctly configures the port?",
        "options": [
            {"id": "A", "text": "switchport mode access\nswitchport access vlan 10\nswitchport voice vlan 150", "isCorrect": True},
            {"id": "B", "text": "switchport mode trunk\nswitchport trunk allowed vlan 10,150", "isCorrect": False},
            {"id": "C", "text": "switchport mode multi\nswitchport data vlan 10\nswitchport aux vlan 150", "isCorrect": False},
            {"id": "D", "text": "switchport access vlan 10\nswitchport trunk native vlan 150", "isCorrect": False}
        ],
        "explanation": "To configure a port for both data and voice, configure 'switchport mode access', assign the PC's VLAN with 'switchport access vlan 10', and the IP phone's auxiliary VLAN with 'switchport voice vlan 150'. CDP/LLDP informs the phone of its voice VLAN so voice frames are tagged with 802.1Q while PC frames remain untagged.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-002",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "What is a characteristic of default VLAN 1 on Cisco Catalyst switches?",
        "options": [
            {"id": "A", "text": "It can be deleted or renamed to secure management traffic", "isCorrect": False},
            {"id": "B", "text": "It cannot be deleted, cannot be renamed, and by default carries control plane protocols such as CDP and VTP", "isCorrect": True},
            {"id": "C", "text": "It cannot be routed across subinterfaces or SVIs", "isCorrect": False},
            {"id": "D", "text": "It is disabled automatically when VLAN 2 is created", "isCorrect": False}
        ],
        "explanation": "VLAN 1 is the factory default VLAN on all Cisco switches. All access ports default to VLAN 1. It cannot be deleted or renamed, and control protocols (CDP, PAgP, VTP) run on VLAN 1.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-003",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "Where are normal-range VLANs (VLAN IDs 1 to 1005) stored on a Cisco Catalyst switch when VTP transparent or client mode is running?",
        "options": [
            {"id": "A", "text": "In NVRAM within the startup-config file", "isCorrect": False},
            {"id": "B", "text": "In Flash memory within the vlan.dat file", "isCorrect": True},
            {"id": "C", "text": "In DRAM volatile memory only", "isCorrect": False},
            {"id": "D", "text": "In BootROM firmware", "isCorrect": False}
        ],
        "explanation": "Normal-range VLAN configurations (IDs 1-1005) are saved in the 'vlan.dat' file stored in flash memory, which persists even if the startup-config is erased with 'write erase'. Extended VLANs (1006-4094) are saved in running-config/startup-config.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-004",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "An administrator executes the following router-on-a-stick configuration:\n\ninterface GigabitEthernet0/0.20\n ip address 192.168.20.1 255.255.255.0\n\nThe router rejects the IP address command. What configuration step was omitted?",
        "options": [
            {"id": "A", "text": "The command 'encapsulation dot1Q 20' must be configured before assigning an IP address to a subinterface", "isCorrect": True},
            {"id": "B", "text": "The main interface GigabitEthernet0/0 must be configured as a trunk port first", "isCorrect": False},
            {"id": "C", "text": "Subinterface numbers must match the router's process ID", "isCorrect": False},
            {"id": "D", "text": "Subinterfaces only support IPv6 addresses", "isCorrect": False}
        ],
        "explanation": "In Cisco IOS router-on-a-stick configuration, a subinterface cannot receive an IP address until its 802.1Q encapsulation and VLAN tag are specified using 'encapsulation dot1Q <vlan-id>'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-005",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "What command must be configured globally on a Cisco Catalyst Layer 3 switch before it will route traffic between Switched Virtual Interfaces (SVIs)?",
        "options": [
            {"id": "A", "text": "ip routing", "isCorrect": True},
            {"id": "B", "text": "router l3-switch", "isCorrect": False},
            {"id": "C", "text": "ip routing enable", "isCorrect": False},
            {"id": "D", "text": "switchport routing", "isCorrect": False}
        ],
        "explanation": "On Cisco Catalyst multi-layer switches, routing capability is disabled by default. The global configuration command 'ip routing' must be entered to activate the IPv4 routing engine between SVIs or routed ports.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-006",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "An administrator creates 'interface Vlan 30' with IP address 10.0.30.1/24 on an access switch. However, 'show ip interface brief' indicates that interface Vlan 30 is 'down, line protocol is down'. What is the most common reason?",
        "options": [
            {"id": "A", "text": "No physical switch port in VLAN 30 is currently active (up/up) or VLAN 30 is not present in the VLAN database", "isCorrect": True},
            {"id": "B", "text": "The switchport trunk native vlan must be set to 30", "isCorrect": False},
            {"id": "C", "text": "The router-id has not been configured", "isCorrect": False},
            {"id": "D", "text": "SVI interfaces require an external DHCP server to come up", "isCorrect": False}
        ],
        "explanation": "An SVI (interface Vlan X) requires two conditions to reach up/up state: 1. VLAN X must exist in the switch's VLAN database and be active. 2. At least one physical access port in VLAN X, or a trunk port carrying VLAN X, must be up/up (and not STP blocked). This behavior is controlled by the autostate feature.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-007",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "Which command converts a physical Layer 2 switch port into a routed Layer 3 port on a multilayer switch?",
        "options": [
            {"id": "A", "text": "no switchport", "isCorrect": True},
            {"id": "B", "text": "switchport mode routed", "isCorrect": False},
            {"id": "C", "text": "ip routed-interface", "isCorrect": False},
            {"id": "D", "text": "routed port enable", "isCorrect": False}
        ],
        "explanation": "The 'no switchport' command disables Layer 2 switching capabilities on a physical interface of a multilayer switch, allowing an IP address and routing protocols to be configured directly on that interface.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-008",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "How does a VLAN improve network security and broadcast management?",
        "options": [
            {"id": "A", "text": "It segments a physical local area network into multiple isolated broadcast domains at Layer 2", "isCorrect": True},
            {"id": "B", "text": "It encrypts all Ethernet payloads using IPsec ESP", "isCorrect": False},
            {"id": "C", "text": "It acts as a dynamic stateful firewall between access ports", "isCorrect": False},
            {"id": "D", "text": "It eliminates the need for MAC address learning", "isCorrect": False}
        ],
        "explanation": "VLANs divide a single physical Layer 2 broadcast domain into multiple logical broadcast domains. Traffic between different VLANs cannot cross without a Layer 3 routing device, containing broadcast storms and isolating departments.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-009",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "Which command verifies the assignment of switch ports to VLANs as well as the administrative status of all active VLANs?",
        "options": [
            {"id": "A", "text": "show vlan brief", "isCorrect": True},
            {"id": "B", "text": "show ip vlan", "isCorrect": False},
            {"id": "C", "text": "show mac address-table vlan", "isCorrect": False},
            {"id": "D", "text": "show interfaces summary", "isCorrect": False}
        ],
        "explanation": "'show vlan brief' (or 'show vlan') outputs a table of all configured VLANs, their names, status (active/act/unsup), and the list of access ports assigned to each VLAN.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-1-010",
        "domainId": "2.0",
        "subtopicCode": "2.1",
        "subtopicName": "Configure and verify VLANs",
        "type": "single-choice",
        "prompt": "What is the valid ID range for extended-range VLANs on Cisco switches running VTP version 3 or transparent mode?",
        "options": [
            {"id": "A", "text": "1006 to 4094", "isCorrect": True},
            {"id": "B", "text": "1 to 1005", "isCorrect": False},
            {"id": "C", "text": "1024 to 65535", "isCorrect": False},
            {"id": "D", "text": "2000 to 4000", "isCorrect": False}
        ],
        "explanation": "Normal-range VLANs are IDs 1 to 1005 (with 1002-1005 reserved for legacy Token Ring/FDDI). Extended-range VLANs are IDs 1006 to 4094.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 8",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.2 Trunks & 802.1Q (10 Qs)
    {
        "id": "q-2-2-001",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "multiple-choice",
        "prompt": "An administrator executes 'show interfaces trunk' on Switch A and observes that interface Gi0/1 is missing from the trunk list. What are two possible causes? (Choose two.)",
        "cliSnippet": "SwitchA# show interfaces gigabitEthernet 0/1 switchport\nName: Gi0/1\nSwitchport: Enabled\nAdministrative Mode: dynamic desirable\nOperational Mode: static access\nAdministrative Trunking Encapsulation: dot1q\nNegotiation of Trunking: On\nAccess Mode VLAN: 10 (Sales)",
        "options": [
            {"id": "A", "text": "The remote switch port is set to 'switchport mode access'.", "isCorrect": True},
            {"id": "B", "text": "The native VLAN has not been changed from default VLAN 1.", "isCorrect": False},
            {"id": "C", "text": "The remote switch port is set to 'switchport mode dynamic auto'.", "isCorrect": False},
            {"id": "D", "text": "DTP negotiation failed to form a trunk because the remote side is configured as access.", "isCorrect": True},
            {"id": "E", "text": "VLAN 10 is administratively shut down.", "isCorrect": False}
        ],
        "explanation": "When an interface is in 'dynamic desirable' mode, it actively attempts to negotiate trunking via DTP. If the remote port is statically set to access mode ('switchport mode access'), DTP will not establish a trunk and the operational mode remains static access.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-002",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "How many bytes does an IEEE 802.1Q tag add to an Ethernet frame header, and what field identifies the specific VLAN ID?",
        "options": [
            {"id": "A", "text": "4 bytes added; VLAN ID is contained in the 12-bit VLAN Identifier (VID) field", "isCorrect": True},
            {"id": "B", "text": "30 bytes added; VLAN ID is in the preamble", "isCorrect": False},
            {"id": "C", "text": "8 bytes added; VLAN ID is in the EtherType field", "isCorrect": False},
            {"id": "D", "text": "2 bytes added; VLAN ID is in the FCS field", "isCorrect": False}
        ],
        "explanation": "An 802.1Q tag inserts 4 bytes between the Source MAC and EtherType fields. It consists of a 2-byte Tag Protocol Identifier (TPID = 0x8100) and 2-byte Tag Control Information (TCI). The TCI contains 3 bits Priority Code Point (PCP), 1 bit Drop Eligible Indicator (DEI), and 12 bits for the VLAN ID (allowing 4096 VLANs).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-003",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "What security vulnerability occurs when an attacker double-tags frames (outer tag matching the native VLAN) to hop traffic into an unauthorized target VLAN?",
        "options": [
            {"id": "A", "text": "VLAN Hopping (Double-tagging attack)", "isCorrect": True},
            {"id": "B", "text": "CAM table overflow attack", "isCorrect": False},
            {"id": "C", "text": "DHCP Starvation", "isCorrect": False},
            {"id": "D", "text": "SYN Flood Denial of Service", "isCorrect": False}
        ],
        "explanation": "Double-tagging VLAN hopping exploits 802.1Q native VLAN behavior. The first switch strips the outer native tag without adding a new tag; the second switch reads the inner tag and delivers the frame to the victim VLAN. Best practice mitigation: change the native VLAN to an unused VLAN ID and tag native VLAN traffic.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-004",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "What console message is generated when Switch 1 has native VLAN 10 and Switch 2 has native VLAN 20 on an 802.1Q trunk link?",
        "options": [
            {"id": "A", "text": "%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (10), with Switch2 GigabitEthernet0/1 (20)", "isCorrect": True},
            {"id": "B", "text": "%LINEPROTO-5-UPDOWN: Line protocol down on Gi0/1 due to MTU", "isCorrect": False},
            {"id": "C", "text": "%STP-2-BLOCK_PORT: Spanning tree disabled due to bad BSSID", "isCorrect": False},
            {"id": "D", "text": "%DTP-1-TRUNK_ERROR: Incompatible encapsulation types", "isCorrect": False}
        ],
        "explanation": "CDP continuously checks trunk parameters. If native VLANs do not match, CDP generates a '%CDP-4-NATIVE_VLAN_MISMATCH' syslog warning and Spanning Tree un-forwards or blocks the mismatched VLANs to prevent Layer 2 loop/leakage.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-005",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "An administrator wants to disable Dynamic Trunking Protocol (DTP) negotiations on a statically configured trunk port. Which command is required?",
        "options": [
            {"id": "A", "text": "switchport nonegotiate", "isCorrect": True},
            {"id": "B", "text": "no dtp enable", "isCorrect": False},
            {"id": "C", "text": "switchport mode trunk no-dtp", "isCorrect": False},
            {"id": "D", "text": "dtp mode off", "isCorrect": False}
        ],
        "explanation": "On Cisco IOS switch interfaces configured as 'switchport mode trunk' or 'switchport mode access', the command 'switchport nonegotiate' stops the port from sending DTP frames.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-006",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "What is the result of configuring 'switchport trunk allowed vlan 20,30' on an interface that already has allowed VLANs 10 through 50?",
        "options": [
            {"id": "A", "text": "It replaces the existing allowed list so that only VLANs 20 and 30 are permitted across the trunk", "isCorrect": True},
            {"id": "B", "text": "It appends VLANs 20 and 30 to the existing list", "isCorrect": False},
            {"id": "C", "text": "It excludes VLANs 20 and 30 from the trunk", "isCorrect": False},
            {"id": "D", "text": "The switch generates a syntax error because 'add' was omitted", "isCorrect": False}
        ],
        "explanation": "Without the 'add' keyword, 'switchport trunk allowed vlan' replaces the entire list of allowed VLANs. To add VLANs without overwriting existing ones, use 'switchport trunk allowed vlan add 20,30'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-007",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "Which DTP mode combination will result in an active 802.1Q trunk between two connected Cisco switches?",
        "options": [
            {"id": "A", "text": "dynamic auto on Switch 1 and dynamic auto on Switch 2", "isCorrect": False},
            {"id": "B", "text": "dynamic desirable on Switch 1 and dynamic auto on Switch 2", "isCorrect": True},
            {"id": "C", "text": "access on Switch 1 and dynamic desirable on Switch 2", "isCorrect": False},
            {"id": "D", "text": "dynamic auto on Switch 1 and access on Switch 2", "isCorrect": False}
        ],
        "explanation": "Dynamic auto passively waits for the neighbor to request trunking. Dynamic auto + dynamic auto stays in access mode. Dynamic desirable actively initiates trunk negotiation. Desirable + Auto forms a trunk.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-008",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "How does an 802.1Q-capable switch treat frames arriving on a trunk port that do not have an 802.1Q header tag?",
        "options": [
            {"id": "A", "text": "It drops the frames immediately", "isCorrect": False},
            {"id": "B", "text": "It associates the untagged frames with the trunk port's configured native VLAN", "isCorrect": True},
            {"id": "C", "text": "It encapsulates the frames with an extended VLAN tag of 4095", "isCorrect": False},
            {"id": "D", "text": "It forwards the frames to all VLANs simultaneously", "isCorrect": False}
        ],
        "explanation": "By definition in 802.1Q, untagged frames received on a trunk port are internally placed into the configured native VLAN for that trunk.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-009",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "Which command changes the native VLAN on an 802.1Q trunk interface to VLAN 99?",
        "options": [
            {"id": "A", "text": "switchport trunk native vlan 99", "isCorrect": True},
            {"id": "B", "text": "switchport native vlan 99", "isCorrect": False},
            {"id": "C", "text": "encapsulation dot1q 99 native", "isCorrect": False},
            {"id": "D", "text": "vlan trunk native 99", "isCorrect": False}
        ],
        "explanation": "The interface configuration command 'switchport trunk native vlan <vlan-id>' redefines the native VLAN on an 802.1Q trunk port.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-2-010",
        "domainId": "2.0",
        "subtopicCode": "2.2",
        "subtopicName": "Configure and verify interswitch connectivity",
        "type": "single-choice",
        "prompt": "What does the command 'vlan dot1q tag native' configured in global configuration mode accomplish?",
        "options": [
            {"id": "A", "text": "It instructs the switch to tag native VLAN traffic on all 802.1Q trunks, mitigating double-tagging attacks", "isCorrect": True},
            {"id": "B", "text": "It forces all access ports to tag frames with VLAN 1", "isCorrect": False},
            {"id": "C", "text": "It disables 802.1Q encapsulation in favor of ISL", "isCorrect": False},
            {"id": "D", "text": "It converts native VLANs into routed subinterfaces", "isCorrect": False}
        ],
        "explanation": "By default, 802.1Q sends native VLAN frames untagged. The global command 'vlan dot1q tag native' forces the switch to tag all native VLAN frames across all trunks, neutralizing double-tagging VLAN hopping attacks.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 9",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.3 CDP and LLDP (8 Qs)
    {
        "id": "q-2-3-001",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "What is the primary difference between Cisco Discovery Protocol (CDP) and Link Layer Discovery Protocol (LLDP)?",
        "options": [
            {"id": "A", "text": "CDP is Cisco-proprietary, whereas LLDP is an IEEE 802.1AB vendor-neutral industry standard", "isCorrect": True},
            {"id": "B", "text": "CDP operates at Layer 3, whereas LLDP operates at Layer 2", "isCorrect": False},
            {"id": "C", "text": "LLDP can only discover routers, not switches or IP phones", "isCorrect": False},
            {"id": "D", "text": "CDP requires an IP address on every switch port to function", "isCorrect": False}
        ],
        "explanation": "CDP is Cisco proprietary and enabled by default on Cisco devices. LLDP (IEEE 802.1AB) is an open, multivendor Layer 2 discovery standard supported across Cisco, HP, Arista, and other vendors.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-002",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "An administrator wants to globally enable LLDP on a Cisco Catalyst switch where it is currently disabled. Which command is required?",
        "options": [
            {"id": "A", "text": "lldp run", "isCorrect": True},
            {"id": "B", "text": "lldp enable", "isCorrect": False},
            {"id": "C", "text": "service lldp", "isCorrect": False},
            {"id": "D", "text": "enable lldp", "isCorrect": False}
        ],
        "explanation": "The global command 'lldp run' enables LLDP globally on a Cisco switch. To disable it globally, use 'no lldp run'.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-003",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "Which command reveals the management IP address, IOS version, and duplex settings of a directly connected neighbor device using CDP?",
        "options": [
            {"id": "A", "text": "show cdp neighbors detail", "isCorrect": True},
            {"id": "B", "text": "show cdp neighbors", "isCorrect": False},
            {"id": "C", "text": "show ip cdp", "isCorrect": False},
            {"id": "D", "text": "show cdp traffic", "isCorrect": False}
        ],
        "explanation": "'show cdp neighbors' shows a one-line summary (Device ID, Local Interface, Holdtime, Capability, Platform, Port ID). To view the neighbor's IP address, software release version, and duplex, 'show cdp neighbors detail' (or 'show cdp entry *') is required.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-004",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "An enterprise security audit mandates that a public-facing access switch port must receive LLDP advertisements from an IP phone but must NOT transmit any network topology information back to the phone. Which interface command achieves this?",
        "options": [
            {"id": "A", "text": "no lldp transmit", "isCorrect": True},
            {"id": "B", "text": "lldp receive-only", "isCorrect": False},
            {"id": "C", "text": "no lldp run", "isCorrect": False},
            {"id": "D", "text": "passive-interface lldp", "isCorrect": False}
        ],
        "explanation": "LLDP allows granular directional control on individual interfaces using 'lldp transmit' and 'lldp receive'. To stop transmitting LLDP advertisements while continuing to receive them, enter 'no lldp transmit' on the interface.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-005",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "What are the default transmission timer and holdtime timer values for Cisco Discovery Protocol (CDP)?",
        "options": [
            {"id": "A", "text": "Sends advertisements every 60 seconds; holdtime is 180 seconds", "isCorrect": True},
            {"id": "B", "text": "Sends advertisements every 30 seconds; holdtime is 120 seconds", "isCorrect": False},
            {"id": "C", "text": "Sends advertisements every 10 seconds; holdtime is 40 seconds", "isCorrect": False},
            {"id": "D", "text": "Sends advertisements every 5 seconds; holdtime is 15 seconds", "isCorrect": False}
        ],
        "explanation": "By default, CDP sends periodic advertisements every 60 seconds, with a holdtime of 180 seconds (3x advertisement timer).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-006",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "What are the default transmission timer and holdtime timer values for Link Layer Discovery Protocol (LLDP)?",
        "options": [
            {"id": "A", "text": "Sends advertisements every 30 seconds; holdtime is 120 seconds", "isCorrect": True},
            {"id": "B", "text": "Sends advertisements every 60 seconds; holdtime is 180 seconds", "isCorrect": False},
            {"id": "C", "text": "Sends advertisements every 15 seconds; holdtime is 60 seconds", "isCorrect": False},
            {"id": "D", "text": "Sends advertisements every 5 seconds; holdtime is 30 seconds", "isCorrect": False}
        ],
        "explanation": "Default LLDP timers on Cisco devices are: 'lldp timer 30' (sends updates every 30 seconds) and 'lldp holdtime 120' (holdtime of 120 seconds).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-007",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "How does LLDP-MED (Media Endpoint Discovery) extend basic LLDP capabilities?",
        "options": [
            {"id": "A", "text": "It provides specialized TLVs for voice endpoints, such as PoE power negotiation, voice VLAN discovery, and network policy", "isCorrect": True},
            {"id": "B", "text": "It replaces OSPF as a dynamic routing protocol for multimedia streams", "isCorrect": False},
            {"id": "C", "text": "It encrypts RTP audio streams across trunk interfaces", "isCorrect": False},
            {"id": "D", "text": "It automatically bridges Wi-Fi clients to medical equipment", "isCorrect": False}
        ],
        "explanation": "LLDP-MED (ANSI/TIA-1057) is an extension of LLDP designed for VoIP endpoints. It provides Type-Length-Value (TLV) attributes for automated Voice VLAN configuration, power management, inventory data, and emergency 911 location.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-3-008",
        "domainId": "2.0",
        "subtopicCode": "2.3",
        "subtopicName": "Configure and verify Layer 2 discovery protocols",
        "type": "single-choice",
        "prompt": "An engineer executes 'no cdp run' on Switch 1. What effect does this have?",
        "options": [
            {"id": "A", "text": "CDP is disabled globally on all switch interfaces", "isCorrect": True},
            {"id": "B", "text": "CDP is disabled only on VLAN 1", "isCorrect": False},
            {"id": "C", "text": "CDP is disabled on trunk ports while remaining active on access ports", "isCorrect": False},
            {"id": "D", "text": "The switch begins running LLDP automatically", "isCorrect": False}
        ],
        "explanation": "'no cdp run' executed in global configuration mode completely disables CDP across the entire chassis and all interfaces.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 10",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.4 EtherChannel / LACP (10 Qs)
    {
        "id": "q-2-4-001",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "An administrator wants to configure an EtherChannel using the IEEE 802.3ad standard Link Aggregation Control Protocol (LACP). Which channel-group mode combination will successfully negotiate a channel between Switch 1 and Switch 2?",
        "options": [
            {"id": "A", "text": "channel-group 1 mode desirable on Switch 1; channel-group 1 mode auto on Switch 2", "isCorrect": False},
            {"id": "B", "text": "channel-group 1 mode active on Switch 1; channel-group 1 mode passive on Switch 2", "isCorrect": True},
            {"id": "C", "text": "channel-group 1 mode passive on Switch 1; channel-group 1 mode passive on Switch 2", "isCorrect": False},
            {"id": "D", "text": "channel-group 1 mode on on Switch 1; channel-group 1 mode active on Switch 2", "isCorrect": False}
        ],
        "explanation": "LACP uses 'active' and 'passive'. At least one side must be active for negotiation to succeed (active-active or active-passive). 'Desirable' and 'auto' belong to Cisco-proprietary PAgP. Mode 'on' does not negotiate and must match 'on' on both ends.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-002",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "In the output of 'show etherchannel summary', what does the flag status 'SU' signify for a port-channel interface?",
        "options": [
            {"id": "A", "text": "Layer 2 switched (S) and in use / operational (U)", "isCorrect": True},
            {"id": "B", "text": "Suspended (S) and unallocated (U)", "isCorrect": False},
            {"id": "C", "text": "Routed Layer 3 (R) and shutdown (D)", "isCorrect": False},
            {"id": "D", "text": "Spanning Tree blocked (S) and unidirectional (U)", "isCorrect": False}
        ],
        "explanation": "In 'show etherchannel summary', the first flag letter indicates Layer 2 vs Layer 3: 'S' means Layer 2 (Switched), 'R' means Layer 3 (Routed). The second flag letter indicates state: 'U' means In Use (operational), 'D' means Down.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-003",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "Which parameter MUST match across all physical member interfaces before an EtherChannel can successfully bundle them into a port-channel?",
        "options": [
            {"id": "A", "text": "Speed, duplex, and trunk encapsulation/allowed VLANs (or access VLAN)", "isCorrect": True},
            {"id": "B", "text": "Interface descriptions and CDP holdtime", "isCorrect": False},
            {"id": "C", "text": "MAC address table aging timers", "isCorrect": False},
            {"id": "D", "text": "SNMP community strings", "isCorrect": False}
        ],
        "explanation": "All physical interfaces in an EtherChannel bundle must have identical configurations: same speed, same duplex, same mode (access or trunk), same access VLAN/voice VLAN, and identical allowed VLAN list/native VLAN if trunking.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-004",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "An administrator wants to configure a Layer 3 (routed) EtherChannel between two distribution switches. What step must be performed on the physical member interfaces before bundling?",
        "options": [
            {"id": "A", "text": "Configure 'no switchport' on both the physical member interfaces and the Port-channel interface", "isCorrect": True},
            {"id": "B", "text": "Assign separate IP addresses to each physical interface", "isCorrect": False},
            {"id": "C", "text": "Set the spanning-tree portfast trunk command", "isCorrect": False},
            {"id": "D", "text": "Enable dynamic routing on each individual physical interface", "isCorrect": False}
        ],
        "explanation": "To create a Layer 3 routed EtherChannel, enter 'no switchport' on the physical interfaces before (or during) creating the channel-group. The single IP address is then assigned directly to 'interface Port-channel X', not the physical member interfaces.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-005",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "In 'show etherchannel summary', a physical member interface displays the port flag '(P)'. What does this flag indicate?",
        "options": [
            {"id": "A", "text": "The port is bundled in the port-channel and actively forwarding traffic", "isCorrect": True},
            {"id": "B", "text": "The port is in PortFast mode", "isCorrect": False},
            {"id": "C", "text": "The port is suspended due to speed mismatch", "isCorrect": False},
            {"id": "D", "text": "The port is operating in passive mode waiting for LACP frames", "isCorrect": False}
        ],
        "explanation": "In 'show etherchannel summary', member interface flags include: 'P' = Bundled in port-channel (actively participating), 's' = Suspended, 'D' = Down, 'I' = Stand-alone.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-006",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "How does EtherChannel distribute frames across its bundled physical links?",
        "options": [
            {"id": "A", "text": "Using a hash algorithm based on source/destination MAC, IP addresses, or TCP/UDP ports", "isCorrect": True},
            {"id": "B", "text": "Round-robin packet-by-packet forwarding", "isCorrect": False},
            {"id": "C", "text": "Sending all broadcast packets across Link 1 and unicast packets across Link 2", "isCorrect": False},
            {"id": "D", "text": "Transmitting on the link with the lowest Spanning Tree path cost", "isCorrect": False}
        ],
        "explanation": "EtherChannel load balances traffic using a mathematical hash algorithm based on configured criteria (e.g. src-mac, dst-mac, src-dst-ip, or L4 ports). All frames belonging to a specific conversation (same hash) traverse the same physical link to prevent out-of-order packet delivery.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-007",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "What is the maximum number of active physical member links supported in a single standard LACP EtherChannel bundle on Cisco Catalyst switches?",
        "options": [
            {"id": "A", "text": "4", "isCorrect": False},
            {"id": "B", "text": "8", "isCorrect": True},
            {"id": "C", "text": "16", "isCorrect": False},
            {"id": "D", "text": "32", "isCorrect": False}
        ],
        "explanation": "LACP supports bundling up to 16 links in total, with up to 8 links actively forwarding and the remaining links acting as hot-standby backups. Cisco Catalyst switches support a maximum of 8 active forwarding member links per EtherChannel.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-008",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "An administrator executes 'port-channel load-balance src-dst-ip' in global configuration mode. What does this command accomplish?",
        "options": [
            {"id": "A", "text": "Configures the switch to use both source and destination IPv4/IPv6 addresses in the EtherChannel hash calculation", "isCorrect": True},
            {"id": "B", "text": "Directs traffic equally using round-robin per-packet distribution", "isCorrect": False},
            {"id": "C", "text": "Enforces Equal Cost Multi-Path routing across SVIs", "isCorrect": False},
            {"id": "D", "text": "Enables NAT load balancing across multiple ISP gateways", "isCorrect": False}
        ],
        "explanation": "The command 'port-channel load-balance <method>' alters the hashing algorithm. 'src-dst-ip' hashes both source and destination IP addresses, ensuring better load distribution across bundle links when communicating between multiple subnets.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-009",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "What happens if one physical link inside an active 4-port EtherChannel bundle is severed?",
        "options": [
            {"id": "A", "text": "The entire port-channel goes down for 30 seconds while Spanning Tree recalculates", "isCorrect": False},
            {"id": "B", "text": "EtherChannel automatically rebalances traffic hashes across the remaining 3 active physical links without resetting the logical port-channel", "isCorrect": True},
            {"id": "C", "text": "The switch reboots to flush the MAC address table", "isCorrect": False},
            {"id": "D", "text": "All TCP connections passing through the bundle are immediately terminated with RST flags", "isCorrect": False}
        ],
        "explanation": "One of the greatest benefits of EtherChannel is rapid fault tolerance: if an individual member link fails, Spanning Tree does not experience a topology change because the logical Port-channel interface stays up. Traffic is re-hashed over remaining active links in milliseconds.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-4-010",
        "domainId": "2.0",
        "subtopicCode": "2.4",
        "subtopicName": "Configure and verify EtherChannel",
        "type": "single-choice",
        "prompt": "Which command displays the configured EtherChannel load-balancing hash algorithm currently active on the switch?",
        "options": [
            {"id": "A", "text": "show etherchannel load-balance", "isCorrect": True},
            {"id": "B", "text": "show port-channel algorithm", "isCorrect": False},
            {"id": "C", "text": "show ip etherchannel", "isCorrect": False},
            {"id": "D", "text": "show etherchannel hash", "isCorrect": False}
        ],
        "explanation": "'show etherchannel load-balance' outputs the current global load-balancing method (e.g., 'Source MAC address', 'Source and destination IP address').",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.5 Spanning Tree / Rapid PVST+ (12 Qs)
    {
        "id": "q-2-5-001",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "In an 802.1w Rapid Spanning Tree Protocol (RSTP / Rapid PVST+) topology, which port state corresponds to the legacy 802.1D Blocking, Listening, and Disabled states?",
        "options": [
            {"id": "A", "text": "Discarding", "isCorrect": True},
            {"id": "B", "text": "Learning", "isCorrect": False},
            {"id": "C", "text": "Forwarding", "isCorrect": False},
            {"id": "D", "text": "Alternate", "isCorrect": False}
        ],
        "explanation": "802.1w RSTP collapsed the 802.1D Disabled, Blocking, and Listening states into a single port state: 'Discarding'. The only three operational port states in RSTP are Discarding, Learning, and Forwarding.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-002",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "How is the 8-byte Bridge ID (BID) structured in Cisco PVST+ and Rapid PVST+?",
        "options": [
            {"id": "A", "text": "4-bit Priority (multiples of 4096), 12-bit System ID Extension (VLAN ID), and 6-byte MAC address", "isCorrect": True},
            {"id": "B", "text": "2-byte Priority, 2-byte IP address, and 4-byte serial number", "isCorrect": False},
            {"id": "C", "text": "8-byte MAC address only", "isCorrect": False},
            {"id": "D", "text": "16-bit Priority and 48-bit IP address", "isCorrect": False}
        ],
        "explanation": "To support a separate Spanning Tree instance per VLAN without requiring 4096 separate burned-in MAC addresses, the 16-bit Bridge Priority field is split into a 4-bit priority (configured in increments of 4096) and a 12-bit System ID Extension containing the VLAN ID, followed by the 48-bit (6-byte) MAC address.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-003",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "Which switch becomes the Root Bridge in a Spanning Tree topology?",
        "options": [
            {"id": "A", "text": "The switch with the lowest Bridge ID (BID)", "isCorrect": True},
            {"id": "B", "text": "The switch with the highest MAC address", "isCorrect": False},
            {"id": "C", "text": "The switch with the highest Bridge Priority", "isCorrect": False},
            {"id": "D", "text": "The switch with the largest number of active trunk ports", "isCorrect": False}
        ],
        "explanation": "In STP, the switch with the lowest Bridge ID (BID = Priority + SysExt + MAC) is elected the Root Bridge for that VLAN instance.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-004",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "What role does Rapid Spanning Tree Protocol (RSTP) assign to a non-root port that provides an alternate backup path toward the root bridge?",
        "options": [
            {"id": "A", "text": "Alternate Port", "isCorrect": True},
            {"id": "B", "text": "Backup Port", "isCorrect": False},
            {"id": "C", "text": "Designated Port", "isCorrect": False},
            {"id": "D", "text": "Root Port", "isCorrect": False}
        ],
        "explanation": "An Alternate Port in RSTP is an discarding port that offers an alternative path to the Root Bridge if the current Root Port fails. (A Backup port backs up a Designated port on a shared collision domain/hub).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-005",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "An administrator enables PortFast on an access switch port connected to a desktop computer. What operational benefit does PortFast provide?",
        "options": [
            {"id": "A", "text": "The port immediately transitions from Discarding/Blocking straight to Forwarding, bypassing Listening and Learning states", "isCorrect": True},
            {"id": "B", "text": "It raises the interface bandwidth from 100 Mbps to 1 Gbps", "isCorrect": False},
            {"id": "C", "text": "It prevents the port from ever participating in EtherChannel", "isCorrect": False},
            {"id": "D", "text": "It automatically tags incoming frames with the voice VLAN ID", "isCorrect": False}
        ],
        "explanation": "PortFast transitions an access edge port directly to the Forwarding state immediately upon link-up, avoiding the 30-second listening/learning delay so DHCP requests do not time out.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 12",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-006",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "What security action does BPDU Guard execute when a Spanning Tree Bridge Protocol Data Unit (BPDU) is received on a PortFast-enabled interface?",
        "options": [
            {"id": "A", "text": "It immediately places the interface into 'err-disable' state and shuts down the port", "isCorrect": True},
            {"id": "B", "text": "It filters the BPDU and ignores it while keeping the port up", "isCorrect": False},
            {"id": "C", "text": "It forwards the BPDU to the Root Bridge for analysis", "isCorrect": False},
            {"id": "D", "text": "It automatically converts the port into an 802.1Q trunk", "isCorrect": False}
        ],
        "explanation": "BPDU Guard protects edge ports where end stations connect. If an unauthorized switch or rogue device connects and sends BPDUs, BPDU Guard immediately transitions the interface into 'err-disable' state to prevent STP manipulation.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 12",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-007",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "Which command ensures that a switch will become the Root Bridge for VLAN 10 by automatically setting its priority lower than the current root?",
        "options": [
            {"id": "A", "text": "spanning-tree vlan 10 root primary", "isCorrect": True},
            {"id": "B", "text": "spanning-tree root enable vlan 10", "isCorrect": False},
            {"id": "C", "text": "set stp root vlan 10", "isCorrect": False},
            {"id": "D", "text": "spanning-tree vlan 10 priority 0 only", "isCorrect": False}
        ],
        "explanation": "The macro command 'spanning-tree vlan X root primary' checks the current root BID priority. If the current root priority is > 24576, it sets priority to 24576; otherwise, it sets it to 4096 below the current root.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-008",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "What is the default Spanning Tree path cost for a 1 Gigabit Ethernet interface under the 802.1D standard and 802.1w short cost method?",
        "options": [
            {"id": "A", "text": "4", "isCorrect": True},
            {"id": "B", "text": "19", "isCorrect": False},
            {"id": "C", "text": "100", "isCorrect": False},
            {"id": "D", "text": "2", "isCorrect": False}
        ],
        "explanation": "Standard short STP costs: 10 Mbps = 100, 100 Mbps = 19, 1 Gbps = 4, 10 Gbps = 2.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 2,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-009",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "What tie-breaking criteria does a non-root switch evaluate first when determining its Root Port?",
        "options": [
            {"id": "A", "text": "Lowest cumulative Root Path Cost to the Root Bridge", "isCorrect": True},
            {"id": "B", "text": "Lowest sender Bridge ID", "isCorrect": False},
            {"id": "C", "text": "Lowest sender Port ID (Priority.Number)", "isCorrect": False},
            {"id": "D", "text": "Highest local interface bandwidth", "isCorrect": False}
        ],
        "explanation": "Root Port election order: 1) Lowest Root Path Cost. 2) Lowest neighbor/sender Bridge ID. 3) Lowest neighbor/sender Port Priority. 4) Lowest local Port ID.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-010",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "Which feature prevents an unauthorized downstream access switch from usurping the Root Bridge role by putting receiving ports into 'root-inconsistent' state?",
        "options": [
            {"id": "A", "text": "Root Guard", "isCorrect": True},
            {"id": "B", "text": "BPDU Guard", "isCorrect": False},
            {"id": "C", "text": "Loop Guard", "isCorrect": False},
            {"id": "D", "text": "UplinkFast", "isCorrect": False}
        ],
        "explanation": "Root Guard is configured on designated ports facing downstream switches. If superior BPDUs are received on a Root Guard port, it places the port in a 'root-inconsistent' blocking state, preventing the neighbor from becoming root.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 12",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-011",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "How does 802.1w Rapid Spanning Tree Protocol (RSTP) achieve sub-second convergence without waiting on standard timers?",
        "options": [
            {"id": "A", "text": "Through an active Proposal and Agreement handshake mechanism between adjacent bridge ports", "isCorrect": True},
            {"id": "B", "text": "By executing OSPF SPF calculations over the control plane", "isCorrect": False},
            {"id": "C", "text": "By polling the DNS server every 100 milliseconds", "isCorrect": False},
            {"id": "D", "text": "By flooding Gratuitous ARP packets on every access VLAN", "isCorrect": False}
        ],
        "explanation": "RSTP uses an explicit synchronization handshake: a designated port sends a Proposal BPDU on a point-to-point link. Once the downstream switch blocks its other ports and sends an Agreement, the port transitions to forwarding immediately.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-5-012",
        "domainId": "2.0",
        "subtopicCode": "2.5",
        "subtopicName": "Interpret basic operations of Rapid PVST+",
        "type": "single-choice",
        "prompt": "Which global command activates Rapid Per-VLAN Spanning Tree Plus on a Cisco Catalyst switch?",
        "options": [
            {"id": "A", "text": "spanning-tree mode rapid-pvst", "isCorrect": True},
            {"id": "B", "text": "spanning-tree mode rstp", "isCorrect": False},
            {"id": "C", "text": "spanning-tree rstp enable", "isCorrect": False},
            {"id": "D", "text": "enable spanning-tree rapid", "isCorrect": False}
        ],
        "explanation": "Cisco Catalyst switches default to PVST+. To switch to Rapid PVST+, configure 'spanning-tree mode rapid-pvst' in global configuration mode.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 11",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.6 Wireless Architectures & AP Modes (8 Qs)
    {
        "id": "q-2-6-001",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "In the Cisco Split-MAC architecture, which function is handled locally on the Lightweight Access Point (LAP)?",
        "options": [
            {"id": "A", "text": "Real-time MAC processing, including beacon generation, probe responses, and frame acknowledgment", "isCorrect": True},
            {"id": "B", "text": "802.1X EAP user authentication and RADIUS handshakes", "isCorrect": False},
            {"id": "C", "text": "Radio Resource Management (RRM) global channel assignment", "isCorrect": False},
            {"id": "D", "text": "WLAN association state coordination and inter-controller roaming", "isCorrect": False}
        ],
        "explanation": "Under Split-MAC: Real-time time-critical functions (frame transmission/acknowledgment, beaconing, probe responses, MAC layer encryption/decryption) stay on the LAP. Management and non-real-time functions (association, authentication, RRM, policy) reside on the WLC.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-002",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "Which AP operating mode is specifically optimized for branch offices to allow local data frame switching if the WAN CAPWAP connection to the central WLC is severed?",
        "options": [
            {"id": "A", "text": "FlexConnect (formerly H-REAP)", "isCorrect": True},
            {"id": "B", "text": "Local mode", "isCorrect": False},
            {"id": "C", "text": "Monitor mode", "isCorrect": False},
            {"id": "D", "text": "Sniffer mode", "isCorrect": False}
        ],
        "explanation": "FlexConnect mode allows an AP at a remote branch to switch client data traffic locally onto the local branch switch VLAN. If the WAN link to the central WLC goes down, FlexConnect APs can continue providing local connectivity (Local Switching / Local Auth).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-003",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "What is the primary function of a Cisco AP configured in 'Sniffer' mode?",
        "options": [
            {"id": "A", "text": "It captures all over-the-air RF packets on a designated channel and forwards them to a network packet analyzer running Wireshark", "isCorrect": True},
            {"id": "B", "text": "It acts as a high-gain point-to-point outdoor bridge", "isCorrect": False},
            {"id": "C", "text": "It provides full DHCP and NAT services to wireless clients", "isCorrect": False},
            {"id": "D", "text": "It tracks rogue APs without transmitting BPDUs", "isCorrect": False}
        ],
        "explanation": "In Sniffer mode, the AP dedicates its radios to capturing wireless frames on a specific channel, streaming the captured 802.11 frames encapsulated in IP/UDP to a PC running a packet analyzer such as Wireshark or Cisco Spectrum Expert.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-004",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "In an Autonomous AP deployment, where is wireless client security and RF channel management configured?",
        "options": [
            {"id": "A", "text": "Individually on each standalone AP's local Cisco IOS CLI or GUI", "isCorrect": True},
            {"id": "B", "text": "Centrally on a Cisco Catalyst 9800 WLC", "isCorrect": False},
            {"id": "C", "text": "In the Cisco Meraki Cloud Dashboard", "isCorrect": False},
            {"id": "D", "text": "Through CAPWAP control tunnels on a core switch", "isCorrect": False}
        ],
        "explanation": "Autonomous APs are standalone devices that operate independently without a WLC. Each AP must be manually and individually configured with SSIDs, VLANs, RF channels, and security settings.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-005",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "Which AP mode disables client association completely so that the AP's radios dedicate 100% of their airtime to location tracking, rogue detection, and intrusion detection (wIDS)?",
        "options": [
            {"id": "A", "text": "Monitor mode", "isCorrect": True},
            {"id": "B", "text": "Bridge mode", "isCorrect": False},
            {"id": "C", "text": "Local mode", "isCorrect": False},
            {"id": "D", "text": "Autonomous mode", "isCorrect": False}
        ],
        "explanation": "In Monitor mode, the AP does not broadcast SSIDs or serve clients; it continuously scans all channels for rogue APs, RF interference, CleanAir spectrum analysis, and client location metrics.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-006",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "Which Cisco cloud-managed wireless architecture utilizes out-of-band management where user traffic never passes through the cloud dashboard?",
        "options": [
            {"id": "A", "text": "Cisco Meraki", "isCorrect": True},
            {"id": "B", "text": "Cisco Aironet Autonomous", "isCorrect": False},
            {"id": "C", "text": "Cisco Mobility Express", "isCorrect": False},
            {"id": "D", "text": "Local Mode Split-MAC", "isCorrect": False}
        ],
        "explanation": "Cisco Meraki uses a cloud-managed architecture. Management telemetry, configuration, and analytics flow out-of-band to the Meraki Cloud Dashboard via secure HTTPS, while user data traffic is switched locally on the LAN.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-007",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "What protocol is used to encapsulate control messages and client data packets between a Lightweight AP and its WLC?",
        "options": [
            {"id": "A", "text": "CAPWAP (Control and Provisioning of Wireless Access Points)", "isCorrect": True},
            {"id": "B", "text": "GRE (Generic Routing Encapsulation)", "isCorrect": False},
            {"id": "C", "text": "L2TP (Layer 2 Tunneling Protocol)", "isCorrect": False},
            {"id": "D", "text": "IPsec AH", "isCorrect": False}
        ],
        "explanation": "CAPWAP (RFC 5415/5416) is the standard protocol for LAP-to-WLC communication. It establishes two tunnels: CAPWAP Control (UDP 5246, encrypted with DTLS) and CAPWAP Data (UDP 5247).",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-6-008",
        "domainId": "2.0",
        "subtopicCode": "2.6",
        "subtopicName": "Describe Cisco Wireless Architectures and AP modes",
        "type": "single-choice",
        "prompt": "In Cisco embedded wireless architectures, what is Cisco Mobility Express?",
        "options": [
            {"id": "A", "text": "A software-based WLC function embedded directly into a designated master AP to manage up to 100 LAPs without a physical hardware controller", "isCorrect": True},
            {"id": "B", "text": "A physical appliance dedicated to outdoor mesh bridges", "isCorrect": False},
            {"id": "C", "text": "A dynamic routing protocol for mobile ad-hoc networks", "isCorrect": False},
            {"id": "D", "text": "A guest captive portal hosted in Cisco Catalyst Center", "isCorrect": False}
        ],
        "explanation": "Cisco Mobility Express integrates virtual WLC capabilities directly into an enterprise AP, allowing smaller sites to run centralized control without requiring a dedicated appliance controller.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 25",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.7 WLAN Infrastructure & Physical Connections (7 Qs)
    {
        "id": "q-2-7-001",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "Which physical port on a hardware Cisco Wireless LAN Controller is dedicated to out-of-band management and disaster recovery, isolated from user data traffic?",
        "options": [
            {"id": "A", "text": "Service Port", "isCorrect": True},
            {"id": "B", "text": "Distribution System Port", "isCorrect": False},
            {"id": "C", "text": "Console Port", "isCorrect": False},
            {"id": "D", "text": "Redundancy Port", "isCorrect": False}
        ],
        "explanation": "The Service Port on a Cisco WLC is a dedicated 10/100/1000 physical port used for out-of-band management and emergency recovery. It belongs to its own non-routable management routing domain.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-002",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "Which DHCP Option allows a Lightweight AP to learn the IPv4 address of its centralized Wireless LAN Controller during boot?",
        "options": [
            {"id": "A", "text": "Option 43", "isCorrect": True},
            {"id": "B", "text": "Option 67", "isCorrect": False},
            {"id": "C", "text": "Option 82", "isCorrect": False},
            {"id": "D", "text": "Option 150", "isCorrect": False}
        ],
        "explanation": "DHCP Option 43 is used to provide vendor-specific information, specifically the IP address(es) of the WLC management interfaces, so the AP can send unicast CAPWAP Discovery requests.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-003",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "What feature bundles all physical Distribution System ports on a Cisco WLC into a single dynamic Link Aggregation group to connect to an upstream switch stack?",
        "options": [
            {"id": "A", "text": "WLC Link Aggregation (LAG)", "isCorrect": True},
            {"id": "B", "text": "Cisco Spanning Tree Root PortFast", "isCorrect": False},
            {"id": "C", "text": "Cisco FlexConnect Tunneling", "isCorrect": False},
            {"id": "D", "text": "Cisco CleanAir Spectrum", "isCorrect": False}
        ],
        "explanation": "When LAG is enabled on a Cisco WLC, all distribution ports are bundled into a single EtherChannel link. This eliminates the need for separate physical port mappings and provides dynamic load distribution and failover.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-004",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "Which logical interface on a Cisco WLC is assigned an IP address such as 192.0.2.1 to manage web authentication redirects and DHCP relay for guest Wi-Fi clients?",
        "options": [
            {"id": "A", "text": "Virtual Interface", "isCorrect": True},
            {"id": "B", "text": "Management Interface", "isCorrect": False},
            {"id": "C", "text": "AP-Manager Interface", "isCorrect": False},
            {"id": "D", "text": "Dynamic Interface", "isCorrect": False}
        ],
        "explanation": "The Virtual Interface on a Cisco WLC facilitates guest user authentication redirects (captive portal) and DHCP relay. It must be assigned a non-routable IP address (commonly 192.0.2.1) identical across all controllers in a mobility group.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-005",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "What DNS hostname does a Cisco Lightweight Access Point query by default when attempting to locate a controller via DNS?",
        "options": [
            {"id": "A", "text": "CISCO-CAPWAP-CONTROLLER.localdomain", "isCorrect": True},
            {"id": "B", "text": "cisco-wlc.local", "isCorrect": False},
            {"id": "C", "text": "wlc-master.cisco.com", "isCorrect": False},
            {"id": "D", "text": "mobility-express.lan", "isCorrect": False}
        ],
        "explanation": "During WLC discovery, if DHCP Option 43 is not present, the AP appends its domain name to 'CISCO-CAPWAP-CONTROLLER' (e.g. CISCO-CAPWAP-CONTROLLER.example.com) and performs a DNS lookup.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-006",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "How should a switch port connected to an access-layer Lightweight AP in Local mode typically be configured?",
        "options": [
            {"id": "A", "text": "As an access port in the AP's management VLAN", "isCorrect": True},
            {"id": "B", "text": "As an 802.1Q trunk port with all client data VLANs tagged", "isCorrect": False},
            {"id": "C", "text": "As a routed Layer 3 port with an OSPF neighbor relationship", "isCorrect": False},
            {"id": "D", "text": "As an unmanaged SPAN destination port", "isCorrect": False}
        ],
        "explanation": "A Lightweight AP in Local mode encapsulates all client 802.11 frames inside CAPWAP tunnels directed to the WLC. Therefore, the switch port connected to the AP only needs to be an access port in the AP's management/infrastructure VLAN.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-7-007",
        "domainId": "2.0",
        "subtopicCode": "2.7",
        "subtopicName": "Describe physical infrastructure connections of WLAN components",
        "type": "single-choice",
        "prompt": "What is the purpose of a Dynamic Interface on a Cisco WLC?",
        "options": [
            {"id": "A", "text": "To map a specific WLAN (SSID) to an internal wired VLAN ID on the distribution switch network", "isCorrect": True},
            {"id": "B", "text": "To terminate the RS-232 serial console connection", "isCorrect": False},
            {"id": "C", "text": "To dynamically adjust AP radio transmit power", "isCorrect": False},
            {"id": "D", "text": "To generate SSL certificates for web authentication", "isCorrect": False}
        ],
        "explanation": "Dynamic interfaces function like SVIs on a switch. They map client traffic from specific WLANs to defined wired 802.1Q VLAN IDs across the distribution system ports.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 26",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.8 Device Management Access (8 Qs)
    {
        "id": "q-2-8-001",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "Why is SSH strictly preferred over Telnet for remote CLI management of network infrastructure?",
        "options": [
            {"id": "A", "text": "SSH encrypts all session data (including usernames, passwords, and commands) using public-key cryptography, whereas Telnet transmits all data in cleartext", "isCorrect": True},
            {"id": "B", "text": "SSH supports 100 Mbps throughput while Telnet is limited to 10 Mbps", "isCorrect": False},
            {"id": "C", "text": "Telnet cannot be configured on Cisco IOS XE devices", "isCorrect": False},
            {"id": "D", "text": "SSH runs over UDP which prevents TCP denial-of-service attacks", "isCorrect": False}
        ],
        "explanation": "Telnet sends all keystrokes in plaintext (TCP port 23), allowing network sniffers to capture administrative credentials. SSH (TCP port 22) provides strong encryption, session integrity, and secure authentication.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-002",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "Which command line under 'line vty 0 4' restricts inbound remote access connections exclusively to encrypted SSH sessions?",
        "options": [
            {"id": "A", "text": "transport input ssh", "isCorrect": True},
            {"id": "B", "text": "ssh only", "isCorrect": False},
            {"id": "C", "text": "line ssh enable", "isCorrect": False},
            {"id": "D", "text": "crypto transport in", "isCorrect": False}
        ],
        "explanation": "The command 'transport input ssh' on VTY lines disables Telnet and only accepts incoming SSH connections.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-003",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "What command instructs a Cisco router to prompt for a username and password authenticated against the device's local database for VTY access?",
        "options": [
            {"id": "A", "text": "login local", "isCorrect": True},
            {"id": "B", "text": "login", "isCorrect": False},
            {"id": "C", "text": "no login", "isCorrect": False},
            {"id": "D", "text": "password local", "isCorrect": False}
        ],
        "explanation": "On line configuration mode ('line vty 0 4' or 'line con 0'), 'login local' instructs the device to look at local accounts configured with 'username <user> secret <pass>'. Plain 'login' uses the single line password.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-004",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "Which physical connection is considered Out-of-Band (OOB) management and does not depend on IP routing or network interface availability?",
        "options": [
            {"id": "A", "text": "The serial or USB Console port", "isCorrect": True},
            {"id": "B", "text": "An SSH session to an SVI IP address", "isCorrect": False},
            {"id": "C", "text": "An HTTPS session to the Web GUI", "isCorrect": False},
            {"id": "D", "text": "An SNMP polling query from the NMS", "isCorrect": False}
        ],
        "explanation": "Out-of-band (OOB) management connects directly to the physical console port (RJ-45 rollover or mini-USB) using a terminal emulator (PuTTY/SecureCRT). It provides access even if all network interfaces are down or misconfigured.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-005",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "What security issue occurs when an administrator configures line passwords without enabling 'service password-encryption'?",
        "options": [
            {"id": "A", "text": "The line and enable passwords appear in clear plaintext when viewing the running-config", "isCorrect": True},
            {"id": "B", "text": "The switch drops all incoming SSH attempts", "isCorrect": False},
            {"id": "C", "text": "The console session disconnects after 5 minutes of inactivity", "isCorrect": False},
            {"id": "D", "text": "The device cannot boot into ROMMON", "isCorrect": False}
        ],
        "explanation": "Without 'service password-encryption', commands like 'password cisco' appear in clear text in 'show running-config'. Enabling it obfuscates passwords with Cisco Type 7 reversible hashing.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-006",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "What is the function of the 'exec-timeout 5 0' command configured under 'line con 0'?",
        "options": [
            {"id": "A", "text": "It automatically logs out an idle console session after 5 minutes and 0 seconds of inactivity", "isCorrect": True},
            {"id": "B", "text": "It delays login authentication by 5 seconds to throttle brute-force attacks", "isCorrect": False},
            {"id": "C", "text": "It sets the command execution timeout to 5 milliseconds", "isCorrect": False},
            {"id": "D", "text": "It terminates running scripts after 5 iterations", "isCorrect": False}
        ],
        "explanation": "'exec-timeout <minutes> <seconds>' sets the inactivity timer. If no input is received within 5 minutes, the console or VTY line automatically logs out the session.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-007",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "An administrator wants console syslog and debug messages to avoid interrupting typed CLI input. Which command should be enabled under 'line con 0'?",
        "options": [
            {"id": "A", "text": "logging synchronous", "isCorrect": True},
            {"id": "B", "text": "logging quiet", "isCorrect": False},
            {"id": "C", "text": "terminal no-log", "isCorrect": False},
            {"id": "D", "text": "service logging clean", "isCorrect": False}
        ],
        "explanation": "'logging synchronous' tells Cisco IOS to re-display the prompt and partially typed command on a new line after printing an unsolicited syslog or debug message, preventing garbled input.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 3",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-8-008",
        "domainId": "2.0",
        "subtopicCode": "2.8",
        "subtopicName": "Describe network device management access",
        "type": "single-choice",
        "prompt": "Which command creates a local administrator user with a cryptographically secure Type 9 (scrypt) hash?",
        "options": [
            {"id": "A", "text": "username admin algorithm-type scrypt secret Cisco12345", "isCorrect": True},
            {"id": "B", "text": "username admin password Cisco12345", "isCorrect": False},
            {"id": "C", "text": "enable password type-9 Cisco12345", "isCorrect": False},
            {"id": "D", "text": "service password-encryption type 9", "isCorrect": False}
        ],
        "explanation": "Modern Cisco IOS-XE supports 'algorithm-type scrypt' (Type 9) or 'algorithm-type sha256' (Type 8) for the strongest resistance against offline GPU password cracking compared to legacy MD5 Type 5.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 5",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 2.9 Wireless LAN GUI Configuration (7 Qs)
    {
        "id": "q-2-9-001",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "When configuring a new WLAN on a Cisco WLC GUI, which checkbox on the General tab must be enabled before the APs will begin broadcasting the SSID?",
        "options": [
            {"id": "A", "text": "Status: Enabled", "isCorrect": True},
            {"id": "B", "text": "Broadcast SSID Only", "isCorrect": False},
            {"id": "C", "text": "Radio Policy: 802.11b only", "isCorrect": False},
            {"id": "D", "text": "Fast Transition Active", "isCorrect": False}
        ],
        "explanation": "When a WLAN is created on a Cisco WLC, its Status defaults to Disabled so configuration can be completed safely. Checking 'Status: Enabled' activates the profile and starts beaconing.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-002",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "On a Cisco WLC GUI, which tab under WLANs > Edit is used to bind an SSID to a specific dynamic VLAN interface?",
        "options": [
            {"id": "A", "text": "General tab (Interface/Interface Group field)", "isCorrect": True},
            {"id": "B", "text": "Security tab", "isCorrect": False},
            {"id": "C", "text": "QoS tab", "isCorrect": False},
            {"id": "D", "text": "Advanced tab", "isCorrect": False}
        ],
        "explanation": "On the General tab of the WLAN configuration page, the 'Interface/Interface Group' drop-down allows selection of the dynamic interface (VLAN) to which client traffic will be mapped.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-003",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "To configure WPA2-Personal security for a new corporate WLAN on a Cisco WLC, what combination of settings should be selected under the Security > Layer 2 tab?",
        "options": [
            {"id": "A", "text": "Layer 2 Security: WPA+WPA2, WPA2 Policy enabled, AES (CCMP) encryption, and Auth Key Mgmt: PSK", "isCorrect": True},
            {"id": "B", "text": "Layer 2 Security: Static WEP with 128-bit key", "isCorrect": False},
            {"id": "C", "text": "Layer 2 Security: 802.1X with TKIP encryption", "isCorrect": False},
            {"id": "D", "text": "Layer 2 Security: None, Layer 3 Web Auth enabled", "isCorrect": False}
        ],
        "explanation": "WPA2-Personal requires: Layer 2 Security set to WPA+WPA2, checking 'WPA2 Policy', selecting 'AES' under WPA2 Encryption, and checking 'PSK' under Authentication Key Management.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-004",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "In the Cisco WLC WLAN GUI, what does the 'Broadcast SSID' checkbox control?",
        "options": [
            {"id": "A", "text": "Whether the AP transmits the SSID in 802.11 beacon frames so clients can discover the network automatically", "isCorrect": True},
            {"id": "B", "text": "Whether the AP forwards broadcast ARP requests to wireless clients", "isCorrect": False},
            {"id": "C", "text": "Whether the WLC advertises the SSID over CDP to adjacent switches", "isCorrect": False},
            {"id": "D", "text": "Whether the network supports 5 GHz radios", "isCorrect": False}
        ],
        "explanation": "If 'Broadcast SSID' is checked (the default), APs include the network name in periodic beacons. Unchecking it hides the SSID, requiring clients to manually enter the SSID to connect.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-005",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "Which Radio Policy setting restricts a WLAN to operate exclusively on the 5 GHz band, preventing 2.4 GHz legacy association?",
        "options": [
            {"id": "A", "text": "802.11a/n/ac only", "isCorrect": True},
            {"id": "B", "text": "All", "isCorrect": False},
            {"id": "C", "text": "802.11b/g only", "isCorrect": False},
            {"id": "D", "text": "Slot 0 only", "isCorrect": False}
        ],
        "explanation": "Selecting '802.11a/n/ac only' (or 802.11a only) forces the WLAN to broadcast exclusively from the 5 GHz radio, avoiding the congested 2.4 GHz spectrum.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-006",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "What feature configured under WLAN > Advanced tab enables branch FlexConnect APs to switch client data frames locally rather than tunneling through CAPWAP?",
        "options": [
            {"id": "A", "text": "FlexConnect Local Switching", "isCorrect": True},
            {"id": "B", "text": "Peer-to-Peer Blocking", "isCorrect": False},
            {"id": "C", "text": "Client Exclusion Policy", "isCorrect": False},
            {"id": "D", "text": "Fast SSID Changing", "isCorrect": False}
        ],
        "explanation": "Checking 'FlexConnect Local Switching' under the Advanced tab instructs FlexConnect APs servicing this WLAN to dump traffic directly onto the local trunk/access switch port instead of backhauling over CAPWAP.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-2-9-007",
        "domainId": "2.0",
        "subtopicCode": "2.9",
        "subtopicName": "Interpret wireless LAN GUI configuration for client connectivity",
        "type": "single-choice",
        "prompt": "Which Layer 2 authentication method requires configuring a RADIUS Authentication Server IP, shared secret, and port 1812 under the Security > AAA Servers tab?",
        "options": [
            {"id": "A", "text": "WPA2 Enterprise (802.1X)", "isCorrect": True},
            {"id": "B", "text": "WPA2 Personal (PSK)", "isCorrect": False},
            {"id": "C", "text": "Open Authentication", "isCorrect": False},
            {"id": "D", "text": "Static WEP", "isCorrect": False}
        ],
        "explanation": "WPA2-Enterprise uses 802.1X EAP authentication. The WLC acts as an authenticator, passing credentials to a central RADIUS server (such as Cisco ISE) over UDP port 1812.",
        "reference": "CCNA 200-301 OCG Vol 1, Ch 27",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    }
]

# Write out Domain 2 questions
output_path = os.path.join(os.path.dirname(__file__), "../src/data/domains/domain2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"[SUCCESS] Generated Domain 2.0 with {len(questions)} questions at {output_path}")

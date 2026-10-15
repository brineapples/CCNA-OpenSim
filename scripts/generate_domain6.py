"""
CCNA OpenSim - Domain 6.0 Automation and Programmability Generator (40 Questions)
Covers subtopics 6.1 through 6.7 based on Cisco CCNA 200-301 v1.1
"""

import json
import os

questions = [
    # 6.1 Automation Impact (5 Qs)
    {
        "id": "q-6-1-001",
        "domainId": "6.0",
        "subtopicCode": "6.1",
        "subtopicName": "Explain how automation impacts network management",
        "type": "single-choice",
        "prompt": "What operational challenge in traditional manual network management is eliminated by adopting declarative infrastructure automation?",
        "options": [
            {"id": "A", "text": "Configuration drift across devices caused by undocumented manual CLI modifications", "isCorrect": True},
            {"id": "B", "text": "The physical attenuation of optical fiber cabling", "isCorrect": False},
            {"id": "C", "text": "The necessity of assigning IP addresses to host interfaces", "isCorrect": False},
            {"id": "D", "text": "The requirement for 802.1Q encapsulation on trunk ports", "isCorrect": False}
        ],
        "explanation": "Configuration drift occurs over time when engineers make manual ad-hoc CLI changes on individual switches and routers without documenting or committing them to version control. Centralized declarative automation continuously enforces the intended state from a single source of truth.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 12",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-1-002",
        "domainId": "6.0",
        "subtopicCode": "6.1",
        "subtopicName": "Explain how automation impacts network management",
        "type": "single-choice",
        "prompt": "What is the primary benefit of maintaining network configurations in a Git version-control repository (Infrastructure as Code / NetDevOps)?",
        "options": [
            {"id": "A", "text": "Full auditability, peer-review change tracking, automated CI/CD pipeline testing, and instant rollbacks to known-good configurations", "isCorrect": True},
            {"id": "B", "text": "Elimination of dynamic routing protocols like OSPF", "isCorrect": False},
            {"id": "C", "text": "Direct conversion of copper ports to fiber transceivers", "isCorrect": False},
            {"id": "D", "text": "Doubling interface hardware switching bandwidth", "isCorrect": False}
        ],
        "explanation": "NetDevOps treats network configurations like software code. Storing configs in Git provides change tracking, branch merging with peer reviews, automated syntax validation via CI/CD, and fast rollbacks when an outage occurs.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 12",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-1-003",
        "domainId": "6.0",
        "subtopicCode": "6.1",
        "subtopicName": "Explain how automation impacts network management",
        "type": "single-choice",
        "prompt": "What is the key difference between imperative configuration and declarative configuration?",
        "options": [
            {"id": "A", "text": "Imperative specifies the exact step-by-step CLI commands to execute, while Declarative specifies the desired end state and leaves implementation details to the tool", "isCorrect": True},
            {"id": "B", "text": "Declarative requires typing commands in terminal console, while Imperative uses web dashboards", "isCorrect": False},
            {"id": "C", "text": "Imperative is idempotent, while Declarative is not idempotent", "isCorrect": False},
            {"id": "D", "text": "Declarative only applies to wireless networks", "isCorrect": False}
        ],
        "explanation": "Imperative tools (like custom Python CLI scripts) tell the device 'how' to do something through sequential commands. Declarative tools (like Terraform and Ansible state definitions) describe 'what' the desired state should look like, and the engine automatically calculates and applies the necessary changes.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 12",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-1-004",
        "domainId": "6.0",
        "subtopicCode": "6.1",
        "subtopicName": "Explain how automation impacts network management",
        "type": "single-choice",
        "prompt": "What does the property of 'idempotency' mean when executing automation playbooks or scripts on network devices?",
        "options": [
            {"id": "A", "text": "Running the automation script multiple times produces the exact same result without unintended changes or errors if the device is already in the target state", "isCorrect": True},
            {"id": "B", "text": "The script executes simultaneously on all devices in the autonomous system", "isCorrect": False},
            {"id": "C", "text": "The script automatically reboots the router after every task", "isCorrect": False},
            {"id": "D", "text": "All commands are translated to Python byte code", "isCorrect": False}
        ],
        "explanation": "Idempotency means that executing a task repeatedly yields the identical end state without redundant side effects. If an interface is already configured with VLAN 10, an idempotent automation tool will recognize this and skip applying changes.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 12",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-1-005",
        "domainId": "6.0",
        "subtopicCode": "6.1",
        "subtopicName": "Explain how automation impacts network management",
        "type": "single-choice",
        "prompt": "Which templating engine is commonly used in network automation workflows to generate Cisco IOS configuration files from data models?",
        "options": [
            {"id": "A", "text": "Jinja2", "isCorrect": True},
            {"id": "B", "text": "Node.js", "isCorrect": False},
            {"id": "C", "text": "Bash", "isCorrect": False},
            {"id": "D", "text": "SQL", "isCorrect": False}
        ],
        "explanation": "Jinja2 is the industry-standard Python templating engine used in Ansible, Nornir, and custom Python automation scripts to merge variables (YAML/JSON) into standardized configuration templates (.j2).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 12",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.2 Traditional vs Controller-Based (SDN) (6 Qs)
    {
        "id": "q-6-2-001",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "Which network plane is responsible for forwarding customer data packets from ingress to egress interfaces using hardware ASICs?",
        "options": [
            {"id": "A", "text": "Data Plane (Forwarding Plane)", "isCorrect": True},
            {"id": "B", "text": "Control Plane", "isCorrect": False},
            {"id": "C", "text": "Management Plane", "isCorrect": False},
            {"id": "D", "text": "Policy Plane", "isCorrect": False}
        ],
        "explanation": "The Data Plane (Forwarding Plane) performs wire-speed packet processing, MAC re-writes, ACL filtering, and hardware forwarding via TCAM and ASICs. The Control Plane runs routing protocols and builds tables; the Management Plane handles SSH/SNMP.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-2-002",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "How does controller-based networking (Software-Defined Networking / SDN) fundamentally reorganize the network architecture compared to traditional distributed networks?",
        "options": [
            {"id": "A", "text": "It centralizes the Control Plane intelligence into a software controller, while leaving the Data Plane distributed on the physical network forwarding devices", "isCorrect": True},
            {"id": "B", "text": "It eliminates the Data Plane and routes all traffic through the cloud", "isCorrect": False},
            {"id": "C", "text": "It moves Layer 2 switching into the Management Plane", "isCorrect": False},
            {"id": "D", "text": "It replaces Ethernet cabling with optical wireless lasers", "isCorrect": False}
        ],
        "explanation": "In traditional networking, every router and switch runs its own distributed control plane (OSPF, STP). SDN decouples the Control Plane from forwarding hardware and centralizes it in an SDN controller, which instructs devices what forwarding entries to install.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-2-003",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "Which task is an exclusive function of the Management Plane on a Cisco router?",
        "options": [
            {"id": "A", "text": "Authenticating an administrator attempting to log in via SSH or HTTPS", "isCorrect": True},
            {"id": "B", "text": "Exchanging OSPF Link-State Updates", "isCorrect": False},
            {"id": "C", "text": "Decrementing the IPv4 TTL and recomputing the header checksum", "isCorrect": False},
            {"id": "D", "text": "Switching frames using the CAM table", "isCorrect": False}
        ],
        "explanation": "Management Plane processes user interaction and monitoring: SSH, Telnet, HTTPS GUI, Syslog logging, and SNMP queries.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-2-004",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "Which Cisco enterprise SDN controller platform provides centralized fabric management, policy automation, and AI analytics for campus networks (formerly known as Cisco DNA Center)?",
        "options": [
            {"id": "A", "text": "Cisco Catalyst Center", "isCorrect": True},
            {"id": "B", "text": "Cisco Nexus Dashboard", "isCorrect": False},
            {"id": "C", "text": "Cisco Meraki Dashboard", "isCorrect": False},
            {"id": "D", "text": "Cisco Intersight", "isCorrect": False}
        ],
        "explanation": "Cisco Catalyst Center (formerly Cisco DNA Center) is the enterprise SDN controller for campus local area networks and wireless infrastructure, providing Cisco Software-Defined Access (SD-Access).",
        "reference": "CCNA 200-301 v1.1 Blueprint 6.2",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-2-005",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "Which controller platform manages Cisco SD-WAN fabrics, handling configuration templates, device onboarding, and centralized policy enforcement?",
        "options": [
            {"id": "A", "text": "Cisco Catalyst SD-WAN Manager (formerly vManage)", "isCorrect": True},
            {"id": "B", "text": "Cisco Catalyst SD-WAN Validator (vBond)", "isCorrect": False},
            {"id": "C", "text": "Cisco Catalyst SD-WAN Controller (vSmart)", "isCorrect": False},
            {"id": "D", "text": "Cisco WAN Edge (vEdge)", "isCorrect": False}
        ],
        "explanation": "In Cisco SD-WAN: Catalyst SD-WAN Manager (vManage) handles the Management Plane (GUI/configuration). Catalyst SD-WAN Controller (vSmart) handles the Control Plane (OMP routing). Catalyst SD-WAN Validator (vBond) handles orchestration/authentication.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-2-006",
        "domainId": "6.0",
        "subtopicCode": "6.2",
        "subtopicName": "Compare traditional networks with controller-based networking",
        "type": "single-choice",
        "prompt": "What is the primary operational advantage of centralized network control over traditional decentralized hop-by-hop configuration?",
        "options": [
            {"id": "A", "text": "Global visibility and instantaneous policy enforcement across thousands of network devices from a single interface", "isCorrect": True},
            {"id": "B", "text": "Elimination of physical cabling", "isCorrect": False},
            {"id": "C", "text": "Guaranteed 100% immunity to cyber attacks", "isCorrect": False},
            {"id": "D", "text": "Removal of IP subnetting requirements", "isCorrect": False}
        ],
        "explanation": "SDN controllers possess end-to-end network visibility. Instead of manually reconfiguring hundreds of switches one CLI at a time, an engineer defines an intent policy once on the controller, which automatically pushes configs across the entire fabric.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.3 Software-Defined Architecture (Overlay/Underlay/Fabric) (6 Qs)
    {
        "id": "q-6-3-001",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "In software-defined fabric terminology (such as Cisco SD-Access or SD-WAN), what is the 'Underlay'?",
        "options": [
            {"id": "A", "text": "The physical switches, routers, and cabling that run standard IP routing protocols to provide reliable transport reachability between fabric nodes", "isCorrect": True},
            {"id": "B", "text": "The virtual VXLAN tunnel headers encapsulating tenant frames", "isCorrect": False},
            {"id": "C", "text": "The REST API dashboard running in the cloud", "isCorrect": False},
            {"id": "D", "text": "The encrypted IPsec session on teleworker laptops", "isCorrect": False}
        ],
        "explanation": "The Underlay consists of physical hardware devices and links running an IGP (like IS-IS or OSPF) to provide IP packet transport between nodes. The Overlay is the logical virtual network encapsulated on top of the underlay.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-3-002",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "Which encapsulation protocol is used by Cisco SD-Access to create the virtual Overlay network, encapsulating original Layer 2 Ethernet frames inside UDP packets?",
        "options": [
            {"id": "A", "text": "VXLAN (Virtual Extensible LAN)", "isCorrect": True},
            {"id": "B", "text": "IPsec AH", "isCorrect": False},
            {"id": "C", "text": "802.1Q", "isCorrect": False},
            {"id": "D", "text": "ISL", "isCorrect": False}
        ],
        "explanation": "Cisco SD-Access uses VXLAN (UDP port 4789) as its data plane encapsulation mechanism to transport Layer 2 frames over an arbitrary Layer 3 routed underlay.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-3-003",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "What protocol constitutes the Control Plane of Cisco SD-Access to maintain an efficient database mapping endpoint IDs (EIDs) to routing locators (RLOCs)?",
        "options": [
            {"id": "A", "text": "LISP (Locator/ID Separation Protocol)", "isCorrect": True},
            {"id": "B", "text": "RIPv2", "isCorrect": False},
            {"id": "C", "text": "Spanning Tree Protocol", "isCorrect": False},
            {"id": "D", "text": "IGMPv3", "isCorrect": False}
        ],
        "explanation": "Cisco SD-Access separates location from identity using LISP (Locator/ID Separation Protocol) for its control plane. LISP maintains a map server/resolver that maps user endpoint IDs (EIDs) to the edge switch routing locators (RLOCs).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-3-004",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "In an SDN controller architecture, what is the role of a Northbound API?",
        "options": [
            {"id": "A", "text": "To allow external business applications, automation scripts, and orchestrators to communicate with and program the SDN controller", "isCorrect": True},
            {"id": "B", "text": "To allow the SDN controller to push configuration commands down to physical switches", "isCorrect": False},
            {"id": "C", "text": "To connect switches to endpoint PCs", "isCorrect": False},
            {"id": "D", "text": "To synchronize NTP time across WAN routers", "isCorrect": False}
        ],
        "explanation": "Northbound APIs (typically RESTful APIs) face upward toward applications, scripts, and monitoring portals. Southbound APIs (NETCONF, RESTCONF, gNMI, OpenFlow) face downward to manage forwarding hardware.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-3-005",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "Which protocol represents a standard model-driven Southbound API used by SDN controllers to configure network devices using XML-encoded messages over SSH?",
        "options": [
            {"id": "A", "text": "NETCONF (RFC 6241)", "isCorrect": True},
            {"id": "B", "text": "Telnet", "isCorrect": False},
            {"id": "C", "text": "TFTP", "isCorrect": False},
            {"id": "D", "text": "RADIUS", "isCorrect": False}
        ],
        "explanation": "NETCONF (Network Configuration Protocol) is a model-driven Southbound protocol that uses SSH transport and XML formatting with YANG data models to perform remote configuration operations.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-3-006",
        "domainId": "6.0",
        "subtopicCode": "6.3",
        "subtopicName": "Describe software-defined architecture",
        "type": "single-choice",
        "prompt": "Why must the Maximum Transmission Unit (MTU) of an underlay network be increased (e.g. to >= 1600 bytes) when deploying VXLAN overlay fabrics?",
        "options": [
            {"id": "A", "text": "To accommodate the 50-byte VXLAN encapsulation header without fragmenting packets", "isCorrect": True},
            {"id": "B", "text": "Because fiber optic cabling requires larger frames", "isCorrect": False},
            {"id": "C", "text": "To allow OSPF to exchange routing tables faster", "isCorrect": False},
            {"id": "D", "text": "To prevent Spanning Tree loops", "isCorrect": False}
        ],
        "explanation": "VXLAN prepends an outer Ethernet header, outer IP header, and UDP/VXLAN header totaling 50 bytes of overhead. Setting underlay MTU to at least 1600 bytes (Jumbo frames) prevents fragmentation of standard 1500-byte client frames.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 13",
        "difficulty": 3,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.4 AI & Machine Learning in Network Operations (6 Qs)
    {
        "id": "q-6-4-001",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "Under the CCNA v1.1 blueprint, which network operations capability exemplifies predictive AI in Cisco enterprise controller platforms such as Cisco Catalyst Center (formerly DNA Center)?",
        "options": [
            {"id": "A", "text": "Generating Jinja2 configuration templates for newly connected access switches", "isCorrect": False},
            {"id": "B", "text": "Analyzing historical Wi-Fi telemetry and baselines to forecast anomalies and AP capacity saturation before users experience degraded service", "isCorrect": True},
            {"id": "C", "text": "Converting natural language user prompts into CLI commands via an interactive chatbot", "isCorrect": False},
            {"id": "D", "text": "Executing Python scripts to auto-commit Git merges for network change windows", "isCorrect": False}
        ],
        "explanation": "Predictive AI models ingest historical and real-time telemetry (KPIs, RF interference, throughput) to establish behavioral baselines and forecast future performance degradation or failures (e.g. Wi-Fi capacity saturation) before they affect clients. Generative AI involves creating content or configuration code.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4 (AI & ML in Network Operations)",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-4-002",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "In modern AIOps (Artificial Intelligence for IT Operations), how is Generative AI applied to network troubleshooting?",
        "options": [
            {"id": "A", "text": "Synthesizing complex multi-device syslog/telemetry data into plain-language incident summaries and suggesting remediation steps via natural language chat interfaces", "isCorrect": True},
            {"id": "B", "text": "Executing hardware ASIC packet switching at line rate", "isCorrect": False},
            {"id": "C", "text": "Recalculating Spanning Tree port costs every second", "isCorrect": False},
            {"id": "D", "text": "Generating 802.1Q VLAN IDs automatically on endpoints", "isCorrect": False}
        ],
        "explanation": "Generative AI leverages Large Language Models (LLMs) to ingest logs, alerts, and topology configs, translating complex multi-vendor telemetry into clear, human-readable root-cause summaries and recommending corrective CLI scripts.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-4-003",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "Which Machine Learning technique is used by network assurance engines to discover unusual traffic spikes and abnormal device behavior without pre-programmed static threshold rules?",
        "options": [
            {"id": "A", "text": "Unsupervised anomaly detection (dynamic baselining)", "isCorrect": True},
            {"id": "B", "text": "Static access list filtering", "isCorrect": False},
            {"id": "C", "text": "Manual SNMP polling thresholds", "isCorrect": False},
            {"id": "D", "text": "Hardcoded syslog severity matching", "isCorrect": False}
        ],
        "explanation": "Unsupervised ML algorithms cluster normal behavior over time to create dynamic baselines. When a metric (e.g. DHCP latency or wireless roam time) deviates significantly from the learned pattern, it flags an anomaly without requiring manual static thresholds.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-4-004",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "In Cisco Catalyst Center AI Network Analytics, what does 'Peer Comparison' provide to an enterprise network engineer?",
        "options": [
            {"id": "A", "text": "Anonymous benchmarking comparing your wireless performance metrics against aggregated data from similar peer organizations in your industry and building type", "isCorrect": True},
            {"id": "B", "text": "Comparing BGP AS-Path lengths with external peers", "isCorrect": False},
            {"id": "C", "text": "Auditing user passwords against Active Directory peers", "isCorrect": False},
            {"id": "D", "text": "Validating STP root priorities between core switches", "isCorrect": False}
        ],
        "explanation": "Cisco Catalyst Center AI Analytics uses cloud-scale machine learning to compare a network's Wi-Fi KPIs (roam time, throughput, onboarding latency) against anonymous aggregated baselines from similar enterprise peers, helping engineers isolate internal issues from industry-wide trends.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-4-005",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "What is the primary role of Cisco ThousandEyes in modern AI-driven network observability?",
        "options": [
            {"id": "A", "text": "Providing end-to-end active path visualization and hop-by-hop performance telemetry across internal LANs, the public Internet, and cloud SaaS providers", "isCorrect": True},
            {"id": "B", "text": "Replacing local DNS servers with AI chatbots", "isCorrect": False},
            {"id": "C", "text": "Generating cryptographic RSA private keys for routers", "isCorrect": False},
            {"id": "D", "text": "Filtering Layer 2 Spanning Tree BPDUs", "isCorrect": False}
        ],
        "explanation": "Cisco ThousandEyes uses synthetic probes and active agent monitoring to map internet path performance, routing BGP anomalies, and application responsiveness, pinpointing exact outage locations across external ISPs and SaaS providers.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-4-006",
        "domainId": "6.0",
        "subtopicCode": "6.4",
        "subtopicName": "Explain AI (generative and predictive) and machine learning in network operations",
        "type": "single-choice",
        "prompt": "How does AI-driven Automated Root Cause Analysis (RCA) accelerate Mean Time to Resolution (MTTR) during major network incidents?",
        "options": [
            {"id": "A", "text": "By correlating hundreds of related alarms across switches, routers, and APs to identify the single underlying root fault, eliminating alarm fatigue", "isCorrect": True},
            {"id": "B", "text": "By shutting down all ports in the affected VLAN", "isCorrect": False},
            {"id": "C", "text": "By increasing interface clock speeds automatically", "isCorrect": False},
            {"id": "D", "text": "By suppressing all syslog messages to the security team", "isCorrect": False}
        ],
        "explanation": "When an outage occurs (e.g. an optical uplink failure), hundreds of downstream alarms fire simultaneously. Machine learning correlates timestamps, topology relationships, and dependency graphs to isolate the true root cause, filtering noise and drastically reducing MTTR.",
        "reference": "CCNA 200-301 v1.1 Topic 6.4",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.5 REST APIs (6 Qs)
    {
        "id": "q-6-5-001",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "drag-and-drop",
        "prompt": "Match each CRUD database operation to its corresponding standard HTTP REST verb.",
        "pairs": [
            {"target": "Create", "match": "POST"},
            {"target": "Read / Retrieve", "match": "GET"},
            {"target": "Update / Replace", "match": "PUT"},
            {"target": "Delete", "match": "DELETE"}
        ],
        "explanation": "REST APIs map CRUD operations directly to HTTP verbs: Create = POST, Read = GET, Update/Replace = PUT (or PATCH for partial updates), Delete = DELETE.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-5-002",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "single-choice",
        "prompt": "Which HTTP status code signifies that a client's REST API request was received and processed successfully, resulting in the creation of a new network resource?",
        "options": [
            {"id": "A", "text": "201 Created", "isCorrect": True},
            {"id": "B", "text": "200 OK", "isCorrect": False},
            {"id": "C", "text": "400 Bad Request", "isCorrect": False},
            {"id": "D", "text": "404 Not Found", "isCorrect": False}
        ],
        "explanation": "HTTP 201 Created indicates successful processing where a new resource (such as a newly configured VLAN or ACL) was created on the server.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-5-003",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "single-choice",
        "prompt": "What does HTTP status code 401 Unauthorized mean when interacting with a Cisco REST API?",
        "options": [
            {"id": "A", "text": "The request lacks valid authentication credentials (e.g. missing or expired API token)", "isCorrect": True},
            {"id": "B", "text": "The resource was successfully updated", "isCorrect": False},
            {"id": "C", "text": "The web server crashed due to an internal bug", "isCorrect": False},
            {"id": "D", "text": "The requested URL path does not exist", "isCorrect": False}
        ],
        "explanation": "HTTP 401 Unauthorized indicates that the client failed to provide valid authentication credentials. HTTP 403 Forbidden means credentials were valid, but the user account lacks permission to perform the action.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-5-004",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "single-choice",
        "prompt": "What architectural constraint of REST mandates that the server stores no client context between requests, requiring each client request to contain all necessary authentication and session information?",
        "options": [
            {"id": "A", "text": "Stateless", "isCorrect": True},
            {"id": "B", "text": "Layered System", "isCorrect": False},
            {"id": "C", "text": "Cacheable", "isCorrect": False},
            {"id": "D", "text": "Code-on-Demand", "isCorrect": False}
        ],
        "explanation": "The Stateless constraint requires each client request to be independent and self-contained with all information (such as authorization headers or tokens) necessary for the server to process it.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-5-005",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "single-choice",
        "prompt": "Which HTTP header is sent by a client to inform the REST API server that the client expects the response data to be formatted in JSON?",
        "options": [
            {"id": "A", "text": "Accept: application/json", "isCorrect": True},
            {"id": "B", "text": "Content-Type: text/plain", "isCorrect": False},
            {"id": "C", "text": "Host: cisco.com", "isCorrect": False},
            {"id": "D", "text": "User-Agent: Python-requests", "isCorrect": False}
        ],
        "explanation": "'Accept: application/json' tells the server what MIME type the client wants to receive in the response body. 'Content-Type: application/json' informs the server of the format of the data being uploaded in the request body.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-5-006",
        "domainId": "6.0",
        "subtopicCode": "6.5",
        "subtopicName": "Describe characteristics of REST-based APIs",
        "type": "single-choice",
        "prompt": "What HTTP method should be used when an engineer wants to update only a single field (such as an interface description) without replacing the entire interface object?",
        "options": [
            {"id": "A", "text": "PATCH", "isCorrect": True},
            {"id": "B", "text": "PUT", "isCorrect": False},
            {"id": "C", "text": "POST", "isCorrect": False},
            {"id": "D", "text": "GET", "isCorrect": False}
        ],
        "explanation": "PUT replaces the entire resource. PATCH applies partial modifications to a resource, updating only the specific attributes included in the payload.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.6 Ansible and Terraform (6 Qs)
    {
        "id": "q-6-6-001",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "Which statement accurately contrasts Terraform with Ansible in modern network infrastructure automation?",
        "options": [
            {"id": "A", "text": "Terraform is agent-based requiring a software daemon installed on Cisco IOS XE, whereas Ansible requires no agent.", "isCorrect": False},
            {"id": "B", "text": "Terraform uses declarative HashiCorp Configuration Language (HCL) and state files (.tfstate) to manage lifecycle, whereas Ansible primarily executes procedural/declarative YAML playbooks over SSH.", "isCorrect": True},
            {"id": "C", "text": "Ansible only manages cloud resources, while Terraform only configures on-premises Cisco switch ports.", "isCorrect": False},
            {"id": "D", "text": "Terraform does not support idempotency, whereas Ansible is strictly idempotent.", "isCorrect": False}
        ],
        "explanation": "Terraform uses declarative HCL (HashiCorp Configuration Language) and tracks deployed infrastructure through state files (.tfstate). Ansible is agentless, communicating primarily over SSH using YAML playbooks. Both are idempotent. (Terraform is a key addition to CCNA v1.1).",
        "reference": "CCNA 200-301 v1.1 Topic 6.6",
        "difficulty": 3,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-6-002",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "How does Ansible communicate with remote Cisco IOS and IOS XE switches to execute tasks without requiring an installed agent on the switch?",
        "options": [
            {"id": "A", "text": "Over standard SSH (or NETCONF/RESTCONF) using native Python network modules", "isCorrect": True},
            {"id": "B", "text": "Through an installed Docker container daemon running in switch ROM", "isCorrect": False},
            {"id": "C", "text": "Via unencrypted TFTP file pushes", "isCorrect": False},
            {"id": "D", "text": "By broadcasting SNMP community strings", "isCorrect": False}
        ],
        "explanation": "Ansible is agentless for network devices. It connects to Cisco switches and routers via SSH or NETCONF APIs, executes CLI commands or API calls, and parses the output directly from the control node.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 15",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-6-003",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "In Terraform workflow, which command displays the execution plan showing what infrastructure changes will be created, modified, or destroyed before making changes?",
        "options": [
            {"id": "A", "text": "terraform plan", "isCorrect": True},
            {"id": "B", "text": "terraform init", "isCorrect": False},
            {"id": "C", "text": "terraform apply", "isCorrect": False},
            {"id": "D", "text": "terraform validate", "isCorrect": False}
        ],
        "explanation": "'terraform plan' reads configuration files and compares them against the current state file, providing an execution plan showing proposed additions (+), changes (~), and destructions (-).",
        "reference": "CCNA 200-301 v1.1 Topic 6.6",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-6-004",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "What file in Ansible defines the list of managed target hostnames, IP addresses, and device groupings (e.g. [routers], [switches])?",
        "options": [
            {"id": "A", "text": "Inventory file (e.g. hosts or hosts.ini)", "isCorrect": True},
            {"id": "B", "text": "playbook.yml", "isCorrect": False},
            {"id": "C", "text": "ansible.cfg", "isCorrect": False},
            {"id": "D", "text": "id_rsa.pub", "isCorrect": False}
        ],
        "explanation": "The Ansible Inventory file (INI or YAML format) lists managed nodes, group hierarchies, and host-specific variables (IP addresses, port numbers, network OS types).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 15",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-6-005",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "What role does the 'terraform.tfstate' file perform in HashiCorp Terraform?",
        "options": [
            {"id": "A", "text": "It records the real-world state of all resources managed by Terraform to map real-world infrastructure to your configuration", "isCorrect": True},
            {"id": "B", "text": "It stores user login passwords in plaintext", "isCorrect": False},
            {"id": "C", "text": "It holds the binary executable code for Cisco IOS", "isCorrect": False},
            {"id": "D", "text": "It acts as a local DNS resolver cache", "isCorrect": False}
        ],
        "explanation": "Terraform uses the state file to store metadata and mappings between real-world infrastructure (cloud resources or Cisco ports) and the configuration definitions, enabling it to compute changes and detect drift.",
        "reference": "CCNA 200-301 v1.1 Topic 6.6",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-6-006",
        "domainId": "6.0",
        "subtopicCode": "6.6",
        "subtopicName": "Recognize capabilities of configuration management",
        "type": "single-choice",
        "prompt": "Which configuration management tools traditionally operate on an agent-based 'pull' architecture requiring a software daemon installed on every managed endpoint?",
        "options": [
            {"id": "A", "text": "Puppet and Chef", "isCorrect": True},
            {"id": "B", "text": "Ansible and Terraform", "isCorrect": False},
            {"id": "C", "text": "Python and Bash", "isCorrect": False},
            {"id": "D", "text": "Git and GitHub", "isCorrect": False}
        ],
        "explanation": "Puppet and Chef are traditionally agent-based tools operating on a pull model: a daemon on the managed device periodically contacts the central server to pull the catalog/recipe. Ansible and Terraform are agentless push tools.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 15",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },

    # 6.7 JSON Components (5 Qs)
    {
        "id": "q-6-7-001",
        "domainId": "6.0",
        "subtopicCode": "6.7",
        "subtopicName": "Recognize components of JSON-encoded data",
        "type": "single-choice",
        "prompt": "Which character pair is used to enclose a JSON object containing key-value pairs?",
        "options": [
            {"id": "A", "text": "Curly braces { }", "isCorrect": True},
            {"id": "B", "text": "Square brackets [ ]", "isCorrect": False},
            {"id": "C", "text": "Angle brackets < >", "isCorrect": False},
            {"id": "D", "text": "Parentheses ( )", "isCorrect": False}
        ],
        "explanation": "In JSON syntax: Curly braces { } enclose an Object (an unordered collection of key-value pairs). Square brackets [ ] enclose an Array (an ordered list of values).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 1,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-7-002",
        "domainId": "6.0",
        "subtopicCode": "6.7",
        "subtopicName": "Recognize components of JSON-encoded data",
        "type": "single-choice",
        "prompt": "Why is the following JSON snippet syntactically INVALID?\n{\n  'hostname': 'Router1',\n  'interfaces': ['Gi0/0', 'Gi0/1'],\n}",
        "options": [
            {"id": "A", "text": "Keys must use double quotation marks (\"), and trailing commas before closing braces are not permitted in JSON", "isCorrect": True},
            {"id": "B", "text": "JSON does not support arrays", "isCorrect": False},
            {"id": "C", "text": "Curly braces are reserved for YAML", "isCorrect": False},
            {"id": "D", "text": "Interface names cannot contain slashes", "isCorrect": False}
        ],
        "explanation": "JSON standards (RFC 8259) strictly enforce two rules violated here: 1. All strings and object keys MUST be enclosed in double quotes (\"), never single quotes. 2. Trailing commas after the final key-value pair or array element are illegal.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 2,
        "fidelityScore": 5.0,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-7-003",
        "domainId": "6.0",
        "subtopicCode": "6.7",
        "subtopicName": "Recognize components of JSON-encoded data",
        "type": "single-choice",
        "prompt": "What data type is represented by the value `true` (without quotes) in a JSON payload?",
        "options": [
            {"id": "A", "text": "Boolean", "isCorrect": True},
            {"id": "B", "text": "String", "isCorrect": False},
            {"id": "C", "text": "Null", "isCorrect": False},
            {"id": "D", "text": "Object", "isCorrect": False}
        ],
        "explanation": "JSON supports 6 fundamental data types: String (in double quotes), Number, Boolean (true or false in lowercase), Null (null), Object ({}), and Array ([]).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-7-004",
        "domainId": "6.0",
        "subtopicCode": "6.7",
        "subtopicName": "Recognize components of JSON-encoded data",
        "type": "single-choice",
        "prompt": "Given the JSON structure:\n{\n  'switch': {\n    'vlans': [10, 20, 30]\n  }\n}\nWhat is the 0-indexed value at position [1] of the 'vlans' array?",
        "options": [
            {"id": "A", "text": "20", "isCorrect": True},
            {"id": "B", "text": "10", "isCorrect": False},
            {"id": "C", "text": "30", "isCorrect": False},
            {"id": "D", "text": "null", "isCorrect": False}
        ],
        "explanation": "Arrays in JSON are ordered and 0-indexed. Index [0] is 10, index [1] is 20, and index [2] is 30.",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 1,
        "fidelityScore": 4.9,
        "contributor": "CCNA OpenSim Community"
    },
    {
        "id": "q-6-7-005",
        "domainId": "6.0",
        "subtopicCode": "6.7",
        "subtopicName": "Recognize components of JSON-encoded data",
        "type": "single-choice",
        "prompt": "Which character separates a key from its value inside a JSON object?",
        "options": [
            {"id": "A", "text": "Colon (:)", "isCorrect": True},
            {"id": "B", "text": "Comma (,)", "isCorrect": False},
            {"id": "C", "text": "Equals sign (=)", "isCorrect": False},
            {"id": "D", "text": "Arrow (->)", "isCorrect": False}
        ],
        "explanation": "In JSON objects, keys and values are paired using a colon (:), e.g. '\"port\": 80'. Multiple key-value pairs are separated from each other by commas (,).",
        "reference": "CCNA 200-301 OCG Vol 2, Ch 14",
        "difficulty": 1,
        "fidelityScore": 4.8,
        "contributor": "CCNA OpenSim Community"
    }
]

# Write out Domain 6 questions
output_path = os.path.join(os.path.dirname(__file__), "../src/data/domains/domain6.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"[SUCCESS] Generated Domain 6.0 with {len(questions)} questions at {output_path}")

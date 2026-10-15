/**
 * CCNA OpenSim - Automated Google Forms Question Audit & Review Generator
 * 
 * Purpose:
 * Generates official Peer-Review Google Forms populated with AI-generated draft questions
 * from the CCNA OpenSim 400-question bank. Community contributors review, rate, and fact-check
 * the pre-generated questions rather than submitting braindumps.
 * 
 * Instructions:
 * 1. Open https://script.new in your browser.
 * 2. Paste this entire script into the editor.
 * 3. Click "Run" (generateReviewForms).
 * 4. Grant Google permissions when prompted.
 * 
 * Result:
 * - Automatically creates the "CCNA OpenSim - Community Audit Sheet" Google Sheet.
 * - Builds 6 Domain Review Forms containing pre-loaded questions with answer keys,
 *   explanations, and technical review metrics (Fact Check, Fidelity 1-5, Difficulty 1-5, Edits).
 * - Links responses directly to the Master Google Sheet.
 */

function generateReviewForms() {
  Logger.log("🚀 Starting CCNA OpenSim Question Audit Form Generator...");

  // 1. Create the Master Tracking Sheet
  var ss = SpreadsheetApp.create("CCNA OpenSim - Community Review Results");
  var sheetId = ss.getId();
  var sheetUrl = ss.getUrl();
  Logger.log("✅ Created Master Audit Google Sheet: " + sheetUrl);

  var instructionsSheet = ss.getSheets()[0];
  instructionsSheet.setName("Review Summary & Pipeline");
  instructionsSheet.appendRow([
    "Domain", "Question ID", "Topic", "Factual Accuracy", "Avg Fidelity", "Avg Difficulty", "Recommended Edits", "Review Status"
  ]);

  // Sample curated questions per domain from the 400-question bank for audit clusters
  var sampleReviewData = {
    "1.0": {
      title: "1.0 Network Fundamentals - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering Subnetting, IPv6, Cabling, TCP/UDP, and Virtualization (VRFs).",
      questions: [
        {
          id: "q-1-1-001",
          topic: "1.1 Network Components (NGFW vs L3 Switch)",
          prompt: "An administrator is designing a campus network and needs a device that inspects traffic up to Layer 7, detects zero-day exploits, and decrypts TLS traffic for malware inspection. Which component is required?",
          options: "A) Layer 3 Distribution Switch\nB) Next-Generation Firewall (NGFW) [CORRECT]\nC) Wireless LAN Controller (WLC)\nD) Stateful Packet Inspection (SPI) Router",
          explanation: "Next-Generation Firewalls (NGFW) provide deep packet inspection up to Layer 7, integrated IPS, TLS/SSL decryption, and advanced threat intelligence, unlike traditional L3 switches or legacy SPI routers.",
          reference: "Cisco Press CCNA 200-301 Official Cert Guide Vol 1, Ch 1"
        },
        {
          id: "q-1-6-001",
          topic: "1.6 IPv4 Subnetting",
          prompt: "A network engineer must allocate a subnet from 172.16.0.0/16 that supports at least 58 usable host IP addresses while minimizing wasted address space. Which prefix length should be selected?",
          options: "A) /25\nB) /26 [CORRECT]\nC) /27\nD) /28",
          explanation: "To support 58 usable hosts: 2^6 - 2 = 62 usable hosts. A /26 provides 62 hosts, satisfying the requirement with minimal waste compared to /25 (126 hosts).",
          reference: "CCNA 200-301 OCG Vol 1, Ch 14"
        },
        {
          id: "q-1-12-001",
          topic: "1.12 Virtualization & VRFs (CCNA v1.1)",
          prompt: "A service provider needs to host two separate enterprise clients on a single physical core router. Both clients use overlapping IP address space (10.0.0.0/8). Which virtualization technology segments the routing table on the router?",
          options: "A) VLAN (Virtual Local Area Network)\nB) VRF (Virtual Routing and Forwarding) [CORRECT]\nC) Type 1 Hypervisor\nD) Docker Container Engine",
          explanation: "VRF functions like a virtual router inside a physical router, allowing multiple routing tables to coexist simultaneously with overlapping IP addresses.",
          reference: "CCNA 200-301 v1.1 Topic 1.12"
        }
      ]
    },
    "2.0": {
      title: "2.0 Network Access - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering VLANs, 802.1Q Trunks, EtherChannel (LACP), Rapid PVST+, and Wireless Architectures.",
      questions: [
        {
          id: "q-2-2-001",
          topic: "2.2 Interswitch Connectivity / DTP",
          prompt: "An administrator executes 'show interfaces trunk' on Switch A and observes that interface Gi0/1 is missing from the trunk list. Administrative mode is dynamic desirable, operational mode is static access. What is the root cause?",
          options: "A) The remote switch port is set to 'switchport mode access' [CORRECT]\nB) The native VLAN has not been changed from default VLAN 1\nC) The remote port is set to dynamic auto\nD) DTP negotiation failed because the remote side is configured as access [CORRECT]",
          explanation: "When an interface is set to dynamic desirable, DTP negotiates a trunk unless the neighbor is explicitly set to access mode ('switchport mode access').",
          reference: "CCNA 200-301 OCG Vol 1, Ch 9"
        },
        {
          id: "q-2-5-001",
          topic: "2.5 Rapid PVST+ Port States",
          prompt: "In an 802.1w Rapid Spanning Tree Protocol (RSTP / Rapid PVST+) topology, which port state corresponds to the legacy 802.1D Blocking, Listening, and Disabled states?",
          options: "A) Discarding [CORRECT]\nB) Learning\nC) Forwarding\nD) Alternate",
          explanation: "802.1w RSTP collapsed the 802.1D Disabled, Blocking, and Listening states into a single port state: 'Discarding'.",
          reference: "CCNA 200-301 OCG Vol 1, Ch 11"
        }
      ]
    },
    "3.0": {
      title: "3.0 IP Connectivity - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering Routing Logic, Longest Prefix Match, Static Routing, and OSPFv2 Single Area.",
      questions: [
        {
          id: "q-3-2-001",
          topic: "3.2 Forwarding Decisions (Longest Prefix Match)",
          prompt: "A router receives an IPv4 packet destined for 192.168.1.130. Its routing table contains:\nS 192.168.1.128/26 via 10.1.1.1\nO 192.168.1.128/27 via 10.2.2.2\nO 192.168.1.0/24 via 10.3.3.3\nThrough which next hop does the router forward the packet?",
          options: "A) 10.1.1.1 (/26 Static Route)\nB) 10.2.2.2 (/27 OSPF Route - Longest Prefix Match) [CORRECT]\nC) 10.3.3.3 (/24 OSPF Route)\nD) 10.4.4.4 (Default gateway)",
          explanation: "Router forwarding decisions ALWAYS evaluate Longest Prefix Match (most specific mask) first before considering Administrative Distance or Metric. /27 is longer than /26 or /24.",
          "reference": "CCNA 200-301 OCG Vol 1, Ch 16"
        },
        {
          id: "q-3-4-002",
          topic: "3.4 OSPFv2 Troubleshooting (ExStart State)",
          prompt: "Two directly connected routers running OSPFv2 are stuck in the 'EXSTART' state. What is the most likely cause?",
          options: "A) The maximum transmission unit (MTU) does not match between connecting interfaces [CORRECT]\nB) The OSPF Process IDs do not match\nC) The routers have different hostnames\nD) The dead timer is set to four times the hello timer",
          explanation: "In ExStart state, neighbors exchange DBD packets. If MTUs do not match and 'ip ospf mtu-ignore' is not configured, the adjacency freezes in ExStart.",
          "reference": "CCNA 200-301 OCG Vol 2, Ch 20"
        }
      ]
    },
    "4.0": {
      title: "4.0 IP Services - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering NAT/PAT, NTP, DHCP Relay, and QoS PHB.",
      questions: [
        {
          id: "q-4-1-001",
          topic: "4.1 Inside Source NAT (PAT / Overload)",
          prompt: "Which Cisco IOS command keyword enables Port Address Translation (PAT) when translating internal private addresses to a single public IP address assigned to interface GigabitEthernet 0/1?",
          options: "A) ip nat inside source list 1 interface gigabitethernet 0/1 overload [CORRECT]\nB) ip nat inside source list 1 interface gigabitethernet 0/1 pat-enable\nC) ip nat pool PUBLIC_POOL 203.0.113.1 203.0.113.1 netmask 255.255.255.252\nD) ip nat inside source static tcp 192.168.1.10 80 203.0.113.1 80",
          explanation: "The 'overload' keyword instructs Cisco IOS to track source L4 port numbers, enabling Port Address Translation (PAT).",
          "reference": "CCNA 200-301 OCG Vol 2, Ch 10"
        }
      ]
    },
    "5.0": {
      title: "5.0 Security Fundamentals - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering Standard/Extended ACLs, Layer 2 Security (DAI/DHCP Snooping/Port Security), and AAA.",
      questions: [
        {
          id: "q-5-7-001",
          topic: "5.7 Layer 2 Security (Dynamic ARP Inspection)",
          prompt: "Which Layer 2 security feature relies on the DHCP Snooping binding database to inspect ARP requests and replies, preventing ARP poisoning and MitM attacks?",
          options: "A) Port Security\nB) Dynamic ARP Inspection (DAI) [CORRECT]\nC) BPDU Guard\nD) Storm Control",
          explanation: "DAI intercepts ARP packets on untrusted ports and validates IP-to-MAC bindings against the DHCP Snooping database.",
          "reference": "CCNA 200-301 OCG Vol 2, Ch 7"
        }
      ]
    },
    "6.0": {
      title: "6.0 Automation and Programmability - Question Audit Form",
      description: "Audit and verify pre-generated CCNA v1.1 questions covering AI/ML in NetOps, Terraform vs Ansible, REST APIs, and JSON encoding.",
      questions: [
        {
          id: "q-6-4-001",
          topic: "6.4 AI & Machine Learning in NetOps (CCNA v1.1)",
          prompt: "Under the CCNA v1.1 blueprint, which network operations capability exemplifies predictive AI in enterprise controller platforms such as Cisco Catalyst Center?",
          options: "A) Generating Jinja2 configuration templates\nB) Analyzing historical Wi-Fi telemetry and baselines to forecast anomalies and AP capacity saturation before users experience degraded service [CORRECT]\nC) Converting natural language user prompts into CLI commands\nD) Executing Python scripts to auto-commit Git merges",
          explanation: "Predictive AI models analyze historical telemetry to establish baselines and forecast future degradation before user impact occurs.",
          "reference": "CCNA 200-301 v1.1 Topic 6.4"
        },
        {
          id: "q-6-6-001",
          topic: "6.6 Ansible vs Terraform (CCNA v1.1)",
          prompt: "Which statement accurately contrasts Terraform with Ansible in modern network infrastructure automation?",
          options: "A) Terraform is agent-based while Ansible requires no agent\nB) Terraform uses declarative HCL and state files (.tfstate) to manage lifecycle, whereas Ansible executes YAML playbooks over SSH [CORRECT]\nC) Ansible only manages cloud resources\nD) Terraform does not support idempotency",
          explanation: "Terraform uses declarative HCL with state files (.tfstate). Ansible is agentless over SSH using YAML playbooks.",
          "reference": "CCNA 200-301 v1.1 Topic 6.6"
        }
      ]
    }
  };

  var results = [];

  for (var domainId in sampleReviewData) {
    var domain = sampleReviewData[domainId];
    Logger.log("Creating Review Form for: " + domain.title);

    var form = FormApp.create("CCNA OpenSim: " + domain.title);
    form.setDescription(
      domain.description + "\n\n" +
      "INSTRUCTIONS FOR REVIEWERS:\n" +
      "Below are draft questions created for the CCNA OpenSim question bank.\n" +
      "Please evaluate each question for technical accuracy, exam closeness, and difficulty."
    );

    // Add questions as review sections
    domain.questions.forEach(function(q, index) {
      form.addPageBreakItem()
          .setTitle("Question " + (index + 1) + " of " + domain.questions.length + " [" + q.id + "]")
          .setHelpText("Topic: " + q.topic);

      // Section Display: The Draft Question
      var displayText = 
        "SCENARIO / PROMPT:\n" + q.prompt + "\n\n" +
        "OPTIONS:\n" + q.options + "\n\n" +
        "EXPLANATION:\n" + q.explanation + "\n\n" +
        "REFERENCE:\n" + q.reference;

      var viewItem = form.addSectionHeaderItem();
      viewItem.setTitle("Draft Question Details");
      viewItem.setHelpText(displayText);

      // Review Question 1: Accuracy
      form.addMultipleChoiceItem()
          .setTitle("[" + q.id + "] Is this question and explanation technically accurate according to Cisco standards?")
          .setChoiceValues(["Yes - Technically Accurate", "No - Contains Errors (explain below)"])
          .setRequired(true);

      // Review Question 2: Exam Closeness (Fidelity)
      form.addScaleItem()
          .setTitle("[" + q.id + "] Exam Closeness / Fidelity Rating:")
          .setHelpText("1 = Unrealistic / Outdated, 5 = Exact Cisco CCNA 200-301 Style")
          .setBounds(1, 5)
          .setLabels("Outdated", "Exact CCNA")
          .setRequired(true);

      // Review Question 3: Calibrated Difficulty
      form.addScaleItem()
          .setTitle("[" + q.id + "] Perceived Difficulty:")
          .setBounds(1, 5)
          .setLabels("1 - Easy", "5 - Very Hard")
          .setRequired(true);

      // Review Question 4: Suggested Corrections
      form.addParagraphTextItem()
          .setTitle("[" + q.id + "] Suggested Corrections, Wording Improvements, or Notes (Optional):")
          .setHelpText("If you answered 'No' above or have ideas to improve this question, please detail them here.");
    });

    // Link form responses directly to the Master Google Sheet
    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);

    results.push({
      domainId: domainId,
      title: domain.title,
      publishedUrl: form.getPublishedUrl(),
      editUrl: form.getEditUrl()
    });
  }

  Logger.log("\n=======================================================");
  Logger.log("🎉 ALL 6 QUESTION AUDIT FORMS CREATED AND LINKED!");
  Logger.log("Master Sheet URL: " + sheetUrl);
  Logger.log("=======================================================\n");

  results.forEach(function(r) {
    Logger.log("Domain " + r.domainId + " (" + r.title + "):");
    Logger.log("  Review Link for Community: " + r.publishedUrl);
    Logger.log("  Edit Link for Admin: " + r.editUrl + "\n");
  });
}

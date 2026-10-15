/**
 * CCNA OpenSim - Automated Google Forms & Master Sheet Generator
 * 
 * Instructions:
 * 1. Go to https://script.new in your browser.
 * 2. Delete any code in the editor, and paste this entire script.
 * 3. Click the "Run" button (triangle icon) at the top.
 * 4. Grant permissions when prompted.
 * 
 * Result:
 * - Automatically creates "CCNA OpenSim - Master Question Bank" Google Sheet.
 * - Programmatically builds all 6 Google Forms with all CCNA v1.1 subtopics.
 * - Automatically links all 6 forms to the Master Google Sheet.
 * - Logs all 6 live URLs in the Execution Log!
 */

function generateAllCCNAForms() {
  Logger.log("🚀 Starting CCNA OpenSim Form & Sheet Generation...");

  // 1. Create the Master Google Sheet
  const sheet = SpreadsheetApp.create("CCNA OpenSim - Master Question Bank");
  const sheetId = sheet.getId();
  const sheetUrl = sheet.getUrl();
  Logger.log("✅ Created Master Google Sheet: " + sheetUrl);

  // Setup initial template headers in Sheet1
  const defaultSheet = sheet.getSheets()[0];
  defaultSheet.setName("Review Queue & Instructions");
  defaultSheet.appendRow([
    "Review Status Options", "Approved", "Pending", "Needs Work", "Rejected"
  ]);
  defaultSheet.appendRow([
    "Instructions", 
    "Forms will automatically create tabs when responses arrive. Use the sync script in GitHub to pull rows marked 'Approved'."
  ]);

  // 2. Blueprint Domains & Subtopics (CCNA v1.1 Official)
  const domains = [
    {
      id: "1.0",
      title: "1.0 Network Fundamentals",
      subtopics: [
        "1.1 Role and function of network components (Routers, Switches, NGFW/IPS, APs, PoE)",
        "1.2 Network topology architectures (Two-tier, Three-tier, Spine-leaf, SOHO, Cloud)",
        "1.3 Cabling & physical interfaces (Single-mode, Multimode, Copper)",
        "1.4 Interface and cable issues (Collisions, errors, duplex/speed mismatch)",
        "1.5 Compare TCP to UDP",
        "1.6 Configure and verify IPv4 addressing and subnetting",
        "1.7 Describe private IPv4 addressing (RFC 1918)",
        "1.8/1.9 IPv6 addressing, prefixes, and types (Global, Link-Local, Unique Local, EUI-64)",
        "1.10 Verify IP parameters for Client OS",
        "1.11 Describe wireless principles (SSID, RF, Channels, Encryption)",
        "1.12 Explain virtualization fundamentals (Hypervisors, Containers, and VRFs)",
        "1.13 Describe switching concepts (MAC learning, aging, flooding, switching)"
      ]
    },
    {
      id: "2.0",
      title: "2.0 Network Access",
      subtopics: [
        "2.1 Configure and verify VLANs (Access ports data/voice, Default VLAN, InterVLAN)",
        "2.2 Configure and verify interswitch connectivity (Trunk ports, 802.1Q, Native VLAN)",
        "2.3 Configure and verify Layer 2 discovery protocols (CDP and LLDP)",
        "2.4 Configure and verify EtherChannel (Layer 2/Layer 3 LACP)",
        "2.5 Interpret basic operations of Rapid PVST+ (Root bridge, Root port, PortFast, BPDU Guard)",
        "2.6 Describe Cisco Wireless Architectures and AP modes",
        "2.7 Physical infrastructure connections of WLAN components (AP, WLC, LAG)",
        "2.8 Network device management access (Console, SSH, Telnet, AAA, Cloud-managed)",
        "2.9 Interpret wireless LAN GUI configuration for client connectivity"
      ]
    },
    {
      id: "3.0",
      title: "3.0 IP Connectivity",
      subtopics: [
        "3.1 Interpret components of routing table (Protocol codes, prefix, mask, next hop, AD, metric)",
        "3.2 Router forwarding decisions (Longest prefix match, AD, metric)",
        "3.3 Configure and verify IPv4 and IPv6 static routing (Default, network, host, floating static)",
        "3.4 Configure and verify single-area OSPFv2 (Adjacencies, DR/BDR, Router ID, point-to-point)",
        "3.5 First Hop Redundancy Protocols (HSRP concepts and operations)"
      ]
    },
    {
      id: "4.0",
      title: "4.0 IP Services",
      subtopics: [
        "4.1 Configure and verify inside source NAT using static and pools (PAT / Overload)",
        "4.2 Configure and verify NTP operating in client and server mode",
        "4.3 Explain role of DHCP and DNS within the network",
        "4.4 Explain function of SNMP in network operations (v2c vs v3, Traps vs Informs)",
        "4.5 Describe syslog features (Severity levels 0-7, facilities)",
        "4.6 Configure and verify DHCP client and relay (ip helper-address)",
        "4.7 Explain forwarding per-hop behavior for QoS (Classification, marking, queuing, policing)",
        "4.8 Configure network devices for remote access using SSH",
        "4.9 Describe capabilities and functions of TFTP/FTP in the network"
      ]
    },
    {
      id: "5.0",
      title: "5.0 Security Fundamentals",
      subtopics: [
        "5.1 Define key security concepts (Threats, vulnerabilities, exploits, mitigations)",
        "5.2 Describe security program elements (User awareness, physical access control)",
        "5.3 Configure and verify device access control using local passwords",
        "5.4 Password policy elements, complexity, and alternatives (MFA, certificates, biometrics)",
        "5.5 Describe IPsec remote access and site-to-site VPNs",
        "5.6 Configure and verify Access Control Lists (Standard and Extended ACLs)",
        "5.7 Configure and verify Layer 2 security features (DHCP snooping, DAI, port security)",
        "5.8 Compare Authentication, Authorization, and Accounting (AAA) concepts",
        "5.9 Describe wireless security protocols (WPA, WPA2, WPA3)",
        "5.10 Configure and verify WLAN within GUI using WPA2 PSK"
      ]
    },
    {
      id: "6.0",
      title: "6.0 Automation and Programmability",
      subtopics: [
        "6.1 Explain how automation impacts network management",
        "6.2 Compare traditional networks with controller-based networking (SDN)",
        "6.3 Describe software-defined architecture (Overlay, underlay, fabric, North/South APIs)",
        "6.4 Explain AI (generative and predictive) and machine learning in network operations",
        "6.5 Describe characteristics of REST-based APIs (CRUD, HTTP verbs, JSON encoding)",
        "6.6 Recognize capabilities of configuration management (Ansible and Terraform)",
        "6.7 Recognize components of JSON-encoded data"
      ]
    }
  ];

  const results = [];

  // 3. Programmatically build each form
  domains.forEach(function(d) {
    Logger.log("Creating Form for " + d.title + "...");
    const form = FormApp.create("CCNA OpenSim: " + d.title);
    
    form.setDescription(
      "Free & Open Source CCNA 200-301 v1.1 Question Bank.\n" +
      "Use this form to rate, verify, or submit questions for " + d.title + ".\n" +
      "Approved questions will be automatically synced into the live GitHub Pages practice exam."
    );

    // Question 1: Subtopic Cluster dropdown
    const subtopicItem = form.addListItem();
    subtopicItem.setTitle("Which topic cluster does this question belong to?")
                .setRequired(true)
                .setChoiceValues(d.subtopics);

    // Question 2: Question Type
    const typeItem = form.addMultipleChoiceItem();
    typeItem.setTitle("Question Type")
            .setRequired(true)
            .setChoiceValues([
              "Multiple Choice (Single Answer)",
              "Multiple Choice (Choose Two / Three)",
              "Drag and Drop (Matching)",
              "Simlet (Scenario with Cisco IOS CLI)"
            ]);

    // Question 3: Scenario / Prompt
    const promptItem = form.addParagraphTextItem();
    promptItem.setTitle("Question Scenario / Prompt")
              .setHelpText("Write the scenario or problem description clearly.")
              .setRequired(true);

    // Question 4: CLI Snippet (Optional)
    const cliItem = form.addParagraphTextItem();
    cliItem.setTitle("Cisco IOS CLI Snippet or Output (Optional)")
           .setHelpText("Paste router/switch show command output or configuration snippets if applicable.");

    // Options A, B, C, D, E
    form.addTextItem().setTitle("Option A").setRequired(true);
    form.addTextItem().setTitle("Option B").setRequired(true);
    form.addTextItem().setTitle("Option C").setRequired(true);
    form.addTextItem().setTitle("Option D").setRequired(true);
    form.addTextItem().setTitle("Option E (Optional)");

    // Correct Option(s)
    form.addTextItem()
        .setTitle("Correct Option(s)")
        .setHelpText("Enter the correct letter(s), e.g., 'B' or 'A, C'")
        .setRequired(true);

    // In-depth Explanation
    form.addParagraphTextItem()
        .setTitle("Explanation & Rationale")
        .setHelpText("Explain why the correct answer is right and why the distractors are wrong.")
        .setRequired(true);

    // Reference
    form.addTextItem()
        .setTitle("Cisco Reference / Source")
        .setHelpText("e.g. Cisco Press CCNA 200-301 OCG Vol 1, RFC, or Whitepaper.");

    // Rating: Exam Closeness
    form.addScaleItem()
        .setTitle("Exam Closeness (Fidelity)")
        .setHelpText("How closely does this match the phrasing, style, and scope of the real CCNA 200-301?")
        .setBounds(1, 5)
        .setLabels("Outdated / Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Rating: Difficulty
    form.addScaleItem()
        .setTitle("Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Contributor Credit
    form.addTextItem()
        .setTitle("Your Name or Discord / GitHub Handle (Optional)")
        .setHelpText("For contributor recognition in the question bank.");

    // Automatically link Form responses to the Master Spreadsheet!
    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);

    results.push({
      domainId: d.id,
      title: d.title,
      publishedUrl: form.getPublishedUrl(),
      editUrl: form.getEditUrl()
    });
  });

  Logger.log("\n=======================================================");
  Logger.log("🎉 ALL 6 FORMS AND MASTER SHEET CREATED SUCCESSFULLY!");
  Logger.log("Master Sheet URL: " + sheetUrl);
  Logger.log("=======================================================\n");

  results.forEach(function(r) {
    Logger.log("Domain " + r.domainId + " (" + r.title + "):");
    Logger.log("  Live Link: " + r.publishedUrl);
    Logger.log("  Edit Link: " + r.editUrl + "\n");
  });
}

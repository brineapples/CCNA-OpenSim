/**
 * CCNA OpenSim - Automated Question Review & Audit Form Generator
 * 
 * This script builds Google Forms that EMBED the AI-drafted questions
 * so contributors can read each scenario and rate/audit accuracy, fidelity, and difficulty.
 * 
 * Instructions:
 * 1. Go to https://script.new in your browser.
 * 2. Paste this entire script.
 * 3. Select 'generateReviewForms' and click Run (▶).
 */

function generateReviewForms() {
  Logger.log("🚀 Generating CCNA OpenSim Question Audit Forms...");

  const sheet = SpreadsheetApp.create("CCNA OpenSim - Community Review Results");
  const sheetId = sheet.getId();
  Logger.log("Created Review Results Sheet: " + sheet.getUrl());

  // Domain 1.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 1.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-1-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-1-1-001] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "An administrator is designing a campus network and needs a device that inspects traffic up to Layer 7, detects zero-day exploits, and decrypts TLS traffic for malware inspection. Which component is required?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) Layer 3 Distribution Switch\n  [CORRECT] B) Next-Generation Firewall (NGFW)\n  [ ] C) Wireless LAN Controller (WLC)\n  [ ] D) Stateful Packet Inspection (SPI) Router\n\n" +
          "EXPLANATION:\n" +
          "Next-Generation Firewalls (NGFW) provide deep packet inspection up to Layer 7 (Application layer), integrated Intrusion Prevention Systems (IPS), TLS/SSL decryption, and advanced threat intelligence, unlike traditional L3 switches or legacy SPI routers."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-1-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-1-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-1-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-1-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-1-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-1-1-002] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "Which network component is responsible for centralizing the management, RF configuration, and roaming policies of Lightweight Access Points (LAPs)?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) Next-Generation Intrusion Prevention System (NGIPS)\n  [CORRECT] B) Wireless LAN Controller (WLC)\n  [ ] C) Top-of-Rack Layer 2 Switch\n  [ ] D) Autonomous Access Point Bridge\n\n" +
          "EXPLANATION:\n" +
          "A Wireless LAN Controller (WLC) uses CAPWAP tunnels to manage Lightweight Access Points (LAPs) centrally, handling radio resource management (RRM), client authentication, mobility/roaming, and security policies."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-1-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-1-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-1-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-1-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-1-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-1-1-003] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "A network engineer needs to power an advanced PTZ IP surveillance camera requiring 25.5 Watts of DC power over Ethernet cabling. Which Power over Ethernet standard must the access switch support?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) IEEE 802.3af (PoE)\n  [CORRECT] B) IEEE 802.3at (PoE+)\n  [ ] C) IEEE 802.1Q\n  [ ] D) IEEE 802.3ad\n\n" +
          "EXPLANATION:\n" +
          "IEEE 802.3af provides up to 15.4W at the PSE (12.95W at PD). IEEE 802.3at (PoE+) provides up to 30W at the PSE (25.5W at PD). High-power devices such as PTZ cameras require 802.3at PoE+."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-1-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-1-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-1-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-1-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-1-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-1-1-004] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "What are two primary functions of a router in an enterprise enterprise campus network? (Choose two.)\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) Forwarding frames based on destination MAC addresses\n  [CORRECT] B) Creating separate broadcast domains for each connected interface\n  [CORRECT] C) Making forwarding decisions based on destination IP addresses\n  [ ] D) Supplying PoE power to unmanaged access switches\n  [ ] E) Managing STP root bridge election within a single VLAN\n\n" +
          "EXPLANATION:\n" +
          "Routers operate at Layer 3 (Network layer). They forward packets based on logical destination IP addresses using routing tables, and by default each router interface defines a separate broadcast domain."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-1-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-1-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-1-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-1-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-1-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-1-1-005] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "How does a Layer 3 switch achieve high-speed packet forwarding compared to a traditional software-based router?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) By executing routing decisions in general-purpose CPU threads\n  [CORRECT] B) By offloading route lookups and ACL processing to hardware ASICs and TCAM\n  [ ] C) By ignoring IP TTL decrementing during transmission\n  [ ] D) By converting all Layer 3 packets into ATM cells\n\n" +
          "EXPLANATION:\n" +
          "Layer 3 switches utilize specialized hardware Application-Specific Integrated Circuits (ASICs) and Ternary Content Addressable Memory (TCAM) to perform Cisco Express Forwarding (CEF) route lookups at line rate."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-1-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-1-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-1-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-1-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-1-1-006) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-1-1-006] Explain role and function of network components")
        .setHelpText(
          "SCENARIO:\n" +
          "Which network security appliance passively monitors traffic via a SPAN port to alert on malicious signatures without inline latency?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Intrusion Detection System (IDS)\n  [ ] B) Intrusion Prevention System (IPS)\n  [ ] C) Stateful Packet Inspection Firewall\n  [ ] D) Application Delivery Controller (ADC)\n\n" +
          "EXPLANATION:\n" +
          "An IDS (Intrusion Detection System) operates out-of-band by receiving a copy of traffic (e.g. through SPAN or network TAP), analyzing signatures and alerting administrators without introducing latency to live traffic."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-1-1-006]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-1-1-006]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-1-1-006]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-1-1-006]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 1.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  // Domain 2.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 2.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-2-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-2-1-001] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "An administrator wants to configure an access switch port connected to both an IP phone and an employee PC. The PC should be in VLAN 10 and the IP phone in VLAN 150. Which command sequence correctly configures the port?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) switchport mode access\n     switchport access vlan 10\n     switchport voice vlan 150\n  [ ] B) switchport mode trunk\n     switchport trunk allowed vlan 10,150\n  [ ] C) switchport mode multi\n     switchport data vlan 10\n     switchport aux vlan 150\n  [ ] D) switchport access vlan 10\n     switchport trunk native vlan 150\n\n" +
          "EXPLANATION:\n" +
          "To configure a port for both data and voice, configure 'switchport mode access', assign the PC's VLAN with 'switchport access vlan 10', and the IP phone's auxiliary VLAN with 'switchport voice vlan 150'. CDP/LLDP informs the phone of its voice VLAN so voice frames are tagged with 802.1Q while PC frames remain untagged."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-2-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-2-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-2-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-2-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-2-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-2-1-002] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "What is a characteristic of default VLAN 1 on Cisco Catalyst switches?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) It can be deleted or renamed to secure management traffic\n  [CORRECT] B) It cannot be deleted, cannot be renamed, and by default carries control plane protocols such as CDP and VTP\n  [ ] C) It cannot be routed across subinterfaces or SVIs\n  [ ] D) It is disabled automatically when VLAN 2 is created\n\n" +
          "EXPLANATION:\n" +
          "VLAN 1 is the factory default VLAN on all Cisco switches. All access ports default to VLAN 1. It cannot be deleted or renamed, and control protocols (CDP, PAgP, VTP) run on VLAN 1."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-2-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-2-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-2-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-2-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-2-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-2-1-003] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "Where are normal-range VLANs (VLAN IDs 1 to 1005) stored on a Cisco Catalyst switch when VTP transparent or client mode is running?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) In NVRAM within the startup-config file\n  [CORRECT] B) In Flash memory within the vlan.dat file\n  [ ] C) In DRAM volatile memory only\n  [ ] D) In BootROM firmware\n\n" +
          "EXPLANATION:\n" +
          "Normal-range VLAN configurations (IDs 1-1005) are saved in the 'vlan.dat' file stored in flash memory, which persists even if the startup-config is erased with 'write erase'. Extended VLANs (1006-4094) are saved in running-config/startup-config."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-2-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-2-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-2-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-2-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-2-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-2-1-004] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "An administrator executes the following router-on-a-stick configuration:  interface GigabitEthernet0/0.20  ip address 192.168.20.1 255.255.255.0  The router rejects the IP address command. What configuration step was omitted?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) The command 'encapsulation dot1Q 20' must be configured before assigning an IP address to a subinterface\n  [ ] B) The main interface GigabitEthernet0/0 must be configured as a trunk port first\n  [ ] C) Subinterface numbers must match the router's process ID\n  [ ] D) Subinterfaces only support IPv6 addresses\n\n" +
          "EXPLANATION:\n" +
          "In Cisco IOS router-on-a-stick configuration, a subinterface cannot receive an IP address until its 802.1Q encapsulation and VLAN tag are specified using 'encapsulation dot1Q <vlan-id>'."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-2-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-2-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-2-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-2-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-2-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-2-1-005] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "What command must be configured globally on a Cisco Catalyst Layer 3 switch before it will route traffic between Switched Virtual Interfaces (SVIs)?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) ip routing\n  [ ] B) router l3-switch\n  [ ] C) ip routing enable\n  [ ] D) switchport routing\n\n" +
          "EXPLANATION:\n" +
          "On Cisco Catalyst multi-layer switches, routing capability is disabled by default. The global configuration command 'ip routing' must be entered to activate the IPv4 routing engine between SVIs or routed ports."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-2-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-2-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-2-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-2-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-2-1-006) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-2-1-006] Configure and verify VLANs")
        .setHelpText(
          "SCENARIO:\n" +
          "An administrator creates 'interface Vlan 30' with IP address 10.0.30.1/24 on an access switch. However, 'show ip interface brief' indicates that interface Vlan 30 is 'down, line protocol is down'. What is the most common reason?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) No physical switch port in VLAN 30 is currently active (up/up) or VLAN 30 is not present in the VLAN database\n  [ ] B) The switchport trunk native vlan must be set to 30\n  [ ] C) The router-id has not been configured\n  [ ] D) SVI interfaces require an external DHCP server to come up\n\n" +
          "EXPLANATION:\n" +
          "An SVI (interface Vlan X) requires two conditions to reach up/up state: 1. VLAN X must exist in the switch's VLAN database and be active. 2. At least one physical access port in VLAN X, or a trunk port carrying VLAN X, must be up/up (and not STP blocked). This behavior is controlled by the autostate feature."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-2-1-006]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-2-1-006]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-2-1-006]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-2-1-006]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 2.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  // Domain 3.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 3.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-3-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-3-1-001] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "In the routing table entry 'O 10.2.2.0/24 [110/65] via 192.168.1.2, 00:14:23, GigabitEthernet0/1', what does the bracketed value '[110/65]' represent?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) 110 is the Administrative Distance, and 65 is the Metric (cost)\n  [ ] B) 110 is the Metric, and 65 is the Administrative Distance\n  [ ] C) 110 is the OSPF process ID, and 65 is the Autonomous System number\n  [ ] D) 110 is the hop count, and 65 is the interface MTU\n\n" +
          "EXPLANATION:\n" +
          "In Cisco IOS routing tables, bracketed entries are formatted as [Administrative Distance / Metric]. For OSPF routes, the default AD is 110, and 65 is the cumulative link cost (metric) to reach the destination subnet."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-3-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-3-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-3-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-3-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-3-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-3-1-002] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "What does the routing protocol code 'L' signify in a modern Cisco IOS routing table output?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) A Local route representing the exact /32 host IP address assigned to a local active router interface\n  [ ] B) A route learned via Link Layer Discovery Protocol\n  [ ] C) A Loopback interface route with infinite metric\n  [ ] D) A Longest Prefix Match candidate route\n\n" +
          "EXPLANATION:\n" +
          "In Cisco IOS 15.0+, connected interfaces generate both a 'C' (Connected subnet) entry and an 'L' (Local /32 host address) entry. The /32 local route allows the router's control plane to process packets destined directly to itself with maximum efficiency."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-3-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-3-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-3-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-3-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-3-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-3-1-003] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "Match each route source with its default Administrative Distance in Cisco IOS.\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  Target: Directly Connected -> Match: 0\n  Target: Static Route -> Match: 1\n  Target: eBGP -> Match: 20\n  Target: OSPF -> Match: 110\n\n" +
          "EXPLANATION:\n" +
          "Default Administrative Distances: Connected = 0, Static = 1, eBGP = 20, EIGRP internal = 90, OSPF = 110, IS-IS = 115, RIP = 120, iBGP = 200."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-3-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-3-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-3-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-3-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-3-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-3-1-004] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "What does the asterisk symbol (*) adjacent to a routing table entry denote (e.g. 'S* 0.0.0.0/0')?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) The route is a candidate default route\n  [ ] B) The route is currently inactive due to a missing next-hop\n  [ ] C) The route is an OSPF external type 2 route\n  [ ] D) The route has an administrative distance of 255\n\n" +
          "EXPLANATION:\n" +
          "An asterisk (*) indicates that the route is a candidate default route that can be chosen as the Gateway of Last Resort."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-3-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-3-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-3-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-3-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-3-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-3-1-005] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "Which routing protocol code indicates a route learned dynamically via EIGRP?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [ ] A) E\n  [CORRECT] B) D\n  [ ] C) I\n  [ ] D) G\n\n" +
          "EXPLANATION:\n" +
          "In Cisco IOS, EIGRP routes are represented by the letter 'D' (derived from the DUAL algorithm: Diffusing Update Algorithm). 'E' stands for legacy EGP."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-3-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-3-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-3-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-3-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-3-1-006) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-3-1-006] Interpret components of routing table")
        .setHelpText(
          "SCENARIO:\n" +
          "In 'show ip route', what is indicated when a route displays 'is directly connected, GigabitEthernet0/0' without a next-hop IP address?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) The router can send ARP requests directly on that interface because the destination subnet is locally attached\n  [ ] B) The route is unreachable because no gateway exists\n  [ ] C) The interface is operating in half-duplex mode\n  [ ] D) The route is being advertised by BGP\n\n" +
          "EXPLANATION:\n" +
          "Directly connected routes indicate that the network resides on the local link attached to that exit interface. For packets destined to hosts on that subnet, the router resolves the host's MAC address directly via ARP rather than forwarding to a next-hop router."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-3-1-006]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-3-1-006]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-3-1-006]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-3-1-006]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 3.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  // Domain 4.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 4.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-4-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-4-1-001] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "Which Cisco IOS command keyword enables Port Address Translation (PAT) when translating internal private addresses to a single public IP address assigned to interface GigabitEthernet 0/1?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) ip nat inside source list 1 interface gigabitethernet 0/1 overload\n  [ ] B) ip nat inside source list 1 interface gigabitethernet 0/1 pat-enable\n  [ ] C) ip nat pool PUBLIC_POOL 203.0.113.1 203.0.113.1 netmask 255.255.255.252\n  [ ] D) ip nat inside source static tcp 192.168.1.10 80 203.0.113.1 80\n\n" +
          "EXPLANATION:\n" +
          "The 'overload' keyword on the 'ip nat inside source list' command instructs the Cisco router to use Port Address Translation (PAT). PAT tracks unique source TCP/UDP port numbers so up to ~65,000 internal connections can share a single public IP."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-4-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-4-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-4-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-4-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-4-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-4-1-002] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "In Cisco NAT terminology, what is the 'Inside Local' address?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) The private IP address assigned to an internal host on the inside network\n  [ ] B) The globally routable public IP address representing an inside host to the outside world\n  [ ] C) The IP address of the destination server on the Internet\n  [ ] D) The IP address of the ISP gateway\n\n" +
          "EXPLANATION:\n" +
          "Cisco NAT definitions: 1. Inside Local = Private IP of inside host. 2. Inside Global = Public IP of inside host after translation. 3. Outside Global = Real public IP of external server. 4. Outside Local = External host's IP as viewed from the internal network."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-4-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-4-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-4-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-4-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-4-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-4-1-003] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "Which command configures a permanent 1-to-1 static NAT mapping for an internal web server at 192.168.1.50 to public IP 203.0.113.5?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) ip nat inside source static 192.168.1.50 203.0.113.5\n  [ ] B) ip nat outside source static 203.0.113.5 192.168.1.50\n  [ ] C) ip nat pool STATIC_WEB 192.168.1.50 203.0.113.5\n  [ ] D) ip nat map 192.168.1.50 to 203.0.113.5\n\n" +
          "EXPLANATION:\n" +
          "Static NAT uses the syntax 'ip nat inside source static <inside-local-ip> <inside-global-ip>'."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-4-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-4-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-4-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-4-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-4-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-4-1-004] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "What command clears all dynamic active NAT translations from the router's translation table during troubleshooting?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) clear ip nat translation *\n  [ ] B) no ip nat translations\n  [ ] C) reset ip nat table\n  [ ] D) flush nat translations all\n\n" +
          "EXPLANATION:\n" +
          "The privileged EXEC command 'clear ip nat translation *' removes all dynamic NAT sessions from the translation table. Note that static NAT entries are permanent and will not be cleared."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-4-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-4-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-4-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-4-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-4-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-4-1-005] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "An administrator configures NAT on Router 1 but notices that no translations occur. The ACL permits the traffic, and the NAT statement is correct. What configuration was most likely omitted?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) The commands 'ip nat inside' and 'ip nat outside' were not configured under the respective router interfaces\n  [ ] B) The router has not enabled OSPF routing\n  [ ] C) The router clock is not synchronized via NTP\n  [ ] D) NAT requires static routes with an Administrative Distance of 10\n\n" +
          "EXPLANATION:\n" +
          "NAT requires designating internal and external interfaces. Without 'ip nat inside' on the LAN-facing interface and 'ip nat outside' on the WAN-facing interface, the router will not intercept and translate passing packets."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-4-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-4-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-4-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-4-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-4-1-006) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-4-1-006] Configure and verify inside source NAT using static and pools")
        .setHelpText(
          "SCENARIO:\n" +
          "In the output of 'show ip nat translations', which column displays the public IP address and port allocated by the router to represent the internal client to external servers?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Inside global\n  [ ] B) Inside local\n  [ ] C) Outside local\n  [ ] D) Outside global\n\n" +
          "EXPLANATION:\n" +
          "The 'Inside global' column displays the public/routable IP address (and Layer 4 port number in PAT) assigned by the router to represent the internal device to the Internet."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-4-1-006]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-4-1-006]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-4-1-006]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-4-1-006]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 4.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  // Domain 5.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 5.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-5-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-5-1-001] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "In information security risk management, what is the definition of a 'vulnerability'?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) A flaw or weakness in system design, implementation, or software that can be exploited by an adversary\n  [ ] B) The potential danger that can exploit a system weakness\n  [ ] C) A piece of software code that takes advantage of a flaw\n  [ ] D) The financial cost of a regulatory fine\n\n" +
          "EXPLANATION:\n" +
          "In security terminology: Vulnerability = Weakness in a system. Threat = Potential danger. Exploit = Mechanism or code used to take advantage of a vulnerability. Risk = Probability of a threat exploiting a vulnerability multiplied by its impact."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-5-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-5-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-5-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-5-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-5-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-5-1-002] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "Which social engineering attack specifically targets high-profile C-level executives (such as CEOs or CFOs) to authorize fraudulent wire transfers or disclose intellectual property?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Whaling\n  [ ] B) Smishing\n  [ ] C) Vishing\n  [ ] D) Watering hole attack\n\n" +
          "EXPLANATION:\n" +
          "Whaling is a highly targeted form of spear-phishing aimed directly at senior executives, board members, or high-level government officials."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-5-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-5-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-5-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-5-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-5-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-5-1-003] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "What type of attack involves an attacker placing themselves logically between two communicating endpoints to secretly intercept, modify, or inject traffic without detection?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Man-in-the-Middle (MitM) attack\n  [ ] B) Smurf attack\n  [ ] C) SQL Injection\n  [ ] D) Buffer overflow attack\n\n" +
          "EXPLANATION:\n" +
          "A Man-in-the-Middle (MitM) attack (often performed via ARP spoofing or rogue DHCP servers on local LANs) intercepts traffic between two legitimate endpoints."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-5-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-5-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-5-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-5-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-5-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-5-1-004] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "Which component of the CIA triad ensures that data is protected from unauthorized modification, deletion, or tampering in transit and at rest?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Integrity\n  [ ] B) Confidentiality\n  [ ] C) Availability\n  [ ] D) Accounting\n\n" +
          "EXPLANATION:\n" +
          "The CIA Triad consists of: Confidentiality (data privacy/encryption), Integrity (guarantee that data has not been altered or corrupted, verified via cryptographic hashes/HMACs), and Availability (systems remain accessible to authorized users)."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-5-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-5-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-5-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-5-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-5-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-5-1-005] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "What security mechanism prevents an attacker from successfully forging the sender IP address in outbound packets from an enterprise campus?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Anti-spoofing filtering (BCP 38 / uRPF - Unicast Reverse Path Forwarding)\n  [ ] B) Port Security violation shutdown\n  [ ] C) DHCP Option 82 insertion\n  [ ] D) Dynamic ARP Inspection trust mode\n\n" +
          "EXPLANATION:\n" +
          "uRPF (Unicast Reverse Path Forwarding) and egress ACLs enforce BCP 38 anti-spoofing rules, dropping packets whose source IP address does not match a valid return route in the routing table."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-5-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-5-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-5-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-5-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-5-1-006) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-5-1-006] Define key security concepts")
        .setHelpText(
          "SCENARIO:\n" +
          "How does ransomware typically monetize an attack against an enterprise network?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) By encrypting organizational files and databases with strong symmetric/asymmetric keys and demanding cryptocurrency payment for the decryption key\n  [ ] B) By executing a SYN flood against the enterprise DNS server\n  [ ] C) By resetting Cisco switch passwords to factory defaults\n  [ ] D) By downgrading 10G fiber optics to 100M copper\n\n" +
          "EXPLANATION:\n" +
          "Ransomware is malicious software that encrypts user data, holding the private decryption key hostage until a ransom (typically in cryptocurrency) is paid."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-5-1-006]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-5-1-006]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-5-1-006]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-5-1-006]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 5.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  // Domain 6.0 Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain 6.0 Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");

    // --- Question 1 (q-6-1-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 1 of 6: [q-6-1-001] Explain how automation impacts network management")
        .setHelpText(
          "SCENARIO:\n" +
          "What operational challenge in traditional manual network management is eliminated by adopting declarative infrastructure automation?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Configuration drift across devices caused by undocumented manual CLI modifications\n  [ ] B) The physical attenuation of optical fiber cabling\n  [ ] C) The necessity of assigning IP addresses to host interfaces\n  [ ] D) The requirement for 802.1Q encapsulation on trunk ports\n\n" +
          "EXPLANATION:\n" +
          "Configuration drift occurs over time when engineers make manual ad-hoc CLI changes on individual switches and routers without documenting or committing them to version control. Centralized declarative automation continuously enforces the intended state from a single source of truth."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q1 [q-6-1-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q1 [q-6-1-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q1 [q-6-1-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q1 [q-6-1-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 2 (q-6-1-002) ---
    form.addSectionHeaderItem()
        .setTitle("Question 2 of 6: [q-6-1-002] Explain how automation impacts network management")
        .setHelpText(
          "SCENARIO:\n" +
          "What is the primary benefit of maintaining network configurations in a Git version-control repository (Infrastructure as Code / NetDevOps)?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Full auditability, peer-review change tracking, automated CI/CD pipeline testing, and instant rollbacks to known-good configurations\n  [ ] B) Elimination of dynamic routing protocols like OSPF\n  [ ] C) Direct conversion of copper ports to fiber transceivers\n  [ ] D) Doubling interface hardware switching bandwidth\n\n" +
          "EXPLANATION:\n" +
          "NetDevOps treats network configurations like software code. Storing configs in Git provides change tracking, branch merging with peer reviews, automated syntax validation via CI/CD, and fast rollbacks when an outage occurs."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q2 [q-6-1-002]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q2 [q-6-1-002]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q2 [q-6-1-002]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q2 [q-6-1-002]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 3 (q-6-1-003) ---
    form.addSectionHeaderItem()
        .setTitle("Question 3 of 6: [q-6-1-003] Explain how automation impacts network management")
        .setHelpText(
          "SCENARIO:\n" +
          "What is the key difference between imperative configuration and declarative configuration?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Imperative specifies the exact step-by-step CLI commands to execute, while Declarative specifies the desired end state and leaves implementation details to the tool\n  [ ] B) Declarative requires typing commands in terminal console, while Imperative uses web dashboards\n  [ ] C) Imperative is idempotent, while Declarative is not idempotent\n  [ ] D) Declarative only applies to wireless networks\n\n" +
          "EXPLANATION:\n" +
          "Imperative tools (like custom Python CLI scripts) tell the device 'how' to do something through sequential commands. Declarative tools (like Terraform and Ansible state definitions) describe 'what' the desired state should look like, and the engine automatically calculates and applies the necessary changes."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q3 [q-6-1-003]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q3 [q-6-1-003]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q3 [q-6-1-003]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q3 [q-6-1-003]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 4 (q-6-1-004) ---
    form.addSectionHeaderItem()
        .setTitle("Question 4 of 6: [q-6-1-004] Explain how automation impacts network management")
        .setHelpText(
          "SCENARIO:\n" +
          "What does the property of 'idempotency' mean when executing automation playbooks or scripts on network devices?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Running the automation script multiple times produces the exact same result without unintended changes or errors if the device is already in the target state\n  [ ] B) The script executes simultaneously on all devices in the autonomous system\n  [ ] C) The script automatically reboots the router after every task\n  [ ] D) All commands are translated to Python byte code\n\n" +
          "EXPLANATION:\n" +
          "Idempotency means that executing a task repeatedly yields the identical end state without redundant side effects. If an interface is already configured with VLAN 10, an idempotent automation tool will recognize this and skip applying changes."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q4 [q-6-1-004]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q4 [q-6-1-004]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q4 [q-6-1-004]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q4 [q-6-1-004]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 5 (q-6-1-005) ---
    form.addSectionHeaderItem()
        .setTitle("Question 5 of 6: [q-6-1-005] Explain how automation impacts network management")
        .setHelpText(
          "SCENARIO:\n" +
          "Which templating engine is commonly used in network automation workflows to generate Cisco IOS configuration files from data models?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Jinja2\n  [ ] B) Node.js\n  [ ] C) Bash\n  [ ] D) SQL\n\n" +
          "EXPLANATION:\n" +
          "Jinja2 is the industry-standard Python templating engine used in Ansible, Nornir, and custom Python automation scripts to merge variables (YAML/JSON) into standardized configuration templates (.j2)."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q5 [q-6-1-005]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q5 [q-6-1-005]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q5 [q-6-1-005]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q5 [q-6-1-005]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    // --- Question 6 (q-6-2-001) ---
    form.addSectionHeaderItem()
        .setTitle("Question 6 of 6: [q-6-2-001] Compare traditional networks with controller-based networking")
        .setHelpText(
          "SCENARIO:\n" +
          "Which network plane is responsible for forwarding customer data packets from ingress to egress interfaces using hardware ASICs?\n\n" +
          "CHOICES & CORRECT ANSWER:\n" +
          "  [CORRECT] A) Data Plane (Forwarding Plane)\n  [ ] B) Control Plane\n  [ ] C) Management Plane\n  [ ] D) Policy Plane\n\n" +
          "EXPLANATION:\n" +
          "The Data Plane (Forwarding Plane) performs wire-speed packet processing, MAC re-writes, ACL filtering, and hardware forwarding via TCAM and ASICs. The Control Plane runs routing protocols and builds tables; the Management Plane handles SSH/SNMP."
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q6 [q-6-2-001]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q6 [q-6-2-001]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q6 [q-6-2-001]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q6 [q-6-2-001]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");

    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain 6.0 Audit Form Published: " + form.getPublishedUrl());
  })();

  Logger.log("🎉 ALL AUDIT FORMS CREATED AND LINKED TO SPREADSHEET!");
}

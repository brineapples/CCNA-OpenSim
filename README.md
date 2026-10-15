# CCNA OpenSim 🌐

> **Free, 100% open-source Cisco Certified Network Associate (CCNA 200-301 v1.1) practice exam engine, simlets, and community peer-review platform.** Statically hosted with zero backend cost on GitHub Pages.

---

## 🎯 Features

- **Cisco CCNA v1.1 (2024) Aligned**: Proportional question weighting matching the official exam objectives:
  - `1.0 Network Fundamentals` (20%) — Includes VRFs
  - `2.0 Network Access` (20%) — VLANs, Trunking, EtherChannel, Rapid PVST+
  - `3.0 IP Connectivity` (25%) — Longest Prefix Match, Routing Tables, OSPFv2
  - `4.0 IP Services` (10%) — NAT/PAT, NTP, DHCP Relay, QoS
  - `5.0 Security Fundamentals` (15%) — ACLs, Port Security, Dynamic ARP Inspection
  - `6.0 Automation & Programmability` (10%) — REST APIs, JSON, Terraform, AI/ML in Cisco Catalyst Center
- **Interactive Cisco IOS Simlets**: Embedded mock CLI terminal supporting `show` commands, tab autocomplete, and command history.
- **Drag-and-Drop Matching**: Practice matching OSI layers, IPv6 prefixes, and administrative distances.
- **Pearson VUE-Style Exam Mode**: 120-minute countdown timer, pause option, review grid navigation, and question flagging.
- **Official-Style Score Report**: 300–1000 scaled score (825 pass threshold) with per-domain mastery percentages.
- **6-Domain Smart Forms Peer Review**: Contributor pipeline partitioned into 6 focused Google Forms so networkers can audit bite-sized 5-to-10 question clusters without fatigue.

---

## 🚀 Quick Start (Local Development)

```bash
# Clone the repository
git clone https://github.com/<your-username>/CCNA-OpenSim.git
cd CCNA-OpenSim

# Install dependencies
npm install

# Start local development server
npm run dev
```

Visit `http://localhost:5173` to test the exam engine.

---

## 🧪 Validating Questions

Ensure all questions in `src/data/questions.json` meet strict schema requirements (correct option count, valid domain ID, non-empty explanations):

```bash
npm run test:questions
```

---

## 📡 Syncing Questions from Google Sheets

Once your reviewers approve questions in the Master Google Sheet:

1. In Google Sheets: **File $\rightarrow$ Share $\rightarrow$ Publish to Web $\rightarrow$ Select CSV**.
2. Run the sync script:

```bash
npm run sync:questions <PUBLISHED_GOOGLE_SHEETS_CSV_URL>
```

The script automatically filters rows where `Review Status == 'Approved'`, validates syntax, updates `src/data/questions.json`, and rebuilds the static site.

---

## 📦 Deployment to GitHub Pages

This project is configured with GitHub Actions (`.github/workflows/deploy.yml`):
1. In your GitHub repository: Go to **Settings $\rightarrow$ Pages**.
2. Under **Build and deployment $\rightarrow$ Source**, select **GitHub Actions**.
3. Push to `main` branch — GitHub will automatically validate questions, build the Vite app, and publish it live!

---

## 🤝 Contributing

We welcome community contributions! Please review `CONTRIBUTING.md` or visit the **Peer Review Hub** inside the app to audit and submit new questions.

---

## ⚖️ License & Disclaimer

- Distributed under the **MIT License**.
- *Cisco, CCNA, and Cisco IOS are registered trademarks of Cisco Systems, Inc. CCNA OpenSim is an independent community study initiative and is neither affiliated with nor endorsed by Cisco Systems, Inc.*

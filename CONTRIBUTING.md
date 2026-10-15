# Contributing to CCNA OpenSim 🤝

Thank you for contributing to CCNA OpenSim! Our goal is to create a free, accurate, and high-quality 400-question practice bank for the Cisco CCNA 200-301 v1.1 certification.

---

## The Peer-Review Philosophy

We know most network engineers do not use Git on a daily basis. That is why our primary contribution mechanism is **Google Forms**:

1. **Pick a Domain**: Choose one of the 6 official CCNA domains you are currently studying.
2. **Select a Cluster**: Each form contains bite-sized clusters of 5–10 questions mapped directly to official Cisco blueprint topics (e.g. `3.4 OSPFv2`).
3. **Audit**:
   - **Exam Closeness (1–5)**: Does this reflect the style, terminology, and scope of the real 200-301 exam?
   - **Difficulty (1–5)**: 1 (Fundamental recall) to 5 (Complex scenario / troubleshooting).
   - **Technical Accuracy**: Are command outputs (e.g. `show ip route`) factually correct?
   - **Explanations**: Is there an in-depth explanation of why the correct answer is right and why distractors are wrong?

---

## Sourcing & Ethics Policy

> [!CAUTION]
> **No Braindumps or Live Exam Leaks**:
> Never submit actual proprietary Cisco exam questions or verbatim NDA-protected material. Cisco actively monitors and penalizes dumps.
>
> All questions must be **original scenario questions** inspired by the public CCNA 200-301 v1.1 blueprint objectives, RFC standards, and official Cisco documentation.

---

## Question Data Format (For GitHub PR Contributors)

If you prefer submitting questions via Pull Request, add your questions to `src/data/questions.json`:

```json
{
  "id": "q-3-4-002",
  "domainId": "3.0",
  "subtopicCode": "3.4",
  "subtopicName": "Configure and verify single area OSPFv2",
  "type": "single-choice",
  "prompt": "An engineer executes 'show ip ospf neighbor' on a multi-access broadcast segment...",
  "cliSnippet": "R1# show ip ospf neighbor\n...",
  "options": [
    { "id": "A", "text": "Option A text", "isCorrect": true },
    { "id": "B", "text": "Option B text", "isCorrect": false }
  ],
  "explanation": "Detailed rationale...",
  "reference": "Cisco Press CCNA 200-301 OCG Vol 2, Ch 19",
  "difficulty": 3,
  "fidelityScore": 5.0,
  "contributor": "@YourHandle"
}
```

Run schema validation before submitting:
```bash
npm run test:questions
```

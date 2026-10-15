import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questionsPath = path.resolve(__dirname, '../src/data/questions.json');
const outputPath = path.resolve(__dirname, './create_review_forms.gs');
const csvOutputPath = path.resolve(__dirname, '../data/master_question_bank_400.csv');

const questions = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));

console.log(`📦 Loaded ${questions.length} questions from questions.json`);

// 1. Export ALL 400 questions to master_question_bank_400.csv with pre-populated content & review columns
function escapeCsv(str) {
  if (!str) return '""';
  return `"${String(str).replace(/"/g, '""')}"`;
}

const csvHeaders = [
  'Question ID',
  'Domain ID',
  'Topic Code',
  'Topic Name',
  'Question Type',
  'Prompt / Scenario',
  'CLI Snippet',
  'Option A',
  'Option B',
  'Option C',
  'Option D',
  'Option E',
  'Correct Answer(s)',
  'Explanation',
  'Reference',
  'Difficulty (1-5)',
  'Fidelity Score (1-5)',
  'Review Status',
  'Reviewer Feedback / Corrections',
  'Audited By'
];

const csvRows = [csvHeaders.join(',')];

questions.forEach((q) => {
  const optA = q.options?.find(o => o.id === 'A')?.text || '';
  const optB = q.options?.find(o => o.id === 'B')?.text || '';
  const optC = q.options?.find(o => o.id === 'C')?.text || '';
  const optD = q.options?.find(o => o.id === 'D')?.text || '';
  const optE = q.options?.find(o => o.id === 'E')?.text || '';
  const correct = q.options?.filter(o => o.isCorrect).map(o => o.id).join(', ') || '';

  const row = [
    escapeCsv(q.id),
    escapeCsv(q.domainId),
    escapeCsv(q.subtopicCode),
    escapeCsv(q.subtopicName),
    escapeCsv(q.type),
    escapeCsv(q.prompt),
    escapeCsv(q.cliSnippet || ''),
    escapeCsv(optA),
    escapeCsv(optB),
    escapeCsv(optC),
    escapeCsv(optD),
    escapeCsv(optE),
    escapeCsv(correct),
    escapeCsv(q.explanation),
    escapeCsv(q.reference || ''),
    q.difficulty || 3,
    q.fidelityScore || 4.5,
    escapeCsv('Approved'), // Default status, can be audited
    escapeCsv(''),
    escapeCsv(q.contributor || 'AI Draft')
  ];
  csvRows.push(row.join(','));
});

fs.writeFileSync(csvOutputPath, csvRows.join('\n'));
console.log(`✅ Generated Master 400-Question Review CSV at: data/master_question_bank_400.csv`);

// 2. Generate Google Apps Script (create_review_forms.gs)
// Group questions by domain and sample representative clusters of 5-8 questions for focused audit forms
const domainGroups = {};
questions.forEach((q) => {
  if (!domainGroups[q.domainId]) domainGroups[q.domainId] = [];
  domainGroups[q.domainId].push(q);
});

let gsContent = `/**
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
`;

Object.keys(domainGroups).forEach((domainId) => {
  const dQuestions = domainGroups[domainId];
  // Select first 6 questions in each domain as the primary audit batch
  const auditSample = dQuestions.slice(0, 6);

  gsContent += `
  // Domain ${domainId} Review Form
  (function() {
    const form = FormApp.create("CCNA OpenSim: Domain ${domainId} Question Audit");
    form.setDescription(
      "Read through each AI-generated scenario question below. " +
      "For each question, evaluate its technical accuracy, exam fidelity, and difficulty."
    );

    const reviewerItem = form.addTextItem();
    reviewerItem.setTitle("Reviewer Name or Discord/GitHub Handle (Optional)");
`;

  auditSample.forEach((q, idx) => {
    let optText = '';
    if (q.options) {
      optText = q.options.map(o => {
        const safeText = (o.text || '').replace(/\r?\n/g, '\\n     ');
        return `  [${o.isCorrect ? 'CORRECT' : ' '}] ${o.id}) ${safeText}`;
      }).join('\\n');
    } else if (q.pairs) {
      optText = q.pairs.map(p => {
        const safeTarget = String(p.target || '').replace(/\r?\n/g, ' ');
        const safeMatch = String(p.match || '').replace(/\r?\n/g, ' ');
        return `  Target: ${safeTarget} -> Match: ${safeMatch}`;
      }).join('\\n');
    }

    const snippetText = q.cliSnippet ? `\\n\\nCLI Output:\\n${q.cliSnippet.replace(/\n/g, '\\n')}` : '';
    const safePrompt = q.prompt.replace(/\n/g, ' ').replace(/"/g, '\\"');
    const safeExp = q.explanation.replace(/\n/g, ' ').replace(/"/g, '\\"');

    gsContent += `
    // --- Question ${idx + 1} (${q.id}) ---
    form.addSectionHeaderItem()
        .setTitle("Question ${idx + 1} of ${auditSample.length}: [${q.id}] ${q.subtopicName}")
        .setHelpText(
          "SCENARIO:\\n" +
          "${safePrompt}${snippetText}\\n\\n" +
          "CHOICES & CORRECT ANSWER:\\n" +
          "${optText.replace(/"/g, '\\"')}\\n\\n" +
          "EXPLANATION:\\n" +
          "${safeExp}"
        );

    // Review Metric 1: Accuracy
    form.addMultipleChoiceItem()
        .setTitle("Q${idx + 1} [${q.id}]: Is this question and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording / typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // Review Metric 2: Fidelity
    form.addScaleItem()
        .setTitle("Q${idx + 1} [${q.id}]: Exam Closeness / Fidelity")
        .setHelpText("1: Unrealistic/Outdated, 5: Exact CCNA 200-301 style")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // Review Metric 3: Difficulty
    form.addScaleItem()
        .setTitle("Q${idx + 1} [${q.id}]: Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // Review Metric 4: Feedback
    form.addParagraphTextItem()
        .setTitle("Q${idx + 1} [${q.id}]: Suggested Corrections / Comments")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");
`;
  });

  gsContent += `
    form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId);
    Logger.log("Domain ${domainId} Audit Form Published: " + form.getPublishedUrl());
  })();
`;
});

gsContent += `
  Logger.log("🎉 ALL AUDIT FORMS CREATED AND LINKED TO SPREADSHEET!");
}
`;

fs.writeFileSync(outputPath, gsContent);
console.log(`✅ Generated Google Apps Script at: scripts/create_review_forms.gs`);

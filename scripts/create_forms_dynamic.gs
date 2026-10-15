/**
 * CCNA OpenSim - Dynamic Question Audit Form Generator (Method 2)
 * 
 * Fetches all 400 AI-generated questions directly from GitHub:
 * https://raw.githubusercontent.com/brineapples/CCNA-OpenSim/main/src/data/questions.json
 * 
 * Instructions:
 * 1. Go to https://script.new
 * 2. Paste this entire file.
 * 3. Make sure the dropdown at the top says 'buildDomain1Form' (or 'buildAllForms').
 * 4. Click the Run (▶) button.
 * 5. Open the NEW URL printed in the Execution Log to see all 80 questions!
 */

const GITHUB_RAW_URL = "https://raw.githubusercontent.com/brineapples/CCNA-OpenSim/main/src/data/questions.json";

// ==========================================
// 🚀 RUN THESE FUNCTIONS FROM THE DROPDOWN:
// ==========================================

// Build Form 1 (All 80 Network Fundamentals questions)
function buildDomain1Form() { 
  return buildFormForDomain("1.0", "Network Fundamentals"); 
}

// Build Form 2 (All 80 Network Access questions)
function buildDomain2Form() { 
  return buildFormForDomain("2.0", "Network Access"); 
}

// Build Form 3 (All 100 IP Connectivity questions)
function buildDomain3Form() { 
  return buildFormForDomain("3.0", "IP Connectivity"); 
}

// Build Form 4 (All 40 IP Services questions)
function buildDomain4Form() { 
  return buildFormForDomain("4.0", "IP Services"); 
}

// Build Form 5 (All 60 Security Fundamentals questions)
function buildDomain5Form() { 
  return buildFormForDomain("5.0", "Security Fundamentals"); 
}

// Build Form 6 (All 40 Automation and Programmability questions)
function buildDomain6Form() { 
  return buildFormForDomain("6.0", "Automation and Programmability"); 
}

// Master function to build all 6 forms
function buildAllForms() {
  const sheet = getOrCreateMasterSheet();
  Logger.log("Master Sheet URL: " + sheet.getUrl());
  
  buildDomain1Form();
  buildDomain2Form();
  buildDomain3Form();
  buildDomain4Form();
  buildDomain5Form();
  buildDomain6Form();
  
  Logger.log("🎉 ALL 6 FORMS GENERATED FROM GITHUB REPO!");
}

// ==========================================
// CORE BUILDER & FETCH LOGIC
// ==========================================

function fetchQuestionsFromGitHub() {
  Logger.log("📡 Fetching questions from GitHub: " + GITHUB_RAW_URL);
  const response = UrlFetchApp.fetch(GITHUB_RAW_URL);
  const jsonText = response.getContentText();
  const questions = JSON.parse(jsonText);
  Logger.log("✅ Successfully downloaded " + questions.length + " questions from GitHub!");
  return questions;
}

function getOrCreateMasterSheet() {
  const properties = PropertiesService.getScriptProperties();
  let sheetId = properties.getProperty("MASTER_SHEET_ID");
  
  if (sheetId) {
    try {
      return SpreadsheetApp.openById(sheetId);
    } catch(e) {
      Logger.log("Stored sheet ID not found, creating a new sheet...");
    }
  }

  const newSheet = SpreadsheetApp.create("CCNA OpenSim - Community Review Results");
  properties.setProperty("MASTER_SHEET_ID", newSheet.getId());
  Logger.log("📊 Created Master Review Sheet: " + newSheet.getUrl());
  return newSheet;
}

function buildFormForDomain(domainId, domainTitle) {
  Logger.log("🔨 Building Audit Form for Domain " + domainId + " (" + domainTitle + ")...");
  
  const allQuestions = fetchQuestionsFromGitHub();
  const domainQuestions = allQuestions.filter(function(q) {
    return q.domainId === domainId;
  });

  Logger.log("Found " + domainQuestions.length + " questions for Domain " + domainId + ". Building form now...");

  const sheet = getOrCreateMasterSheet();
  const form = FormApp.create("CCNA OpenSim: Domain " + domainId + " (" + domainTitle + ") Audit");
  
  form.setDescription(
    "CCNA 200-301 v1.1 Community Peer Review\\n" +
    "Below are the " + domainQuestions.length + " AI-drafted questions for " + domainTitle + ".\\n" +
    "For each question, evaluate its technical accuracy, exam closeness, and difficulty.\\n" +
    "Questions are organized into topic sections below."
  );

  form.addTextItem()
      .setTitle("Reviewer Name or Discord / GitHub Handle (Optional)")
      .setHelpText("Enter your handle to receive credit in the repository.");

  // Group questions by subtopicCode to create clean page sections
  let currentSubtopic = "";

  domainQuestions.forEach(function(q, index) {
    if (q.subtopicCode !== currentSubtopic) {
      currentSubtopic = q.subtopicCode;
      form.addPageBreakItem()
          .setTitle("Topic " + q.subtopicCode + ": " + q.subtopicName)
          .setHelpText("Section " + (index + 1) + " of " + domainQuestions.length);
    }

    // Format choices
    let choicesText = "";
    if (q.options) {
      choicesText = q.options.map(function(o) {
        return "  [" + (o.isCorrect ? "CORRECT" : " ") + "] " + o.id + ") " + o.text;
      }).join("\\n");
    } else if (q.pairs) {
      choicesText = q.pairs.map(function(p) {
        return "  Target: " + p.target + " ---> Match: " + p.match;
      }).join("\\n");
    }

    const snippetText = q.cliSnippet ? "\\n\\nCLI Command Output:\\n" + q.cliSnippet : "";

    // 1. Question Card (Section Header)
    form.addSectionHeaderItem()
        .setTitle("Question " + (index + 1) + " [" + q.id + "]")
        .setHelpText(
          "SCENARIO:\\n" + q.prompt + snippetText + "\\n\\n" +
          "CHOICES & ANSWER:\\n" + choicesText + "\\n\\n" +
          "OFFICIAL EXPLANATION:\\n" + q.explanation +
          (q.reference ? "\\n\\nReference: " + q.reference : "")
        );

    // 2. Accuracy Check
    form.addMultipleChoiceItem()
        .setTitle("[" + q.id + "] Is this question, answer, and explanation technically accurate?")
        .setRequired(true)
        .setChoiceValues([
          "Yes - 100% accurate",
          "Minor wording or typo issue",
          "Inaccurate - wrong answer or flawed explanation"
        ]);

    // 3. Exam Fidelity (1-5)
    form.addScaleItem()
        .setTitle("[" + q.id + "] Exam Closeness / Fidelity")
        .setHelpText("How closely does this match real Cisco CCNA 200-301 question style?")
        .setBounds(1, 5)
        .setLabels("Unrealistic / Out of Scope", "Exact CCNA Style")
        .setRequired(true);

    // 4. Difficulty (1-5)
    form.addScaleItem()
        .setTitle("[" + q.id + "] Calibrated Difficulty")
        .setBounds(1, 5)
        .setLabels("1 - Easy Recall", "5 - Complex Troubleshooting")
        .setRequired(true);

    // 5. Feedback / Edits
    form.addParagraphTextItem()
        .setTitle("[" + q.id + "] Corrections / Suggestions for this Question")
        .setHelpText("Provide corrections to CLI output, choices, or explanation if needed.");
  });

  // Link form responses to the Master Sheet
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  const pubUrl = form.getPublishedUrl();
  Logger.log("\\n=======================================================");
  Logger.log("🎉 Domain " + domainId + " Form Ready with " + domainQuestions.length + " questions!");
  Logger.log("👉 OPEN THIS NEW URL TO SEE THE QUESTIONS:");
  Logger.log(pubUrl);
  Logger.log("=======================================================\\n");

  return pubUrl;
}

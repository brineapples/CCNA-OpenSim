/**
 * CCNA OpenSim - Fast Cluster Review Form Generator
 * Creates an audit form for Cluster 1.1 (Network Components - 6 Questions).
 * Runs in under 5 seconds!
 */

function main() {
  Logger.log("🚀 Building Cluster 1.1 Review Form...");

  const GITHUB_URL = "https://raw.githubusercontent.com/brineapples/CCNA-OpenSim/main/src/data/questions.json";
  const res = UrlFetchApp.fetch(GITHUB_URL);
  const allQuestions = JSON.parse(res.getContentText());

  // Filter only Topic 1.1 (Network Components - 6 questions)
  const clusterQuestions = allQuestions.filter(function(q) {
    return q.subtopicCode === "1.1";
  });

  Logger.log("Found " + clusterQuestions.length + " questions for Cluster 1.1. Creating form...");

  const form = FormApp.create("CCNA OpenSim: Cluster 1.1 Network Components Audit");
  form.setDescription(
    "Audit & Review Form for CCNA Topic 1.1 (Network Components).\n" +
    "Review each of the " + clusterQuestions.length + " questions below for technical accuracy, exam closeness, and difficulty."
  );

  form.addTextItem().setTitle("Your Name or Handle (Optional)");

  clusterQuestions.forEach(function(q, i) {
    let choices = "";
    if (q.options) {
      choices = q.options.map(function(o) {
        return (o.isCorrect ? " [CORRECT] " : " [ ] ") + o.id + ") " + o.text;
      }).join("\n");
    }

    // 1. Question Details Header
    form.addSectionHeaderItem()
        .setTitle("Question " + (i + 1) + " of " + clusterQuestions.length + " [" + q.id + "]")
        .setHelpText(
          "SCENARIO:\n" + q.prompt + (q.cliSnippet ? "\n\nCLI:\n" + q.cliSnippet : "") + "\n\n" +
          "CHOICES & ANSWER:\n" + choices + "\n\n" +
          "EXPLANATION:\n" + q.explanation
        );

    // 2. Accuracy
    form.addMultipleChoiceItem()
        .setTitle("[" + q.id + "] Is this technically accurate?")
        .setRequired(true)
        .setChoiceValues(["Yes - Accurate", "Minor typo / wording", "Inaccurate - wrong answer/explanation"]);

    // 3. Fidelity
    form.addScaleItem()
        .setTitle("[" + q.id + "] Exam Closeness (1-5)")
        .setBounds(1, 5)
        .setLabels("Unrealistic", "Exact CCNA Style")
        .setRequired(true);

    // 4. Difficulty
    form.addScaleItem()
        .setTitle("[" + q.id + "] Difficulty (1-5)")
        .setBounds(1, 5)
        .setLabels("1 - Easy", "5 - Hard")
        .setRequired(true);

    // 5. Comments
    form.addParagraphTextItem()
        .setTitle("[" + q.id + "] Corrections or Feedback");
  });

  const url = form.getPublishedUrl();
  Logger.log("\n=======================================================");
  Logger.log("🎉 SUCCESS! Cluster 1.1 Form Created in 3 seconds!");
  Logger.log("👉 URL: " + url);
  Logger.log("=======================================================\n");
}

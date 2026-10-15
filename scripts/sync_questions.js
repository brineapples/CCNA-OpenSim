import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questionsPath = path.resolve(__dirname, '../src/data/questions.json');

/**
 * Parses a CSV line handling quotes and commas
 */
function parseCsvLine(text) {
  const result = [];
  let cur = '';
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      if (inQuotes && text[i + 1] === '"') {
        cur += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (c === ',' && !inQuotes) {
      result.push(cur.trim());
      cur = '';
    } else {
      cur += c;
    }
  }
  result.push(cur.trim());
  return result;
}

/**
 * Ingests questions from a published Google Sheet CSV URL or file.
 * Expected columns:
 * [0] Timestamp
 * [1] Domain ID (e.g. "3.0")
 * [2] Topic Code (e.g. "3.4")
 * [3] Topic Name
 * [4] Question Type (single-choice | multiple-choice | drag-and-drop | simlet)
 * [5] Prompt / Scenario
 * [6] CLI Snippet (optional)
 * [7] Option A
 * [8] Option B
 * [9] Option C
 * [10] Option D
 * [11] Option E (optional)
 * [12] Correct Option(s) (e.g. "A" or "A, C")
 * [13] Explanation
 * [14] Reference
 * [15] Difficulty (1-5)
 * [16] Review Status ("Approved", "Pending", "Needs Work")
 * [17] Fidelity Score (1-5)
 * [18] Contributor
 */
export async function syncFromCsvUrl(csvUrl) {
  console.log(`📡 Fetching approved responses from Google Sheet...`);
  
  let csvText = '';
  if (csvUrl.startsWith('http')) {
    const res = await fetch(csvUrl);
    if (!res.ok) throw new Error(`HTTP Error ${res.status}: ${res.statusText}`);
    csvText = await res.text();
  } else {
    csvText = fs.readFileSync(csvUrl, 'utf-8');
  }

  const lines = csvText.split('\n').filter(l => l.trim().length > 0);
  if (lines.length <= 1) {
    console.log('No rows found in sheet.');
    return;
  }

  // Load existing questions
  const existingQuestions = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));
  const questionMap = new Map(existingQuestions.map(q => [q.id, q]));

  let approvedCount = 0;

  for (let i = 1; i < lines.length; i++) {
    const cols = parseCsvLine(lines[i]);
    if (cols.length < 17) continue;

    const status = cols[16]?.trim();
    if (status?.toLowerCase() !== 'approved') {
      continue; // Skip unapproved or in-review items
    }

    const domainId = cols[1]?.trim();
    const subtopicCode = cols[2]?.trim();
    const subtopicName = cols[3]?.trim();
    const type = cols[4]?.trim() || 'single-choice';
    const prompt = cols[5]?.trim();
    const cliSnippet = cols[6]?.trim() || undefined;
    
    // Parse options
    const correctAnswers = (cols[12] || '').toUpperCase().split(',').map(s => s.trim());
    const rawOptions = [
      { id: 'A', text: cols[7]?.trim() },
      { id: 'B', text: cols[8]?.trim() },
      { id: 'C', text: cols[9]?.trim() },
      { id: 'D', text: cols[10]?.trim() },
      { id: 'E', text: cols[11]?.trim() },
    ].filter(o => o.text && o.text.length > 0);

    const options = rawOptions.map(o => ({
      ...o,
      isCorrect: correctAnswers.includes(o.id),
    }));

    const explanation = cols[13]?.trim();
    const reference = cols[14]?.trim() || undefined;
    const difficulty = parseInt(cols[15], 10) || 3;
    const fidelityScore = parseFloat(cols[17]) || 4.5;
    const contributor = cols[18]?.trim() || 'Community Contributor';

    const id = `q-${subtopicCode.replace('.', '-')}-${String(i).padStart(3, '0')}`;

    const questionObj = {
      id,
      domainId,
      subtopicCode,
      subtopicName,
      type,
      prompt,
      cliSnippet,
      options,
      explanation,
      reference,
      difficulty,
      fidelityScore,
      contributor,
    };

    questionMap.set(id, questionObj);
    approvedCount++;
  }

  const merged = Array.from(questionMap.values());
  fs.writeFileSync(questionsPath, JSON.stringify(merged, null, 2));
  console.log(`✅ Synced and updated ${approvedCount} approved questions from Google Sheet into questions.json!`);
}

// CLI runner if executed directly
const target = process.argv[2];
if (target) {
  syncFromCsvUrl(target).catch(console.error);
} else {
  console.log('Usage: node scripts/sync_questions.js <Google_Sheet_Published_CSV_URL_or_File>');
}

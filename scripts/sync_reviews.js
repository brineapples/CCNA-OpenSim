import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questionsPath = path.resolve(__dirname, '../src/data/questions.json');

/**
 * Parses CSV text handling multiline values and quotes
 */
function parseCsv(text) {
  const rows = [];
  let row = [];
  let col = '';
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      if (inQuotes && text[i + 1] === '"') {
        col += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (c === ',' && !inQuotes) {
      row.push(col.trim());
      col = '';
    } else if ((c === '\r' || c === '\n') && !inQuotes) {
      if (c === '\r' && text[i + 1] === '\n') i++;
      row.push(col.trim());
      col = '';
      if (row.length > 0 && row.some(item => item.length > 0)) {
        rows.push(row);
      }
      row = [];
    } else {
      col += c;
    }
  }
  if (col.length > 0 || row.length > 0) {
    row.push(col.trim());
    rows.push(row);
  }
  return rows;
}

/**
 * Syncs reviewer feedback, ratings, and status from Master CSV or Sheet back into questions.json
 */
export async function syncReviews(csvSource) {
  console.log(`📡 Reading community review feedback from: ${csvSource}...`);

  let csvText = '';
  if (csvSource.startsWith('http')) {
    const res = await fetch(csvSource);
    if (!res.ok) throw new Error(`HTTP Error ${res.status}: ${res.statusText}`);
    csvText = await res.text();
  } else {
    csvText = fs.readFileSync(csvSource, 'utf-8');
  }

  const rows = parseCsv(csvText);
  if (rows.length <= 1) {
    console.log('No rows found to sync.');
    return;
  }

  const questions = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));
  const questionMap = new Map(questions.map(q => [q.id, q]));

  let updatedCount = 0;

  // Expected headers: Question ID is column 0, Fidelity is 16, Difficulty is 15, Status is 17
  for (let i = 1; i < rows.length; i++) {
    const cols = rows[i];
    const qId = cols[0]?.trim();
    if (!qId || !questionMap.has(qId)) continue;

    const targetQ = questionMap.get(qId);
    let changed = false;

    // Difficulty (col 15)
    const diff = parseInt(cols[15], 10);
    if (!isNaN(diff) && diff >= 1 && diff <= 5 && diff !== targetQ.difficulty) {
      targetQ.difficulty = diff;
      changed = true;
    }

    // Fidelity (col 16)
    const fidelity = parseFloat(cols[16]);
    if (!isNaN(fidelity) && fidelity >= 1.0 && fidelity <= 5.0 && fidelity !== targetQ.fidelityScore) {
      targetQ.fidelityScore = fidelity;
      changed = true;
    }

    // Status (col 17)
    const status = cols[17]?.trim();
    if (status && status !== targetQ.reviewStatus) {
      targetQ.reviewStatus = status;
      changed = true;
    }

    // Feedback (col 18)
    const feedback = cols[18]?.trim();
    if (feedback && feedback.length > 0) {
      targetQ.reviewerFeedback = feedback;
      changed = true;
    }

    if (changed) {
      updatedCount++;
    }
  }

  fs.writeFileSync(questionsPath, JSON.stringify(questions, null, 2));
  console.log(`✅ Successfully synced reviews! Updated metadata for ${updatedCount} questions.`);
}

const inputArg = process.argv[2];
if (inputArg) {
  syncReviews(inputArg).catch(console.error);
} else {
  console.log('Usage: node scripts/sync_reviews.js <CSV_Path_or_Published_Google_Sheet_URL>');
}

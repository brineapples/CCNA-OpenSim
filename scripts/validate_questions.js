import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questionsPath = path.resolve(__dirname, '../src/data/questions.json');
const blueprintPath = path.resolve(__dirname, '../src/data/blueprint_v1_1.json');

console.log('🔍 Validating CCNA OpenSim Question Bank...');

const questions = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));
const blueprint = JSON.parse(fs.readFileSync(blueprintPath, 'utf-8'));

const validDomains = new Set(blueprint.domains.map((d) => d.id));
let errorCount = 0;

questions.forEach((q, index) => {
  const prefix = `[Q #${index + 1} (${q.id || 'NO_ID'})]:`;

  if (!q.id) {
    console.error(`${prefix} Missing 'id'`);
    errorCount++;
  }
  if (!validDomains.has(q.domainId)) {
    console.error(`${prefix} Invalid domainId '${q.domainId}'. Must be one of: ${Array.from(validDomains).join(', ')}`);
    errorCount++;
  }
  if (!q.prompt || q.prompt.trim().length === 0) {
    console.error(`${prefix} Missing prompt text`);
    errorCount++;
  }
  if (!q.explanation || q.explanation.trim().length === 0) {
    console.error(`${prefix} Missing explanation`);
    errorCount++;
  }

  // Type-specific validations
  if (q.type === 'single-choice') {
    if (!q.options || q.options.length < 2) {
      console.error(`${prefix} Single-choice must have at least 2 options`);
      errorCount++;
    } else {
      const correct = q.options.filter((o) => o.isCorrect);
      if (correct.length !== 1) {
        console.error(`${prefix} Single-choice must have EXACTLY 1 correct option (found ${correct.length})`);
        errorCount++;
      }
    }
  } else if (q.type === 'multiple-choice') {
    if (!q.options || q.options.length < 3) {
      console.error(`${prefix} Multiple-choice must have at least 3 options`);
      errorCount++;
    } else {
      const correct = q.options.filter((o) => o.isCorrect);
      if (correct.length < 2) {
        console.error(`${prefix} Multiple-choice must have at least 2 correct options (found ${correct.length})`);
        errorCount++;
      }
    }
  } else if (q.type === 'drag-and-drop') {
    if (!q.pairs || q.pairs.length < 2) {
      console.error(`${prefix} Drag-and-drop question must have at least 2 matching pairs`);
      errorCount++;
    }
  } else if (q.type === 'simlet') {
    if (!q.simlet || !q.simlet.commandResponses || Object.keys(q.simlet.commandResponses).length === 0) {
      console.error(`${prefix} Simlet must contain commandResponses dictionary`);
      errorCount++;
    }
    if (!q.options || q.options.length < 2) {
      console.error(`${prefix} Simlet must have at least 2 answer options`);
      errorCount++;
    }
  } else {
    console.error(`${prefix} Unknown question type '${q.type}'`);
    errorCount++;
  }
});

if (errorCount > 0) {
  console.error(`\n❌ Validation FAILED with ${errorCount} errors.`);
  process.exit(1);
} else {
  console.log(`\n✅ All ${questions.length} questions in bank PASSED validation!`);
  console.log(`📊 Domain Breakdown:`);
  blueprint.domains.forEach((dom) => {
    const count = questions.filter((q) => q.domainId === dom.id).length;
    console.log(`   - ${dom.id} ${dom.name}: ${count} questions`);
  });
}

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const domainsDir = path.resolve(__dirname, '../src/data/domains');
const outputPath = path.resolve(__dirname, '../src/data/questions.json');
const blueprintPath = path.resolve(__dirname, '../src/data/blueprint_v1_1.json');

console.log('🚀 Compiling CCNA OpenSim 400-Question Bank...');

const blueprint = JSON.parse(fs.readFileSync(blueprintPath, 'utf-8'));
const domainFiles = ['domain1.json', 'domain2.json', 'domain3.json', 'domain4.json', 'domain5.json', 'domain6.json'];

let allQuestions = [];
const seenIds = new Set();
let duplicates = 0;

for (const file of domainFiles) {
  const filePath = path.join(domainsDir, file);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Error: Missing domain file ${filePath}`);
    process.exit(1);
  }

  const questions = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  console.log(`📦 Loaded ${file}: ${questions.length} questions`);

  for (const q of questions) {
    if (seenIds.has(q.id)) {
      console.warn(`⚠️ Duplicate ID detected: ${q.id}. Auto-reindexing...`);
      duplicates++;
      q.id = `${q.id}-dup-${duplicates}`;
    }
    seenIds.add(q.id);
    allQuestions.push(q);
  }
}

fs.writeFileSync(outputPath, JSON.stringify(allQuestions, null, 2), 'utf-8');
console.log(`\n🎉 Successfully compiled ${allQuestions.length} questions into ${outputPath}!`);

console.log('\n📊 Domain Breakdown:');
blueprint.domains.forEach((dom) => {
  const count = allQuestions.filter((q) => q.domainId === dom.id).length;
  const target = dom.targetQuestions;
  const matchIcon = count === target ? '✅' : '⚠️';
  console.log(`   ${matchIcon} ${dom.id} ${dom.name}: ${count} / ${target} target`);
});

if (allQuestions.length === 400) {
  console.log('\n🎯 EXACT 400-QUESTION TARGET ACHIEVED!');
} else {
  console.log(`\n⚠️ Total count is ${allQuestions.length} (Target: 400)`);
}

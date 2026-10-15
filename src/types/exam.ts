export type DomainId = '1.0' | '2.0' | '3.0' | '4.0' | '5.0' | '6.0';

export type QuestionType = 'single-choice' | 'multiple-choice' | 'drag-and-drop' | 'simlet';

export interface Option {
  id: string;
  text: string;
  isCorrect: boolean;
}

export interface DragPair {
  target: string;
  match: string;
}

export interface SimletContext {
  deviceName: string;
  promptString: string;
  commandResponses: Record<string, string>;
}

export interface Question {
  id: string;
  domainId: DomainId;
  subtopicCode: string;
  subtopicName: string;
  type: QuestionType;
  prompt: string;
  cliSnippet?: string;
  diagramUrl?: string;
  options?: Option[];
  pairs?: DragPair[];
  simlet?: SimletContext;
  explanation: string;
  reference?: string;
  difficulty: 1 | 2 | 3 | 4 | 5;
  fidelityScore: number;
  contributor?: string;
}

export interface Subtopic {
  code: string;
  title: string;
}

export interface DomainMeta {
  id: DomainId;
  name: string;
  weight: number;
  color: string;
  targetQuestions: number;
  subtopics: Subtopic[];
}

export interface Blueprint {
  version: string;
  examCode: string;
  totalDurationMinutes: number;
  passingScore: number;
  maxScore: number;
  domains: DomainMeta[];
}

export interface UserAnswer {
  questionId: string;
  selectedOptionIds?: string[]; // For single/multiple choice
  dragMatches?: Record<string, string>; // target -> matched text
  isFlagged?: boolean;
}

export interface DomainScore {
  domainId: DomainId;
  name: string;
  total: number;
  correct: number;
  percentage: number;
  weight: number;
}

export interface ExamResult {
  totalQuestions: number;
  totalCorrect: number;
  scaledScore: number; // 300 to 1000
  passed: boolean;
  passingScore: number;
  timeSpentSeconds: number;
  domainScores: DomainScore[];
}

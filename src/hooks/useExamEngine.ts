import { useState, useEffect, useMemo, useCallback } from 'react';
import type { Question, UserAnswer, ExamResult, DomainScore, DomainId, Blueprint } from '../types/exam';
import rawQuestions from '../data/questions.json';
import blueprintData from '../data/blueprint_v1_1.json';

const blueprint = blueprintData as Blueprint;
const allQuestions = rawQuestions as Question[];

const STORAGE_KEY = 'ccna_opensim_state_v1';
const TOTAL_EXAM_SECONDS = 120 * 60; // 120 minutes

export function useExamEngine() {
  const [viewMode, setViewMode] = useState<'welcome' | 'exam' | 'results' | 'review' | 'hub'>('welcome');
  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [answers, setAnswers] = useState<Record<string, UserAnswer>>({});
  const [timeRemaining, setTimeRemaining] = useState<number>(TOTAL_EXAM_SECONDS);
  const [isPaused, setIsPaused] = useState<boolean>(false);
  const [isGridOpen, setIsGridOpen] = useState<boolean>(false);
  const [selectedDomainFilter, setSelectedDomainFilter] = useState<DomainId | 'all'>('all');

  // Load saved session on initial mount if available
  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed && parsed.questions && parsed.questions.length > 0) {
          setQuestions(parsed.questions);
          setAnswers(parsed.answers || {});
          setCurrentIndex(parsed.currentIndex || 0);
          setTimeRemaining(parsed.timeRemaining ?? TOTAL_EXAM_SECONDS);
          setViewMode(parsed.viewMode || 'welcome');
        }
      }
    } catch (e) {
      console.warn('Could not load saved exam state', e);
    }
  }, []);

  // Save state on updates
  useEffect(() => {
    if (questions.length > 0 && (viewMode === 'exam' || viewMode === 'results' || viewMode === 'review')) {
      try {
        localStorage.setItem(
          STORAGE_KEY,
          JSON.stringify({
            questions,
            answers,
            currentIndex,
            timeRemaining,
            viewMode,
          })
        );
      } catch (e) {
        console.warn('Could not save exam state', e);
      }
    }
  }, [questions, answers, currentIndex, timeRemaining, viewMode]);

  // Timer countdown
  useEffect(() => {
    if (viewMode !== 'exam' || isPaused || timeRemaining <= 0) return;

    const timer = setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          // Auto submit on time expiry
          handleFinishExam();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [viewMode, isPaused, timeRemaining]);

  // Start a new exam
  const startExam = useCallback((domainFilter: DomainId | 'all' = 'all') => {
    let pool = [...allQuestions];
    if (domainFilter !== 'all') {
      pool = pool.filter((q) => q.domainId === domainFilter);
    }

    // Shuffle questions
    const shuffled = [...pool].sort(() => Math.random() - 0.5);

    setQuestions(shuffled);
    setCurrentIndex(0);
    setAnswers({});
    setTimeRemaining(TOTAL_EXAM_SECONDS);
    setIsPaused(false);
    setSelectedDomainFilter(domainFilter);
    setViewMode('exam');
    localStorage.removeItem(STORAGE_KEY);
  }, []);

  const handleAnswerChange = useCallback((answer: UserAnswer) => {
    setAnswers((prev) => ({
      ...prev,
      [answer.questionId]: answer,
    }));
  }, []);

  // Check if a question is answered correctly
  const isQuestionCorrect = useCallback((q: Question, ans?: UserAnswer): boolean => {
    if (!ans) return false;

    if (q.type === 'single-choice' || q.type === 'multiple-choice' || q.type === 'simlet') {
      const correctOptionIds = q.options?.filter((o) => o.isCorrect).map((o) => o.id) || [];
      const selectedIds = ans.selectedOptionIds || [];

      if (correctOptionIds.length !== selectedIds.length) return false;
      return correctOptionIds.every((id) => selectedIds.includes(id));
    }

    if (q.type === 'drag-and-drop' && q.pairs) {
      const matches = ans.dragMatches || {};
      return q.pairs.every((p) => matches[p.target] === p.match);
    }

    return false;
  }, []);

  // Compute final score & domain breakdown
  const examResult = useMemo<ExamResult>(() => {
    if (questions.length === 0) {
      return {
        totalQuestions: 0,
        totalCorrect: 0,
        scaledScore: 300,
        passed: false,
        passingScore: blueprint.passingScore,
        timeSpentSeconds: 0,
        domainScores: [],
      };
    }

    let totalCorrect = 0;
    const domainTotals: Record<string, { total: number; correct: number }> = {
      '1.0': { total: 0, correct: 0 },
      '2.0': { total: 0, correct: 0 },
      '3.0': { total: 0, correct: 0 },
      '4.0': { total: 0, correct: 0 },
      '5.0': { total: 0, correct: 0 },
      '6.0': { total: 0, correct: 0 },
    };

    questions.forEach((q) => {
      const correct = isQuestionCorrect(q, answers[q.id]);
      if (correct) totalCorrect++;

      if (domainTotals[q.domainId]) {
        domainTotals[q.domainId].total++;
        if (correct) domainTotals[q.domainId].correct++;
      }
    });

    const percent = questions.length > 0 ? totalCorrect / questions.length : 0;
    // Cisco scaled score between 300 and 1000
    const scaledScore = Math.round(300 + percent * 700);
    const passed = scaledScore >= blueprint.passingScore;

    const domainScores: DomainScore[] = blueprint.domains.map((dom) => {
      const stats = domainTotals[dom.id] || { total: 0, correct: 0 };
      const percentage = stats.total > 0 ? (stats.correct / stats.total) * 100 : 0;
      return {
        domainId: dom.id,
        name: dom.name,
        total: stats.total,
        correct: stats.correct,
        percentage,
        weight: dom.weight,
      };
    });

    return {
      totalQuestions: questions.length,
      totalCorrect,
      scaledScore,
      passed,
      passingScore: blueprint.passingScore,
      timeSpentSeconds: TOTAL_EXAM_SECONDS - timeRemaining,
      domainScores,
    };
  }, [questions, answers, timeRemaining, isQuestionCorrect]);

  const handleFinishExam = useCallback(() => {
    setViewMode('results');
  }, []);

  const handleResetSession = useCallback(() => {
    localStorage.removeItem(STORAGE_KEY);
    setViewMode('welcome');
    setQuestions([]);
    setAnswers({});
    setCurrentIndex(0);
    setTimeRemaining(TOTAL_EXAM_SECONDS);
  }, []);

  return {
    viewMode,
    setViewMode,
    questions,
    currentIndex,
    setCurrentIndex,
    answers,
    timeRemaining,
    isPaused,
    setIsPaused,
    isGridOpen,
    setIsGridOpen,
    selectedDomainFilter,
    startExam,
    handleAnswerChange,
    handleFinishExam,
    handleResetSession,
    examResult,
    blueprint,
    totalVettedQuestions: allQuestions.length,
  };
}

import React from 'react';
import type { Question, UserAnswer } from '../types/exam';
import { ChoiceQuestionView } from './ChoiceQuestionView';
import { DragAndDropView } from './DragAndDropView';
import { CiscoTerminal } from './CiscoTerminal';
import { BookOpen, Star, Flag, Info } from 'lucide-react';

interface QuestionCardProps {
  question: Question;
  userAnswer?: UserAnswer;
  onAnswerChange: (answer: UserAnswer) => void;
  showResults?: boolean;
}

export const QuestionCard: React.FC<QuestionCardProps> = ({
  question,
  userAnswer,
  onAnswerChange,
  showResults = false,
}) => {
  const isFlagged = userAnswer?.isFlagged || false;

  const handleToggleFlag = () => {
    onAnswerChange({
      ...userAnswer,
      questionId: question.id,
      isFlagged: !isFlagged,
    });
  };

  const handleSelectionChange = (selectedOptionIds: string[]) => {
    onAnswerChange({
      ...userAnswer,
      questionId: question.id,
      selectedOptionIds,
    });
  };

  const handleDragMatchChange = (dragMatches: Record<string, string>) => {
    onAnswerChange({
      ...userAnswer,
      questionId: question.id,
      dragMatches,
    });
  };

  const getDomainColor = (domainId: string) => {
    switch (domainId) {
      case '1.0': return 'bg-cyan-950 text-cyan-300 border-cyan-800';
      case '2.0': return 'bg-blue-950 text-blue-300 border-blue-800';
      case '3.0': return 'bg-emerald-950 text-emerald-300 border-emerald-800';
      case '4.0': return 'bg-amber-950 text-amber-300 border-amber-800';
      case '5.0': return 'bg-rose-950 text-rose-300 border-rose-800';
      case '6.0': return 'bg-purple-950 text-purple-300 border-purple-800';
      default: return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 md:p-7 shadow-xl space-y-6">
      {/* Question Header Metadata */}
      <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800/80 pb-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className={`text-xs px-2.5 py-1 rounded-full font-medium border ${getDomainColor(question.domainId)}`}>
            Domain {question.domainId}
          </span>
          <span className="text-xs text-slate-400 font-mono">
            Topic {question.subtopicCode} - {question.subtopicName}
          </span>
        </div>

        <div className="flex items-center gap-4">
          {/* Difficulty indicators */}
          <div className="flex items-center gap-0.5" title={`Difficulty: ${question.difficulty}/5`}>
            {[1, 2, 3, 4, 5].map((lvl) => (
              <Star
                key={lvl}
                className={`w-3.5 h-3.5 ${
                  lvl <= question.difficulty
                    ? 'text-amber-400 fill-amber-400'
                    : 'text-slate-700'
                }`}
              />
            ))}
          </div>

          {/* Flag Button */}
          <button
            type="button"
            onClick={handleToggleFlag}
            className={`flex items-center gap-1.5 text-xs px-2.5 py-1 rounded-md border transition ${
              isFlagged
                ? 'bg-amber-950/60 border-amber-500 text-amber-300'
                : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-slate-200'
            }`}
          >
            <Flag className={`w-3.5 h-3.5 ${isFlagged ? 'fill-amber-400 text-amber-400' : ''}`} />
            <span>{isFlagged ? 'Flagged' : 'Flag'}</span>
          </button>
        </div>
      </div>

      {/* Question Scenario / Prompt */}
      <div className="text-base md:text-lg text-slate-100 font-medium leading-relaxed">
        {question.prompt}
      </div>

      {/* Terminal for Simlet Questions */}
      {question.type === 'simlet' && question.simlet && (
        <CiscoTerminal simlet={question.simlet} />
      )}

      {/* Choice Options View */}
      {(question.type === 'single-choice' || question.type === 'multiple-choice' || question.type === 'simlet') && question.options && (
        <ChoiceQuestionView
          type={question.type === 'multiple-choice' ? 'multiple-choice' : 'single-choice'}
          options={question.options}
          selectedOptionIds={userAnswer?.selectedOptionIds}
          cliSnippet={question.cliSnippet}
          onSelectionChange={handleSelectionChange}
          showResults={showResults}
        />
      )}

      {/* Drag and Drop View */}
      {question.type === 'drag-and-drop' && question.pairs && (
        <DragAndDropView
          pairs={question.pairs}
          currentMatches={userAnswer?.dragMatches}
          onMatchChange={handleDragMatchChange}
          showResults={showResults}
        />
      )}

      {/* Explanation and Reference Card (Visible when showResults is true) */}
      {showResults && (
        <div className="mt-6 p-4 rounded-lg bg-slate-950 border border-cyan-900/60 text-slate-300 space-y-2">
          <div className="flex items-center gap-2 text-cyan-400 font-semibold text-sm">
            <Info className="w-4 h-4" />
            <span>Official Explanation & Analysis</span>
          </div>
          <p className="text-sm leading-relaxed text-slate-300">
            {question.explanation}
          </p>
          {question.reference && (
            <div className="flex items-center gap-1.5 text-xs text-slate-400 pt-2 border-t border-slate-900">
              <BookOpen className="w-3.5 h-3.5 text-cyan-400" />
              <span>Reference: {question.reference}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

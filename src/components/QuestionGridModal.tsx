import React, { useState } from 'react';
import type { Question, UserAnswer } from '../types/exam';
import { X, Flag, CheckCircle2, Circle } from 'lucide-react';

interface QuestionGridModalProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  answers: Record<string, UserAnswer>;
  currentIndex: number;
  onSelectQuestion: (index: number) => void;
}

export const QuestionGridModal: React.FC<QuestionGridModalProps> = ({
  isOpen,
  onClose,
  questions,
  answers,
  currentIndex,
  onSelectQuestion,
}) => {
  const [filter, setFilter] = useState<'all' | 'unanswered' | 'flagged'>('all');

  if (!isOpen) return null;

  const isAnswered = (q: Question) => {
    const a = answers[q.id];
    if (!a) return false;
    if (q.type === 'drag-and-drop') {
      return a.dragMatches && Object.keys(a.dragMatches).length > 0;
    }
    return a.selectedOptionIds && a.selectedOptionIds.length > 0;
  };

  const isFlagged = (q: Question) => {
    return Boolean(answers[q.id]?.isFlagged);
  };

  const filteredQuestions = questions.map((q, idx) => ({ q, idx })).filter(({ q }) => {
    if (filter === 'unanswered') return !isAnswered(q);
    if (filter === 'flagged') return isFlagged(q);
    return true;
  });

  const answeredCount = questions.filter(isAnswered).length;
  const flaggedCount = questions.filter(isFlagged).length;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
        {/* Modal Header */}
        <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold text-white">Question Overview & Navigation</h3>
            <p className="text-xs text-slate-400">
              Answered: {answeredCount}/{questions.length} • Flagged for review: {flaggedCount}
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Filter Tabs */}
        <div className="px-6 py-3 border-b border-slate-800/80 bg-slate-950/40 flex items-center gap-2 text-xs">
          <button
            onClick={() => setFilter('all')}
            className={`px-3 py-1.5 rounded-md font-medium transition ${
              filter === 'all'
                ? 'bg-cyan-500 text-slate-950'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            All Questions ({questions.length})
          </button>
          <button
            onClick={() => setFilter('unanswered')}
            className={`px-3 py-1.5 rounded-md font-medium transition ${
              filter === 'unanswered'
                ? 'bg-cyan-500 text-slate-950'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            Unanswered ({questions.length - answeredCount})
          </button>
          <button
            onClick={() => setFilter('flagged')}
            className={`px-3 py-1.5 rounded-md font-medium transition ${
              filter === 'flagged'
                ? 'bg-cyan-500 text-slate-950'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            Flagged ({flaggedCount})
          </button>
        </div>

        {/* Questions Grid */}
        <div className="p-6 overflow-y-auto flex-1">
          <div className="grid grid-cols-4 sm:grid-cols-6 md:grid-cols-8 gap-2.5">
            {filteredQuestions.map(({ q, idx }) => {
              const answered = isAnswered(q);
              const flagged = isFlagged(q);
              const isCurrent = idx === currentIndex;

              return (
                <button
                  key={q.id}
                  onClick={() => {
                    onSelectQuestion(idx);
                    onClose();
                  }}
                  className={`relative p-2.5 rounded-lg border text-sm font-semibold flex flex-col items-center justify-center transition ${
                    isCurrent
                      ? 'ring-2 ring-cyan-400 border-cyan-400'
                      : ''
                  } ${
                    answered
                      ? 'bg-cyan-950/50 border-cyan-700 text-cyan-200 hover:bg-cyan-900/50'
                      : 'bg-slate-800/60 border-slate-700 text-slate-400 hover:bg-slate-800 hover:text-slate-200'
                  }`}
                >
                  <span>{idx + 1}</span>
                  {flagged && (
                    <span className="absolute top-1 right-1">
                      <Flag className="w-2.5 h-2.5 fill-amber-400 text-amber-400" />
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        </div>

        {/* Legend Footer */}
        <div className="px-6 py-3 border-t border-slate-800 bg-slate-950/60 flex items-center justify-between text-xs text-slate-400">
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400" /> Answered
            </span>
            <span className="flex items-center gap-1.5">
              <Circle className="w-3.5 h-3.5 text-slate-600" /> Unanswered
            </span>
            <span className="flex items-center gap-1.5">
              <Flag className="w-3.5 h-3.5 text-amber-400 fill-amber-400" /> Flagged
            </span>
          </div>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition font-medium"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

import React, { useState } from 'react';
import type { Option } from '../types/exam';
import { Check, X, Copy, CheckCheck } from 'lucide-react';

interface ChoiceQuestionViewProps {
  type: 'single-choice' | 'multiple-choice';
  options: Option[];
  selectedOptionIds?: string[];
  cliSnippet?: string;
  onSelectionChange: (selectedIds: string[]) => void;
  showResults?: boolean;
}

export const ChoiceQuestionView: React.FC<ChoiceQuestionViewProps> = ({
  type,
  options,
  selectedOptionIds = [],
  cliSnippet,
  onSelectionChange,
  showResults = false,
}) => {
  const [copied, setCopied] = useState(false);

  const handleToggle = (optId: string) => {
    if (showResults) return;

    if (type === 'single-choice') {
      onSelectionChange([optId]);
    } else {
      if (selectedOptionIds.includes(optId)) {
        onSelectionChange(selectedOptionIds.filter(id => id !== optId));
      } else {
        onSelectionChange([...selectedOptionIds, optId]);
      }
    }
  };

  const handleCopyCli = () => {
    if (!cliSnippet) return;
    navigator.clipboard.writeText(cliSnippet);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-4 my-3">
      {/* CLI Output Snippet if available */}
      {cliSnippet && (
        <div className="relative rounded-lg border border-slate-700 bg-slate-950 p-3 overflow-x-auto my-3">
          <div className="flex items-center justify-between text-xs text-slate-400 border-b border-slate-800 pb-1 mb-2 font-mono">
            <span>Cisco IOS Command Output</span>
            <button
              type="button"
              onClick={handleCopyCli}
              className="flex items-center gap-1 text-[11px] text-slate-400 hover:text-white px-1.5 py-0.5 rounded bg-slate-800 hover:bg-slate-700 transition"
              title="Copy output"
            >
              {copied ? <CheckCheck className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
              <span>{copied ? 'Copied' : 'Copy'}</span>
            </button>
          </div>
          <pre className="font-mono text-xs md:text-sm text-slate-200 whitespace-pre leading-relaxed">
            {cliSnippet}
          </pre>
        </div>
      )}

      {/* Options List */}
      <div className="space-y-2.5">
        {options.map((option) => {
          const isSelected = selectedOptionIds.includes(option.id);
          const isCorrect = option.isCorrect;
          
          let cardStyle = 'border-slate-800 bg-slate-900/60 hover:border-slate-700 hover:bg-slate-900 text-slate-200';
          let badgeStyle = 'border-slate-700 bg-slate-800 text-slate-400';

          if (showResults) {
            if (isCorrect) {
              cardStyle = 'border-emerald-500 bg-emerald-950/30 text-emerald-100';
              badgeStyle = 'border-emerald-500 bg-emerald-600 text-white';
            } else if (isSelected && !isCorrect) {
              cardStyle = 'border-rose-500 bg-rose-950/30 text-rose-100';
              badgeStyle = 'border-rose-500 bg-rose-600 text-white';
            }
          } else if (isSelected) {
            cardStyle = 'border-cyan-500 bg-cyan-950/30 text-cyan-100 ring-1 ring-cyan-500';
            badgeStyle = 'border-cyan-400 bg-cyan-500 text-slate-950 font-bold';
          }

          return (
            <div
              key={option.id}
              onClick={() => handleToggle(option.id)}
              className={`p-3.5 rounded-lg border transition cursor-pointer flex items-start gap-3.5 ${cardStyle}`}
            >
              <div
                className={`w-6 h-6 rounded flex items-center justify-center shrink-0 border text-xs font-semibold mt-0.5 transition ${badgeStyle}`}
              >
                {showResults ? (
                  isCorrect ? (
                    <Check className="w-4 h-4 text-white" />
                  ) : isSelected ? (
                    <X className="w-4 h-4 text-white" />
                  ) : (
                    option.id
                  )
                ) : (
                  option.id
                )}
              </div>
              <div className="flex-1 text-sm md:text-base leading-relaxed">
                {option.text}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

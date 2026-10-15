import React, { useState, useMemo } from 'react';
import type { DragPair } from '../types/exam';
import { GripVertical, Check, X } from 'lucide-react';

interface DragAndDropViewProps {
  pairs: DragPair[];
  currentMatches?: Record<string, string>; // target -> match text
  onMatchChange: (matches: Record<string, string>) => void;
  showResults?: boolean;
}

export const DragAndDropView: React.FC<DragAndDropViewProps> = ({
  pairs,
  currentMatches = {},
  onMatchChange,
  showResults = false,
}) => {
  const [selectedMatch, setSelectedMatch] = useState<string | null>(null);

  // Available draggable options that haven't been assigned yet
  const assignedValues = useMemo(() => new Set(Object.values(currentMatches)), [currentMatches]);

  const unassignedMatches = useMemo(() => {
    return pairs.map(p => p.match).filter(m => !assignedValues.has(m));
  }, [pairs, assignedValues]);

  const handleSelectMatch = (matchText: string) => {
    if (showResults) return;
    if (selectedMatch === matchText) {
      setSelectedMatch(null);
    } else {
      setSelectedMatch(matchText);
    }
  };

  const handleAssignToTarget = (targetText: string) => {
    if (showResults) return;
    if (selectedMatch) {
      const next = { ...currentMatches, [targetText]: selectedMatch };
      onMatchChange(next);
      setSelectedMatch(null);
    } else if (currentMatches[targetText]) {
      // Remove match if clicking an already filled target
      const next = { ...currentMatches };
      delete next[targetText];
      onMatchChange(next);
    }
  };

  const handleClearSlot = (targetText: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (showResults) return;
    const next = { ...currentMatches };
    delete next[targetText];
    onMatchChange(next);
  };

  return (
    <div className="space-y-6 my-4 select-none">
      <p className="text-sm text-slate-400">
        Click or drag an item from the pool on the right to match each item on the left. Tap a slotted item to return it.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Left: Targets */}
        <div className="space-y-3">
          <h4 className="text-xs uppercase tracking-wider font-semibold text-slate-400 mb-2">Categories / Targets</h4>
          {pairs.map((p, idx) => {
            const currentMatch = currentMatches[p.target];
            const isCorrect = showResults && currentMatch === p.match;
            const isWrong = showResults && currentMatch && currentMatch !== p.match;

            return (
              <div
                key={idx}
                onClick={() => handleAssignToTarget(p.target)}
                className={`p-3 rounded-lg border transition cursor-pointer flex flex-col justify-between min-h-[72px] ${
                  currentMatch
                    ? isCorrect
                      ? 'border-emerald-500 bg-emerald-950/20'
                      : isWrong
                      ? 'border-rose-500 bg-rose-950/20'
                      : 'border-cyan-600 bg-slate-900'
                    : selectedMatch
                    ? 'border-dashed border-cyan-400 bg-cyan-950/20 hover:bg-cyan-950/40'
                    : 'border-slate-700 bg-slate-900/50 hover:border-slate-600'
                }`}
              >
                <div className="flex items-center justify-between text-sm font-medium text-slate-200">
                  <span>{p.target}</span>
                  {showResults && (
                    <span>
                      {isCorrect ? (
                        <Check className="w-4 h-4 text-emerald-400 inline" />
                      ) : (
                        <X className="w-4 h-4 text-rose-400 inline" />
                      )}
                    </span>
                  )}
                </div>

                {/* Slotted Value */}
                {currentMatch ? (
                  <div className="mt-2 flex items-center justify-between p-2 rounded bg-slate-800 text-cyan-300 font-mono text-xs border border-slate-700">
                    <span>{currentMatch}</span>
                    {!showResults && (
                      <button
                        type="button"
                        onClick={(e) => handleClearSlot(p.target, e)}
                        className="text-slate-400 hover:text-white p-0.5"
                        title="Remove"
                      >
                        <X className="w-3.5 h-3.5" />
                      </button>
                    )}
                  </div>
                ) : (
                  <div className="mt-2 text-xs text-slate-500 italic">
                    {selectedMatch ? 'Click here to place selected item' : '[ Empty Slot ]'}
                  </div>
                )}

                {showResults && !isCorrect && (
                  <div className="mt-1 text-xs text-emerald-400">Correct: {p.match}</div>
                )}
              </div>
            );
          })}
        </div>

        {/* Right: Available Item Pool */}
        <div className="space-y-3">
          <h4 className="text-xs uppercase tracking-wider font-semibold text-slate-400 mb-2">Available Items Pool</h4>
          {unassignedMatches.length === 0 && !showResults ? (
            <div className="p-6 rounded-lg border border-dashed border-slate-800 text-center text-sm text-slate-500">
              All items have been placed! Click any placed item to return it.
            </div>
          ) : (
            <div className="space-y-2">
              {pairs.map((p, idx) => {
                const isAssigned = assignedValues.has(p.match);
                if (isAssigned && !showResults) return null;

                const isSelected = selectedMatch === p.match;

                return (
                  <div
                    key={idx}
                    onClick={() => handleSelectMatch(p.match)}
                    className={`p-3 rounded-lg border font-mono text-xs md:text-sm flex items-center justify-between transition cursor-pointer ${
                      isAssigned
                        ? 'opacity-40 border-slate-800 bg-slate-900/30'
                        : isSelected
                        ? 'border-cyan-400 bg-cyan-950/40 text-cyan-200 ring-2 ring-cyan-500/50'
                        : 'border-slate-700 bg-slate-900 text-slate-200 hover:border-slate-500'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <GripVertical className="w-4 h-4 text-slate-500" />
                      <span>{p.match}</span>
                    </div>
                    {isSelected && (
                      <span className="text-[11px] text-cyan-400 font-sans font-semibold">Selected</span>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

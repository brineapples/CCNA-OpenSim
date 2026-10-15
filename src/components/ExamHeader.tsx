import React from 'react';
import { Timer, LayoutGrid, Users, CheckSquare, Pause, Play } from 'lucide-react';

interface ExamHeaderProps {
  currentIndex: number;
  totalQuestions: number;
  timeRemainingSeconds: number;
  isPaused: boolean;
  onTogglePause: () => void;
  onOpenGrid: () => void;
  onOpenHub: () => void;
  onFinishExam: () => void;
  examMode: 'exam' | 'review';
}

export const ExamHeader: React.FC<ExamHeaderProps> = ({
  currentIndex,
  totalQuestions,
  timeRemainingSeconds,
  isPaused,
  onTogglePause,
  onOpenGrid,
  onOpenHub,
  onFinishExam,
  examMode,
}) => {
  const formatTime = (secs: number) => {
    const hours = Math.floor(secs / 3600);
    const minutes = Math.floor((secs % 3600) / 60);
    const seconds = secs % 60;

    const pad = (n: number) => n.toString().padStart(2, '0');
    if (hours > 0) {
      return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    }
    return `${pad(minutes)}:${pad(seconds)}`;
  };

  const isLowTime = timeRemainingSeconds <= 900; // 15 mins

  return (
    <header className="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-3 select-none">
      <div className="max-w-5xl mx-auto flex items-center justify-between gap-4">
        {/* Brand / Mode */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-600 to-blue-500 flex items-center justify-center text-slate-950 font-black text-sm shadow-md shadow-cyan-500/20">
            CCNA
          </div>
          <div>
            <div className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
              <span>OpenSim</span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-cyan-400 font-mono font-normal border border-slate-700">
                v1.1
              </span>
            </div>
            <div className="text-xs text-slate-400">
              {examMode === 'review' ? (
                <span className="text-amber-400 font-medium">Exam Review Mode</span>
              ) : (
                <span>Question {currentIndex + 1} of {totalQuestions}</span>
              )}
            </div>
          </div>
        </div>

        {/* Center: Timer (Only in Exam Mode) */}
        {examMode === 'exam' && (
          <div className="flex items-center gap-2 bg-slate-950 px-3 py-1.5 rounded-lg border border-slate-800">
            <Timer className={`w-4 h-4 ${isLowTime ? 'text-rose-500 animate-pulse' : 'text-cyan-400'}`} />
            <span
              className={`font-mono text-sm md:text-base font-bold ${
                isLowTime ? 'text-rose-400' : 'text-slate-100'
              }`}
            >
              {formatTime(timeRemainingSeconds)}
            </span>
            <button
              onClick={onTogglePause}
              className="text-slate-500 hover:text-slate-300 transition ml-1"
              title={isPaused ? 'Resume Timer' : 'Pause Timer'}
            >
              {isPaused ? <Play className="w-3.5 h-3.5 text-emerald-400" /> : <Pause className="w-3.5 h-3.5" />}
            </button>
          </div>
        )}

        {/* Right Action Buttons */}
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={onOpenGrid}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-medium transition"
            title="Question Matrix"
          >
            <LayoutGrid className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Review Grid</span>
          </button>

          <button
            type="button"
            onClick={onOpenHub}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-medium transition"
            title="Peer Review Portal"
          >
            <Users className="w-3.5 h-3.5 text-cyan-400" />
            <span className="hidden md:inline">Contributor Hub</span>
          </button>

          {examMode === 'exam' && (
            <button
              type="button"
              onClick={onFinishExam}
              className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-xs font-semibold shadow-md shadow-cyan-500/20 transition"
            >
              <CheckSquare className="w-3.5 h-3.5" />
              <span>Finish Exam</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

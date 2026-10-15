import React, { useEffect } from 'react';
import type { ExamResult } from '../types/exam';
import confetti from 'canvas-confetti';
import { Award, XCircle, RotateCcw, Eye, ArrowRight } from 'lucide-react';

interface ScoreReportProps {
  result: ExamResult;
  onReviewAnswers: () => void;
  onRetake: () => void;
  onGoToHub: () => void;
}

export const ScoreReport: React.FC<ScoreReportProps> = ({
  result,
  onReviewAnswers,
  onRetake,
  onGoToHub,
}) => {
  useEffect(() => {
    if (result.passed) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
      });
    }
  }, [result.passed]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}m ${secs}s`;
  };

  const getBarColor = (pct: number) => {
    if (pct >= 80) return 'bg-emerald-500';
    if (pct >= 65) return 'bg-amber-500';
    return 'bg-rose-500';
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8 animate-in fade-in duration-300">
      {/* Banner Card */}
      <div
        className={`p-8 rounded-2xl border text-center space-y-4 shadow-2xl ${
          result.passed
            ? 'bg-gradient-to-b from-emerald-950/40 to-slate-900 border-emerald-500/50'
            : 'bg-gradient-to-b from-rose-950/40 to-slate-900 border-rose-500/50'
        }`}
      >
        <div className="inline-flex p-3 rounded-full bg-slate-950 border border-slate-800 shadow-inner">
          {result.passed ? (
            <Award className="w-12 h-12 text-emerald-400" />
          ) : (
            <XCircle className="w-12 h-12 text-rose-400" />
          )}
        </div>

        <div>
          <h2 className="text-2xl md:text-3xl font-bold tracking-tight text-white">
            {result.passed ? 'CONGRATULATIONS! PASS' : 'EXAM RESULT: DID NOT PASS'}
          </h2>
          <p className="text-sm text-slate-400 mt-1">
            Cisco Certified Network Associate (CCNA 200-301 v1.1) Exam Simulation
          </p>
        </div>

        {/* Score Numbers */}
        <div className="flex justify-center items-baseline gap-2 pt-2">
          <span className="text-5xl md:text-6xl font-black font-mono tracking-tight text-white">
            {result.scaledScore}
          </span>
          <span className="text-slate-400 text-lg font-medium">/ 1000</span>
        </div>

        <div className="flex flex-wrap justify-center items-center gap-6 text-xs text-slate-300 pt-2 border-t border-slate-800/80">
          <div>
            <span className="text-slate-500 block">Required Passing Score</span>
            <span className="font-semibold text-white">{result.passingScore} / 1000</span>
          </div>
          <div>
            <span className="text-slate-500 block">Correct Answers</span>
            <span className="font-semibold text-white">{result.totalCorrect} / {result.totalQuestions}</span>
          </div>
          <div>
            <span className="text-slate-500 block">Time Elapsed</span>
            <span className="font-semibold text-white">{formatTime(result.timeSpentSeconds)}</span>
          </div>
        </div>
      </div>

      {/* Official Domain Score Breakdown */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl space-y-5">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <h3 className="text-base font-semibold text-white">Performance by Exam Topic Domain</h3>
          <span className="text-xs text-slate-400">Target Passing: 82.5%</span>
        </div>

        <div className="space-y-4">
          {result.domainScores.map((domain) => (
            <div key={domain.domainId} className="space-y-1.5">
              <div className="flex justify-between text-xs md:text-sm">
                <span className="text-slate-300 font-medium">
                  {domain.domainId} {domain.name} <span className="text-slate-500 font-normal">({(domain.weight * 100).toFixed(0)}% weight)</span>
                </span>
                <span className="font-mono font-semibold text-slate-200">
                  {domain.percentage.toFixed(0)}% ({domain.correct}/{domain.total})
                </span>
              </div>

              {/* Progress bar */}
              <div className="h-2.5 w-full bg-slate-950 rounded-full overflow-hidden border border-slate-800">
                <div
                  className={`h-full rounded-full transition-all duration-1000 ${getBarColor(domain.percentage)}`}
                  style={{ width: `${Math.max(4, domain.percentage)}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
        <button
          onClick={onReviewAnswers}
          className="flex items-center gap-2 px-5 py-2.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold shadow-lg shadow-cyan-500/20 transition text-sm"
        >
          <Eye className="w-4 h-4" />
          <span>Review All Answers & Explanations</span>
        </button>

        <button
          onClick={onRetake}
          className="flex items-center gap-2 px-5 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium border border-slate-700 transition text-sm"
        >
          <RotateCcw className="w-4 h-4" />
          <span>Retake New Exam</span>
        </button>

        <button
          onClick={onGoToHub}
          className="flex items-center gap-2 px-5 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium border border-slate-700 transition text-sm"
        >
          <span>Peer Review Portal</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

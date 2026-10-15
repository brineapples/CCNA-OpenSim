import React from 'react';
import type { Blueprint, DomainId } from '../types/exam';
import { Play, BookOpen, Users, Terminal, CheckCircle2, ShieldCheck, Zap } from 'lucide-react';

interface WelcomeScreenProps {
  blueprint: Blueprint;
  totalVettedQuestions: number;
  onStartExam: (domainFilter?: DomainId | 'all') => void;
  onOpenHub: () => void;
}

export const WelcomeScreen: React.FC<WelcomeScreenProps> = ({
  blueprint,
  totalVettedQuestions,
  onStartExam,
  onOpenHub,
}) => {
  return (
    <div className="max-w-4xl mx-auto space-y-10 py-6 animate-in fade-in duration-300">
      {/* Hero Section */}
      <div className="text-center space-y-4">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/80 border border-cyan-800 text-cyan-300 text-xs font-semibold">
          <Zap className="w-3.5 h-3.5 text-cyan-400" />
          <span>Updated for Cisco CCNA v1.1 (2024 Exam Objectives)</span>
        </div>

        <h1 className="text-4xl md:text-6xl font-black text-white tracking-tight leading-none">
          CCNA <span className="text-cyan-400">OpenSim</span>
        </h1>

        <p className="text-base md:text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
          The free, community-powered Cisco 200-301 practice exam platform. Practice realistic questions, interactive IOS CLI simlets, and drag-and-drop challenges with zero paywalls.
        </p>

        {/* Primary CTA Buttons */}
        <div className="flex flex-wrap items-center justify-center gap-3 pt-3">
          <button
            onClick={() => onStartExam('all')}
            className="flex items-center gap-2 px-7 py-3.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-sm shadow-xl shadow-cyan-500/25 transition transform active:scale-95"
          >
            <Play className="w-4 h-4 fill-slate-950" />
            <span>Start Full Exam Simulation (120 Min)</span>
          </button>

          <button
            onClick={onOpenHub}
            className="flex items-center gap-2 px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 font-semibold text-sm border border-slate-700 transition"
          >
            <Users className="w-4 h-4 text-cyan-400" />
            <span>Peer Review & Audit Hub</span>
          </button>
        </div>
      </div>

      {/* Feature Highlights Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-cyan-950 border border-cyan-800 flex items-center justify-center text-cyan-400">
            <Terminal className="w-5 h-5" />
          </div>
          <h3 className="text-base font-semibold text-white">IOS Simlets & CLI</h3>
          <p className="text-xs text-slate-400 leading-relaxed">
            Troubleshoot scenarios directly with a mock Cisco IOS terminal. Run `show` commands with tab completion and history.
          </p>
        </div>

        <div className="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-blue-950 border border-blue-800 flex items-center justify-center text-blue-400">
            <CheckCircle2 className="w-5 h-5" />
          </div>
          <h3 className="text-base font-semibold text-white">Cisco Scaled Scoring</h3>
          <p className="text-xs text-slate-400 leading-relaxed">
            Get an official-style score report (300-1000 scale, 825 passing mark) with domain breakdowns matching Cisco's weighting.
          </p>
        </div>

        <div className="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-purple-950 border border-purple-800 flex items-center justify-center text-purple-400">
            <ShieldCheck className="w-5 h-5" />
          </div>
          <h3 className="text-base font-semibold text-white">100% Client-Side</h3>
          <p className="text-xs text-slate-400 leading-relaxed">
            Hosted statically on GitHub Pages. No logins, no tracking, works completely offline as a progressive web app.
          </p>
        </div>
      </div>

      {/* Practice by Specific Domain Section */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-6 shadow-xl">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-4">
          <div>
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-cyan-400" />
              <span>Practice by Exam Domain</span>
            </h2>
            <p className="text-xs text-slate-400 mt-1">
              Focus your study on a specific Cisco 200-301 domain:
            </p>
          </div>
          <span className="text-xs text-cyan-400 font-mono">
            {totalVettedQuestions} Total Active Questions
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {blueprint.domains.map((dom) => (
            <button
              key={dom.id}
              onClick={() => onStartExam(dom.id)}
              className="p-4 rounded-xl bg-slate-950 hover:bg-slate-800/80 border border-slate-800 hover:border-cyan-600 text-left transition group space-y-2"
            >
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono font-bold text-cyan-400">
                  Domain {dom.id}
                </span>
                <span className="text-[11px] text-slate-400 font-medium">
                  {(dom.weight * 100).toFixed(0)}%
                </span>
              </div>
              <div className="text-sm font-semibold text-slate-200 group-hover:text-white transition">
                {dom.name}
              </div>
              <div className="text-[11px] text-slate-400 line-clamp-1">
                {dom.subtopics.length} subtopics
              </div>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

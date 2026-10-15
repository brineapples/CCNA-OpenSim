import React from 'react';
import type { Blueprint } from '../types/exam';
import { ExternalLink, Users, BookOpen, ArrowRight } from 'lucide-react';

interface CommunityHubProps {
  blueprint: Blueprint;
  totalVettedQuestions: number;
  onBackToExam: () => void;
}

export const CommunityHub: React.FC<CommunityHubProps> = ({
  blueprint,
  totalVettedQuestions,
  onBackToExam,
}) => {
  // Live published Google Form audit links for CCNA v1.1 domains
  const formLinks: Record<string, string> = {
    '1.0': 'https://docs.google.com/forms/d/e/1FAIpQLSd48XG-NDIOvwYg0hAcykn19wdmKQGIxyQ2sK0PjUzLJ2iuRA/viewform',
    '2.0': 'https://docs.google.com/forms/d/e/1FAIpQLSdg_0VhCLThGl_w0aUlGllHSkWOk6tgYhPZcOKBWTay3t80CA/viewform',
    '3.0': 'https://docs.google.com/forms/d/e/1FAIpQLSf_Ha5jnUiFEsmPECY5eVazOPXAJIyQ5-LtX5yE-3LbSPTJtw/viewform',
    '4.0': 'https://docs.google.com/forms/d/e/1FAIpQLScfSzQKMWFIltQVhHKiCy3vG9MhFjdzS4bgQO8-q1HhJ-T38Q/viewform',
    '5.0': 'https://docs.google.com/forms/d/e/1FAIpQLSdyTWWdxkHNpO0iIi6cn-Wth-spG_KLb1R4erm5NFbvvgV4Jw/viewform',
    '6.0': 'https://docs.google.com/forms/d/e/1FAIpQLSfFVHwcxDVcn-XbhZ-q5Dtydx9qqcnghXSwQrSFhFS-4a3yPg/viewform',
  };

  return (
    <div className="max-w-4xl mx-auto space-y-10 animate-in fade-in duration-300">
      {/* Hero Header */}
      <div className="bg-gradient-to-r from-cyan-950/40 via-slate-900 to-slate-900 border border-cyan-800/50 rounded-2xl p-6 md:p-8 space-y-4 shadow-xl">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950 border border-cyan-800 text-xs font-semibold text-cyan-300">
          <Users className="w-3.5 h-3.5" />
          <span>Open Source Peer Review Pipeline</span>
        </div>
        <h1 className="text-2xl md:text-4xl font-black text-white tracking-tight">
          Help Us Build a 400-Question Free Question Bank
        </h1>
        <p className="text-sm md:text-base text-slate-300 max-w-2xl leading-relaxed">
          CCNA OpenSim is 100% open-source and community-vetted. To avoid question fatigue, reviews are partitioned into <strong className="text-cyan-300">six forms</strong> where you can audit bite-sized 5-to-10 question clusters in minutes.
        </p>

        {/* Global Stats */}
        <div className="flex flex-wrap gap-6 pt-4 border-t border-slate-800 text-xs md:text-sm">
          <div>
            <span className="text-slate-500 block">Syllabus Version</span>
            <span className="font-semibold text-white">Cisco CCNA v1.1 (2024)</span>
          </div>
          <div>
            <span className="text-slate-500 block">Questions in Bank</span>
            <span className="font-semibold text-cyan-400 font-mono">{totalVettedQuestions} / 400 Target</span>
          </div>
          <div>
            <span className="text-slate-500 block">Hosting</span>
            <span className="font-semibold text-white">Static GitHub Pages (100% Free)</span>
          </div>
        </div>
      </div>

      {/* How it works for contributors */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-7 h-7 rounded-lg bg-cyan-950 border border-cyan-800 flex items-center justify-center text-cyan-400 font-bold text-xs">
            1
          </div>
          <h4 className="text-sm font-semibold text-white">Choose a Topic</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Pick whichever domain you're currently studying or feel confident in (e.g. OSPF, VLANs, or Automation).
          </p>
        </div>

        <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-7 h-7 rounded-lg bg-cyan-950 border border-cyan-800 flex items-center justify-center text-cyan-400 font-bold text-xs">
            2
          </div>
          <h4 className="text-sm font-semibold text-white">Audit 5–10 Questions</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Rate exam closeness (1-5), adjust difficulty, and check that Cisco CLI outputs and commands are technically accurate.
          </p>
        </div>

        <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="w-7 h-7 rounded-lg bg-cyan-950 border border-cyan-800 flex items-center justify-center text-cyan-400 font-bold text-xs">
            3
          </div>
          <h4 className="text-sm font-semibold text-white">Automated Live Sync</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Approved questions from Google Sheets are pulled automatically into GitHub and published to the live test!
          </p>
        </div>
      </div>

      {/* The 6 Forms List */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-bold text-white flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-cyan-400" />
            <span>Select a Form to Audit</span>
          </h3>
          <button
            onClick={onBackToExam}
            className="text-xs text-cyan-400 hover:text-cyan-300 font-medium flex items-center gap-1 transition"
          >
            <span>Back to Exam</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {blueprint.domains.map((domain) => (
            <div
              key={domain.id}
              className="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-xl p-5 flex flex-col justify-between space-y-4 transition group shadow-lg"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-800 text-cyan-300 border border-slate-700">
                    Domain {domain.id}
                  </span>
                  <span className="text-xs text-slate-400 font-medium">
                    {(domain.weight * 100).toFixed(0)}% Exam Weight • {domain.targetQuestions} Qs Target
                  </span>
                </div>
                <h4 className="text-base font-semibold text-white group-hover:text-cyan-300 transition">
                  {domain.name}
                </h4>
                <p className="text-xs text-slate-400 mt-2 line-clamp-2">
                  Includes: {domain.subtopics.map(s => s.code).join(', ')} ({domain.subtopics.length} subtopic clusters)
                </p>
              </div>

              <div className="pt-3 border-t border-slate-800/80 flex items-center justify-between">
                <span className="text-xs text-slate-500">
                  Google Form • ~5 min review
                </span>
                <a
                  href={formLinks[domain.id] || '#'}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-950 hover:bg-cyan-900 border border-cyan-800 text-cyan-300 text-xs font-medium transition shadow-sm"
                >
                  <span>Open Form</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

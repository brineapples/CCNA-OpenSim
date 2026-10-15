import React, { useState, useRef, useEffect } from 'react';
import { Terminal as TerminalIcon, RotateCcw } from 'lucide-react';
import type { SimletContext } from '../types/exam';

interface CiscoTerminalProps {
  simlet: SimletContext;
}

export const CiscoTerminal: React.FC<CiscoTerminalProps> = ({ simlet }) => {
  const [history, setHistory] = useState<Array<{ command: string; output: string }>>([
    {
      command: '',
      output: `Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.7(3)M2\nTechnical Support: http://www.cisco.com/techsupport\nType '?' or 'help' for available mock commands.\n`
    }
  ]);
  const [input, setInput] = useState('');
  const [cmdHistory, setCmdHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState<number>(-1);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [history]);

  const handleCommand = (e: React.FormEvent) => {
    e.preventDefault();
    const rawCmd = input.trim();
    if (!rawCmd) return;

    const lowerCmd = rawCmd.toLowerCase();
    let response = '';

    if (lowerCmd === 'clear') {
      setHistory([]);
      setInput('');
      return;
    }

    if (lowerCmd === '?' || lowerCmd === 'help') {
      const available = Object.keys(simlet.commandResponses);
      response = `Available commands in this scenario:\n  ${available.join('\n  ')}\n  clear`;
    } else {
      // Find matching response (exact or prefix match)
      const matchingKey = Object.keys(simlet.commandResponses).find(
        key => key.toLowerCase() === lowerCmd || lowerCmd.startsWith(key.toLowerCase())
      );

      if (matchingKey) {
        response = simlet.commandResponses[matchingKey];
      } else {
        response = `% Invalid input detected at '^' marker.\nType '?' to see commands loaded for this scenario.`;
      }
    }

    setHistory(prev => [...prev, { command: rawCmd, output: response }]);
    setCmdHistory(prev => [...prev, rawCmd]);
    setHistoryIndex(-1);
    setInput('');
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (cmdHistory.length === 0) return;
      const nextIndex = historyIndex === -1 ? cmdHistory.length - 1 : Math.max(0, historyIndex - 1);
      setHistoryIndex(nextIndex);
      setInput(cmdHistory[nextIndex]);
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex === -1) return;
      const nextIndex = historyIndex + 1;
      if (nextIndex >= cmdHistory.length) {
        setHistoryIndex(-1);
        setInput('');
      } else {
        setHistoryIndex(nextIndex);
        setInput(cmdHistory[nextIndex]);
      }
    } else if (e.key === 'Tab') {
      e.preventDefault();
      // Simple tab autocomplete
      const match = Object.keys(simlet.commandResponses).find(cmd =>
        cmd.toLowerCase().startsWith(input.toLowerCase())
      );
      if (match) {
        setInput(match);
      }
    }
  };

  const handleReset = () => {
    setHistory([
      {
        command: '',
        output: `Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.7(3)M2\nTechnical Support: http://www.cisco.com/techsupport\nType '?' or 'help' for available mock commands.\n`
      }
    ]);
    setInput('');
  };

  return (
    <div 
      className="rounded-lg border border-slate-700 bg-slate-950 shadow-2xl overflow-hidden font-mono text-xs md:text-sm my-4"
      onClick={() => inputRef.current?.focus()}
    >
      {/* Terminal Title Bar */}
      <div className="flex items-center justify-between px-3 py-2 bg-slate-900 border-b border-slate-800 text-slate-300">
        <div className="flex items-center gap-2">
          <TerminalIcon className="w-4 h-4 text-cyan-400" />
          <span className="font-semibold text-slate-200">{simlet.deviceName} (Console Session)</span>
          <span className="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800">Mock IOS CLI</span>
        </div>
        <button
          type="button"
          onClick={(e) => {
            e.stopPropagation();
            handleReset();
          }}
          className="flex items-center gap-1 text-xs text-slate-400 hover:text-white px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 transition"
          title="Reset Terminal"
        >
          <RotateCcw className="w-3 h-3" />
          <span>Reset</span>
        </button>
      </div>

      {/* Terminal Body */}
      <div className="p-3 max-h-72 overflow-y-auto space-y-2 select-text">
        {history.map((item, idx) => (
          <div key={idx} className="space-y-1">
            {item.command && (
              <div className="flex items-center gap-1 text-slate-100">
                <span className="text-cyan-400 font-bold">{simlet.promptString}</span>
                <span>{item.command}</span>
              </div>
            )}
            {item.output && (
              <pre className="text-slate-300 whitespace-pre-wrap leading-relaxed">
                {item.output}
              </pre>
            )}
          </div>
        ))}

        {/* Input prompt */}
        <form onSubmit={handleCommand} className="flex items-center gap-1 pt-1">
          <span className="text-cyan-400 font-bold">{simlet.promptString}</span>
          <input
            ref={inputRef}
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            className="flex-1 bg-transparent text-slate-100 focus:outline-none caret-cyan-400 font-mono text-xs md:text-sm"
            placeholder="Type 'show ...' or '?' for commands"
            autoComplete="off"
            spellCheck={false}
          />
        </form>
        <div ref={bottomRef} />
      </div>

      <div className="px-3 py-1 bg-slate-900/60 border-t border-slate-800/80 text-[11px] text-slate-400 flex justify-between">
        <span>Press <kbd className="px-1 py-0.5 bg-slate-800 rounded text-slate-300">Tab</kbd> to autocomplete, <kbd className="px-1 py-0.5 bg-slate-800 rounded text-slate-300">?</kbd> for help</span>
        <span>Device: {simlet.deviceName}</span>
      </div>
    </div>
  );
};

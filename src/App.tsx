import { useExamEngine } from './hooks/useExamEngine';
import { ExamHeader } from './components/ExamHeader';
import { WelcomeScreen } from './components/WelcomeScreen';
import { QuestionCard } from './components/QuestionCard';
import { ScoreReport } from './components/ScoreReport';
import { CommunityHub } from './components/CommunityHub';
import { QuestionGridModal } from './components/QuestionGridModal';
import { ChevronLeft, ChevronRight, CheckSquare, Home } from 'lucide-react';

export function App() {
  const {
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
    startExam,
    handleAnswerChange,
    handleFinishExam,
    handleResetSession,
    examResult,
    blueprint,
    totalVettedQuestions,
  } = useExamEngine();

  const currentQuestion = questions[currentIndex];

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans">
      {/* Header bar (Visible during Exam or Review) */}
      {(viewMode === 'exam' || viewMode === 'review') && (
        <ExamHeader
          currentIndex={currentIndex}
          totalQuestions={questions.length}
          timeRemainingSeconds={timeRemaining}
          isPaused={isPaused}
          onTogglePause={() => setIsPaused(!isPaused)}
          onOpenGrid={() => setIsGridOpen(true)}
          onOpenHub={() => setViewMode('hub')}
          onFinishExam={() => {
            if (window.confirm('Are you sure you want to finish the exam and calculate your score?')) {
              handleFinishExam();
            }
          }}
          examMode={viewMode === 'review' ? 'review' : 'exam'}
        />
      )}

      {/* Main Container */}
      <main className="flex-1 max-w-5xl w-full mx-auto p-4 md:p-6 flex flex-col justify-between">
        {/* VIEW 1: Welcome Screen */}
        {viewMode === 'welcome' && (
          <WelcomeScreen
            blueprint={blueprint}
            totalVettedQuestions={totalVettedQuestions}
            onStartExam={(dom) => startExam(dom)}
            onOpenHub={() => setViewMode('hub')}
          />
        )}

        {/* VIEW 2: Community & Peer Review Hub */}
        {viewMode === 'hub' && (
          <CommunityHub
            blueprint={blueprint}
            totalVettedQuestions={totalVettedQuestions}
            onBackToExam={() => {
              if (questions.length > 0) {
                setViewMode('exam');
              } else {
                setViewMode('welcome');
              }
            }}
          />
        )}

        {/* VIEW 3: Score Report */}
        {viewMode === 'results' && (
          <ScoreReport
            result={examResult}
            onReviewAnswers={() => {
              setCurrentIndex(0);
              setViewMode('review');
            }}
            onRetake={() => startExam()}
            onGoToHub={() => setViewMode('hub')}
          />
        )}

        {/* VIEW 4: Active Question Runner (Exam or Review) */}
        {(viewMode === 'exam' || viewMode === 'review') && currentQuestion && (
          <div className="space-y-6 animate-in fade-in duration-200">
            {/* Question Card */}
            <QuestionCard
              question={currentQuestion}
              userAnswer={answers[currentQuestion.id]}
              onAnswerChange={handleAnswerChange}
              showResults={viewMode === 'review'}
            />

            {/* Bottom Navigation Toolbar */}
            <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={handlePrev}
                  disabled={currentIndex === 0}
                  className="flex items-center gap-1 px-4 py-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-200 hover:bg-slate-800 disabled:opacity-30 disabled:pointer-events-none transition text-xs md:text-sm font-medium"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>Previous</span>
                </button>

                <button
                  type="button"
                  onClick={() => setIsGridOpen(true)}
                  className="px-3.5 py-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-300 hover:text-white transition text-xs md:text-sm font-medium"
                >
                  Question {currentIndex + 1} of {questions.length}
                </button>

                <button
                  type="button"
                  onClick={handleNext}
                  disabled={currentIndex === questions.length - 1}
                  className="flex items-center gap-1 px-4 py-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-200 hover:bg-slate-800 disabled:opacity-30 disabled:pointer-events-none transition text-xs md:text-sm font-medium"
                >
                  <span>Next</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>

              <div className="flex items-center gap-2">
                {viewMode === 'review' ? (
                  <button
                    type="button"
                    onClick={() => setViewMode('results')}
                    className="flex items-center gap-1.5 px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition text-xs md:text-sm font-medium border border-slate-700"
                  >
                    <span>Back to Score Report</span>
                  </button>
                ) : (
                  <button
                    type="button"
                    onClick={() => {
                      if (window.confirm('Finish exam and view your score?')) {
                        handleFinishExam();
                      }
                    }}
                    className="flex items-center gap-1.5 px-5 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold shadow-md shadow-cyan-500/20 transition text-xs md:text-sm"
                  >
                    <CheckSquare className="w-4 h-4" />
                    <span>Finish Exam</span>
                  </button>
                )}
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Question Grid Modal */}
      <QuestionGridModal
        isOpen={isGridOpen}
        onClose={() => setIsGridOpen(false)}
        questions={questions}
        answers={answers}
        currentIndex={currentIndex}
        onSelectQuestion={(idx) => setCurrentIndex(idx)}
      />

      {/* Global Footer */}
      <footer className="border-t border-slate-900 py-4 px-6 text-center text-xs text-slate-500 select-none">
        <div className="max-w-5xl mx-auto flex flex-wrap items-center justify-between gap-2">
          <span>CCNA OpenSim — Free & Open Source Cisco 200-301 v1.1 Practice Engine</span>
          <div className="flex items-center gap-4">
            <button
              onClick={() => handleResetSession()}
              className="hover:text-slate-300 flex items-center gap-1 transition"
            >
              <Home className="w-3 h-3" />
              <span>Reset & Home</span>
            </button>
            <button
              onClick={() => setViewMode('hub')}
              className="text-cyan-400 hover:underline"
            >
              Peer Review Google Forms
            </button>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;

import '../styles/globals.css';
import type { ReactNode } from 'react';

export const metadata = {
  title: 'Code Forge | PDF Offer Generator',
  description: 'Automatic commercial offer generator'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="ru">
      <body className="bg-[#232730] min-h-screen text-[#ececec] font-sans">
        <header className="w-full bg-[#232730] border-b-4 border-yellow-400 py-6 mb-8 shadow flex flex-col items-center">
          <div className="flex items-center gap-3 max-w-2xl w-full px-4">
            <span className="text-3xl" style={{filter: 'drop-shadow(0 2px 0 #4f46e5)'}}>🔨</span>
            <div>
              <h1 className="text-yellow-400 text-2xl sm:text-3xl font-extrabold tracking-wide leading-tight">
                Code Forge
              </h1>
              <div className="text-indigo-300 text-base font-normal -mt-1">Commercial Offer Generator</div>
            </div>
          </div>
        </header>
        <main className="max-w-2xl mx-auto px-4 w-full">{children}</main>
        <footer className="w-full text-center py-6 text-xs text-indigo-200 mt-12 border-t border-[#363d50]">
          &copy; {new Date().getFullYear()} Code Forge | FastAPI + Next.js • For portfolio
        </footer>
      </body>
    </html>
  );
}

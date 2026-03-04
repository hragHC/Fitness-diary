import sys

def refactor():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');": "/* Removed Google Font */",
        "body { background: #020617; font-family: 'Inter', sans-serif; color: #e2e8f0; margin: 0; overflow-x: hidden; }": "body { background: #000000; font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; color: #F2F2F7; margin: 0; overflow-x: hidden; }",
        ".glass-card { background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.05); }": ".glass-card { background: rgba(28, 28, 30, 0.6); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 20px; }",
        ".panel-title { font-size: 18px; font-weight: 900; letter-spacing: 0.12em; text-transform: uppercase; color: #cbd5e1; margin-bottom: 14px; display: block; }": ".panel-title { font-size: 15px; font-weight: 600; color: #8E8E93; margin-bottom: 8px; display: block; }",
        "<div id=\"auth-screen\" class=\"fixed inset-0 z-[100] bg-[#020617] flex flex-col items-center justify-center p-6\">": "<div id=\"auth-screen\" class=\"fixed inset-0 z-[100] bg-[#000000] flex flex-col items-center justify-center p-6\">",
        "<h2 class=\"text-slate-500 font-bold text-[10px] tracking-[0.3em] uppercase mb-4\">Security Challenge</h2>": "<h2 class=\"text-[#8E8E93] font-medium text-sm mb-4\">Enter Passcode</h2>",
        "class=\"bg-slate-900 border border-slate-800 rounded-2xl p-4 w-40 text-center text-3xl tracking-[0.4em] text-blue-500 outline-none focus:border-blue-500 transition-all\">": "class=\"bg-[#1C1C1E] border-none rounded-xl p-4 w-40 text-center text-3xl tracking-widest text-[#FFFFFF] outline-none transition-all\">",
        "<button id=\"unlock-btn\" class=\"mt-6 bg-blue-600 text-white font-black py-4 px-10 rounded-2xl text-xs uppercase tracking-widest active-tap\">Unlock OS</button>": "<button id=\"unlock-btn\" class=\"mt-6 bg-[#0A84FF] text-[#FFFFFF] font-semibold py-3 px-12 rounded-full text-base active-tap\">Unlock OS</button>",
        "<button onclick=\"localStorage.clear(); location.reload();\" class=\"mt-12 text-[8px] text-slate-700 uppercase tracking-widest\">Reset System Data</button>": "<button onclick=\"localStorage.clear(); location.reload();\" class=\"mt-12 text-xs text-[#8E8E93]\">Reset System Data</button>",
        "<div class=\"fixed top-0 left-0 w-full z-50 bg-slate-900/95 border-b border-slate-800 p-2\">": "<div class=\"fixed top-0 left-0 w-full z-50 bg-[#1C1C1E]/80 backdrop-blur-lg border-b border-white/10 p-2\">",
        "<div class=\"max-w-xl mx-auto\"><div class=\"w-full bg-slate-800 h-2 rounded-full overflow-hidden\"><div id=\"p-bar\" class=\"bg-blue-500 h-full transition-all duration-700\" style=\"width: 0%\"></div></div></div>": "<div class=\"max-w-xl mx-auto\"><div class=\"w-full bg-[#3A3A3C] h-2 rounded-full overflow-hidden\"><div id=\"p-bar\" class=\"bg-[#0A84FF] h-full transition-all duration-700\" style=\"width: 0%\"></div></div></div>",
        "<h1 class=\"text-2xl font-black italic uppercase leading-none\">Fitness<span id=\"brand-suffix\" class=\"text-blue-500\">OS</span></h1>": "<h1 class=\"text-3xl font-bold leading-none\">Fitness<span id=\"brand-suffix\" class=\"text-[#0A84FF]\">OS</span></h1>",
        "<div id=\"overall-grade\" class=\"text-5xl font-black text-emerald-400\">A+</div>": "<div id=\"overall-grade\" class=\"text-4xl font-bold text-[#30D158]\">A+</div>",
        "<div class=\"glass-card p-6 rounded-[2rem] border-b-4 border-blue-500/50 text-center\">": "<div class=\"glass-card p-6 rounded-[2rem] text-center\">",
        "<span class=\"panel-title text-blue-400\">Protein</span>": "<span class=\"panel-title text-[#0A84FF]\">Protein</span>",
        "<p class=\"text-4xl font-black\"><span id=\"total-p\">0</span>g</p>": "<p class=\"text-4xl font-bold\"><span id=\"total-p\">0</span>g</p>",
        "<div class=\"glass-card p-6 rounded-[2rem] border-b-4 border-slate-700 text-center\">": "<div class=\"glass-card p-6 rounded-[2rem] text-center\">",
        "<p class=\"text-4xl font-black\" id=\"total-cal\">0</p>": "<p class=\"text-4xl font-bold\" id=\"total-cal\">0</p>",
        "<button id=\"add-meal-btn\" class=\"bg-emerald-500 text-black font-black w-10 h-10 rounded-full shadow-lg text-xl active-tap\">+</button>": "<button id=\"add-meal-btn\" class=\"bg-[#30D158] text-[#FFFFFF] font-medium w-8 h-8 rounded-full shadow text-xl flex items-center justify-center active-tap\">+</button>",
        "<div id=\"workout-section\" class=\"glass-card p-6 rounded-[2rem] border-l-4 border-blue-500 mb-6\">": "<div id=\"workout-section\" class=\"glass-card p-6 rounded-[2rem] mb-6\">",
        "<span class=\"panel-title text-blue-400 m-0\">Workout AI</span>": "<span class=\"panel-title text-[#0A84FF] m-0\">Workout AI</span>",
        "<label class=\"bg-emerald-500 text-black font-black w-8 h-8 rounded-full flex items-center justify-center cursor-pointer active-tap\">": "<label class=\"bg-[#30D158] text-[#FFFFFF] font-medium w-8 h-8 rounded-full flex items-center justify-center cursor-pointer active-tap\">",
        "<button id=\"clear-workout-btn\" class=\"bg-red-500 text-white font-black w-8 h-8 rounded-full active-tap\">-</button>": "<button id=\"clear-workout-btn\" class=\"bg-[#FF453A] text-[#FFFFFF] font-medium w-8 h-8 rounded-full active-tap\">-</button>",
        "<div class=\"bg-slate-900/50 p-4 rounded-2xl border border-slate-800\">": "<div class=\"bg-[#1C1C1E] p-4 rounded-2xl border border-white/5\">",
        "<p class=\"text-blue-400 font-black text-xl mb-2\"><span id=\"work-val\">0</span>% Intensity</p>": "<p class=\"text-[#0A84FF] font-bold text-xl mb-2\"><span id=\"work-val\">0</span>% Intensity</p>",
        "<div id=\"workout-summary\" class=\"text-[11px] text-slate-300 font-mono italic\"></div>": "<div id=\"workout-summary\" class=\"text-sm text-[#F2F2F7]\"></div>",
        "<p id=\"workout-placeholder\" class=\"text-[10px] text-slate-500 uppercase font-bold tracking-widest text-center py-4\">Upload plan to analyze intensity</p>": "<p id=\"workout-placeholder\" class=\"text-sm text-[#8E8E93] text-center py-4\">Upload plan to analyze intensity</p>",
        "<div class=\"glass-card p-6 rounded-[2rem] mb-8 border-l-4 border-purple-500 flex justify-between items-center\">": "<div class=\"glass-card p-6 rounded-[2rem] mb-8 flex justify-between items-center\">",
        "<span class=\"panel-title text-purple-500 m-0\">Rest Mode</span>": "<span class=\"panel-title text-[#BF5AF2] m-0\">Rest Mode</span>",
        "<button id=\"rest-btn\" class=\"bg-slate-800 text-[10px] font-bold px-6 py-2 rounded-full border border-slate-700 active-tap uppercase\">Off</button>": "<button id=\"rest-btn\" class=\"bg-[#3A3A3C] text-sm font-medium px-6 py-2 rounded-full border border-white/10 active-tap\">Off</button>",
        "<button id=\"archive-btn\" class=\"w-full bg-white text-black font-black py-6 rounded-3xl uppercase text-lg tracking-widest italic shadow-xl active-tap\">Archive & Sync</button>": "<button id=\"archive-btn\" class=\"w-full bg-[#0A84FF] text-[#FFFFFF] font-semibold py-4 rounded-xl text-lg shadow-md active-tap\">Archive & Sync</button>",
        "<div id=\"macro-modal\" class=\"fixed inset-0 z-[110] hidden flex items-center justify-center p-4 bg-black/95 backdrop-blur-md\">": "<div id=\"macro-modal\" class=\"fixed inset-0 z-[110] hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-md\">",
        "<div class=\"glass-card w-full max-w-sm p-6 rounded-[2.5rem] border border-emerald-500/30\">": "<div class=\"glass-card w-full max-w-sm p-6 rounded-[2.5rem]\">",
        "<input id=\"m-name\" type=\"text\" placeholder=\"Meal Name\" class=\"w-full bg-slate-900 p-5 rounded-2xl mb-4 text-white outline-none\">": "<input id=\"m-name\" type=\"text\" placeholder=\"Meal Name\" class=\"w-full bg-[#1C1C1E] font-bold p-5 rounded-2xl mb-4 text-[#FFFFFF] outline-none\">",
        "<input id=\"m-p\" type=\"number\" placeholder=\"P\" class=\"bg-slate-900 p-5 rounded-2xl text-center font-black\">": "<input id=\"m-p\" type=\"number\" placeholder=\"P\" class=\"bg-[#1C1C1E] p-5 rounded-2xl text-center font-bold text-[#FFFFFF]\">",
        "<input id=\"m-c\" type=\"number\" placeholder=\"C\" class=\"bg-slate-900 p-5 rounded-2xl text-center font-black\">": "<input id=\"m-c\" type=\"number\" placeholder=\"C\" class=\"bg-[#1C1C1E] p-5 rounded-2xl text-center font-bold text-[#FFFFFF]\">",
        "<input id=\"m-f\" type=\"number\" placeholder=\"F\" class=\"bg-slate-900 p-5 rounded-2xl text-center font-black\">": "<input id=\"m-f\" type=\"number\" placeholder=\"F\" class=\"bg-[#1C1C1E] p-5 rounded-2xl text-center font-bold text-[#FFFFFF]\">",
        "<button id=\"close-modal-btn\" class=\"flex-1 bg-slate-800 py-4 rounded-2xl font-bold uppercase text-xs\">Cancel</button>": "<button id=\"close-modal-btn\" class=\"flex-1 bg-[#3A3A3C] text-[#FFFFFF] py-4 rounded-2xl font-semibold text-base\">Cancel</button>",
        "<button id=\"save-meal-btn\" class=\"flex-1 bg-emerald-500 text-black py-4 rounded-2xl font-black uppercase text-xs\">Log</button>": "<button id=\"save-meal-btn\" class=\"flex-1 bg-[#0A84FF] text-[#FFFFFF] py-4 rounded-2xl font-semibold text-base\">Log</button>",
        "<button onclick='window.fillMeal(${JSON.stringify(m)})' class=\"bg-slate-800 px-4 py-2 rounded-xl text-[10px] whitespace-nowrap border border-slate-700 text-slate-300 font-bold active-tap uppercase\">${m.name}</button>": "<button onclick='window.fillMeal(${JSON.stringify(m)})' class=\"bg-[#3A3A3C] px-4 py-2 rounded-full text-xs whitespace-nowrap text-[#FFFFFF] font-medium active-tap\">${m.name}</button>",
        "<div class=\"flex justify-between items-center bg-slate-900/60 p-4 rounded-2xl border border-slate-800\">": "<div class=\"flex justify-between items-center bg-[#1C1C1E] p-4 rounded-xl mb-2\">",
        "<p class=\"text-[11px] font-black uppercase truncate flex-1 text-slate-100\">${m.name}</p>": "<p class=\"text-sm font-semibold truncate flex-1 text-[#F2F2F7]\">${m.name}</p>",
        "<button onclick=\"window.removeMeal(${m.id})\" class=\"text-slate-600 text-[9px] font-black ml-4 uppercase\">Delete</button>": "<button onclick=\"window.removeMeal(${m.id})\" class=\"text-[#FF453A] text-xs font-semibold ml-4\">Delete</button>"
    }

    for k, v in replacements.items():
        if k not in content:
            print(f"Warning: String not found:\n{k}")
        content = content.replace(k, v)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    refactor()

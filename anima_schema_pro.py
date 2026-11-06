import tkinter as tk
from tkinter import messagebox
C = {"bg": "#000000", "card": "#111111", "accent": "#FFB300", "text": "#E0E0E0", "dim": "#555555"}
F = "Courier"
Q = [
    {"t": 1, "q": "Q1 [Noise]: Workspace landscape?", "o": [("Silence", 1), ("Lo-fi Beats", 2), ("Rain/Nature", 3), ("Cafe Hum", 4)]},
    {"t": 1, "q": "Q2 [Style]: Visual preferences?", "o": [("Minimalism", 1), ("Retro Analog", 2), ("Organic Materials", 3), ("Cyberpunk/Gothic", 4)]},
    {"t": 1, "q": "Q3 [Plans]: Social matrix over-saturates?", "o": [("Pivot to tasks", 1), ("Adapt/Mask", 2), ("Go Home", 3), ("Chaotic Variance", 4)]},
    {"t": 2, "q": "Q4 [Humor]: Conversational format?", "o": [("Sarcastic Irony", 1), ("Absurd Loops", 2), ("Analytical Data", 3), ("Uncalibrated Noise", 4)]},
    {"t": 2, "q": "Q5 [Stars]: Cosmic vacuum reaction?", "o": [("Existential Comfort", 1), ("Existential Dread", 2), ("Pure Physics", 3), ("Aesthetic Admiration", 4)]},
    {"t": 2, "q": "Q6 [Nostalgia]: Historical data logs?", "o": [("Permanently Live There", 1), ("Contextual Pitstop", 2), ("Active Avoidance", 3), ("System Log Only", 4)]},
    {"t": 2, "q": "Q7 [Narrative]: Tactical roles?", "o": [("Reluctant Hero", 1), ("Trickster Changer", 2), ("System Anchor", 3), ("Isolated Philosopher", 4)]},
    {"t": 3, "q": "Q8 [Role]: Optimization function?", "o": [("Blueprint Architect", 1), ("Social Catalyst", 2), ("System Anchor", 3), ("Lone Wolf", 4)]},
    {"t": 3, "q": "Q9 [Boundary]: Non-negotiable layer?", "o": [("Personal Time", 1), ("Technical Autonomy", 2), ("Environmental Solitude", 3), ("Interpersonal Trust", 4)]},
    {"t": 3, "q": "Q10 [Gift]: Processing upgrade?", "o": [("Logic Channels", 1), ("Empathy Transceivers", 2), ("Infinite Curiosity", 3), ("Absurd Humor", 4)]}
]
class AnimaApp:
    def __init__(self, r):
        self.r = r; r.title("ANIMA CORE"); r.geometry("520x680"); r.configure(bg=C["bg"])
        self.idx = -1; self.v = [0] * 10; self.sv = tk.IntVar(value=0)
        self.m = tk.Frame(r, bg=C["bg"]); self.m.pack(fill=tk.BOTH, expand=1, padx=25, pady=10)
        self.show_landing()
    def show_landing(self):
        self.idx = -1; [w.destroy() for w in self.m.winfo_children()]
        tk.Label(self.m, text="\n\n(O) ANIMA POD DETECTED\nID: ESP32-C3-ANIMA", font=(F, 11), bg=C["bg"], fg=C["text"]).pack(pady=20)
        card = tk.Frame(self.m, bg=C["card"], padx=20, pady=20, bd=1, relief=tk.SOLID); card.pack(fill=tk.X, pady=20)
        tk.Label(card, text="NO HUMAN MANIFEST PROFILE LINKED\n\nYour hardware requires a local 10-Question matrix alignment.", font=(F, 10), bg=C["card"], fg=C["text"], wraplength=400).pack()
        tk.Button(self.m, text="[ BEGIN TRIAL ]", font=(F, 11, "bold"), bg=C["bg"], fg=C["accent"], command=self.next_q).pack(pady=30)
    def render_q(self):
        [w.destroy() for w in self.m.winfo_children()]; data = Q[self.idx]
        tk.Label(self.m, text=f"PROGRESS TIER {data['t']}", font=(F, 9), bg=C["bg"], fg=C["accent"]).pack(anchor=tk.W, pady=10)
        tk.Label(self.m, text=data['q'], font=(F, 11), bg=C["bg"], fg=C["text"], wraplength=460).pack(anchor=tk.W, pady=10)
        self.sv.set(self.v[self.idx])
        for i, (txt, val) in enumerate(data['o']):
            rf = tk.Frame(self.m, bg=C["card"], bd=1, relief=tk.SOLID); rf.pack(fill=tk.X, pady=5)
            tk.Radiobutton(rf, text=f" {chr(65+i)}. {txt}", variable=self.sv, value=val, font=(F, 10), bg=C["card"], fg=C["text"], selectcolor=C["bg"]).pack(fill=tk.X, padx=10, pady=10)
        nf = tk.Frame(self.m, bg=C["bg"]); nf.pack(fill=tk.X, side=tk.BOTTOM, pady=20)
        tk.Button(nf, text="[ < PREVIOUS ]", command=self.prev_q).pack(side=tk.LEFT)
        tk.Button(nf, text="[ NEXT > ]", font=(F, 10, "bold"), fg=C["accent"], bg=C["bg"], command=self.next_q).pack(side=tk.RIGHT)
    def prev_q(self):
        self.idx -= 1; self.render_q() if self.idx >= 0 else self.show_landing()
    def next_q(self):
        if self.idx >= 0 and self.sv.get() == 0:
            messagebox.showwarning("ALERT", "Select an option."); return
        if self.idx >= 0: self.v[self.idx] = self.sv.get()
        self.idx += 1; self.render_q() if self.idx < 10 else self.show_compile()
    def show_compile(self):
        [w.destroy() for w in self.m.winfo_children()]
        tk.Label(self.m, text="\n[⚡] VECTOR COMPILE COMPLETE", font=(F, 12, "bold"), bg=C["bg"], fg=C["accent"]).pack(pady=10)
        card = tk.Frame(self.m, bg=C["card"], padx=20, pady=20, bd=1, relief=tk.SOLID); card.pack(fill=tk.X, pady=20)
        tk.Label(card, text=f"RAW DATA SCRUBBED [✓]\n\nVector Generated:\nV = {str(self.v)}", font=(F, 10), bg=C["card"], fg=C["text"]).pack()
        tk.Button(self.m, text="[ FLASH TO KEYRING POD ]", font=(F, 11, "bold"), bg=C["bg"], fg=C["accent"], command=lambda: messagebox.showinfo("BLE", "Payload written to ESP32-C3.")).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk(); app = AnimaApp(root); root.mainloop()
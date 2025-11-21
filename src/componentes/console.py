import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
from styles.colors import COLORS

class ConsoleComponent:
    def __init__(self, parent):
        self.parent = parent
        self.create_console()
    
    def create_console(self):
        log_header = ctk.CTkFrame(self.parent, fg_color="transparent", height=30)
        log_header.pack(fill="x", padx=15, pady=(12,0))

        self.console_label = ctk.CTkLabel(log_header, text="> SYSTEM LOG", 
                                          font=("Consolas", 12, "bold"), text_color=COLORS["text_soft"])
        self.console_label.pack(side="left")

        btn_clear = ctk.CTkButton(log_header, text="LIMPAR LOG", width=80, height=22,
                                  fg_color="transparent", border_width=1, 
                                  border_color=COLORS["border"], text_color=COLORS["text_soft"],
                                  hover_color=COLORS["accent"],
                                  font=("Segoe UI", 10, "bold"),
                                  command=self.clear_console)
        btn_clear.pack(side="right")
        
        self.console = scrolledtext.ScrolledText(self.parent, bg=COLORS["bg_panel"], fg=COLORS["text_soft"], 
                                                 insertbackground=COLORS["text_main"], relief="flat", 
                                                 borderwidth=0, font=("Consolas", 11))
        self.console.pack(fill="both", expand=True, padx=15, pady=5)
    
    def write_console(self, text):
        self.console.configure(state=tk.NORMAL)
        self.console.insert(tk.END, f">> {text}\n")
        self.console.see(tk.END)
        self.console.configure(state=tk.DISABLED)

    def clear_console(self):
        self.console.configure(state=tk.NORMAL)
        self.console.delete('1.0', tk.END)
        self.console.configure(state=tk.DISABLED)
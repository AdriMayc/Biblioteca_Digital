import customtkinter as ctk
from styles.colors import COLORS
from utils.helpers import safe_invoke, call_and_capture

class EmprestimosView:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.left_panel, fg_color="transparent")
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(self.frame, text="CONTROLE DE EMPRÉSTIMOS", font=("Segoe UI", 18, "bold"), text_color=COLORS["text_main"]).pack(pady=(30,25))

        self.emprestimo_user = ctk.CTkEntry(self.frame, placeholder_text="ID do Usuário", **self.app._get_entry_style())
        self.emprestimo_user.pack(pady=6, padx=25, fill="x")
        self.emprestimo_book = ctk.CTkEntry(self.frame, placeholder_text="ID do Livro", **self.app._get_entry_style())
        self.emprestimo_book.pack(pady=6, padx=25, fill="x")

        ctk.CTkFrame(self.frame, height=25, fg_color="transparent").pack()

        ctk.CTkButton(self.frame, text="REGISTRAR SAÍDA", command=self.action_emprestimo, **self.app._get_action_btn_style()).pack(pady=6, padx=25, fill="x")
        ctk.CTkButton(self.frame, text="REGISTRAR DEVOLUÇÃO", command=self.action_devolucao, **self.app._get_action_btn_style()).pack(pady=6, padx=25, fill="x")
        
        btn_sec_style = self.app._get_action_btn_style().copy()
        btn_sec_style["fg_color"] = "transparent"
        btn_sec_style["border_width"] = 1
        btn_sec_style["border_color"] = COLORS["accent"]
        btn_sec_style["text_color"] = COLORS["accent"]
        btn_sec_style["hover_color"] = COLORS["input_bg"]

        ctk.CTkButton(self.frame, text="HISTÓRICO", command=self.action_show_history, **btn_sec_style).pack(pady=6, padx=25, fill="x")
    
    def action_emprestimo(self):
        from componentes.emprestimos import registrar_emprestimo
        
        vals = [self.emprestimo_user.get(), self.emprestimo_book.get()]
        result, printed = safe_invoke(registrar_emprestimo, vals)
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(f"RESULTADO: {result}")

    def action_devolucao(self):
        from componentes.emprestimos import registrar_devolucao
        
        vals = [self.emprestimo_book.get()]
        result, printed = safe_invoke(registrar_devolucao, vals)
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(f"RESULTADO: {result}")

    def action_show_history(self):
        from componentes.emprestimos import listar_historico
        
        # CORREÇÃO: Chamamos a função 'listar_historico' formatada
        _, printed = call_and_capture(listar_historico)
        
        if printed: 
            self.app.write_console(printed)
        else: 
            self.app.write_console("Nenhum histórico disponível.")
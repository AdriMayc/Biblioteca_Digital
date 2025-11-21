import customtkinter as ctk
from styles.colors import COLORS
from utils.helpers import call_and_capture

class RelatoriosView:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.left_panel, fg_color="transparent")
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(self.frame, text="RELATÓRIOS DO SISTEMA", font=("Segoe UI", 18, "bold"), text_color=COLORS["text_main"]).pack(pady=(30,25))

        ctk.CTkFrame(self.frame, height=10, fg_color="transparent").pack()

        btn_style = self.app._get_action_btn_style().copy()
        btn_style["fg_color"] = "transparent"
        btn_style["border_width"] = 1
        btn_style["border_color"] = COLORS["border"]
        btn_style["text_color"] = COLORS["text_main"]
        btn_style["hover_color"] = COLORS["accent"]

        ctk.CTkButton(self.frame, text="LIVROS DISPONÍVEIS", command=self.action_rel_disponiveis, **btn_style).pack(pady=6, padx=25, fill="x")
        ctk.CTkButton(self.frame, text="LIVROS EMPRESTADOS", command=self.action_rel_emprestados, **btn_style).pack(pady=6, padx=25, fill="x")
        ctk.CTkButton(self.frame, text="HISTÓRICO GERAL", command=self.action_rel_historico, **btn_style).pack(pady=6, padx=25, fill="x")
    
    def action_rel_disponiveis(self):
        from componentes.relatorios import relatorio_livros_disponiveis
        from componentes.livros import livros
        
        if relatorio_livros_disponiveis:
            _, printed = call_and_capture(relatorio_livros_disponiveis, livros)
            if printed: self.app.write_console(printed)
        else: self.app.write_console("Relatório não disponível.")

    def action_rel_emprestados(self):
        from componentes.relatorios import relatorio_livros_emprestados
        from componentes.livros import livros
        
        if relatorio_livros_emprestados:
            _, printed = call_and_capture(relatorio_livros_emprestados, livros)
            if printed: self.app.write_console(printed)
        else: self.app.write_console("Relatório não disponível.")

    def action_rel_historico(self):
        from componentes.relatorios import relatorio_historico_completo
        from componentes.emprestimos import historico
        
        if relatorio_historico_completo:
            _, printed = call_and_capture(relatorio_historico_completo, historico)
            if printed: self.app.write_console(printed)
        else: self.app.write_console("Relatório não disponível.")
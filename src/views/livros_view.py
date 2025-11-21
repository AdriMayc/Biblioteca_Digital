import customtkinter as ctk
from styles.colors import COLORS

class LivrosView:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.left_panel, fg_color="transparent")
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(self.frame, text="GERENCIAR LIVROS", font=("Segoe UI", 18, "bold"), text_color=COLORS["text_main"]).pack(pady=(30,25))
        
        self.livro_id = ctk.CTkEntry(self.frame, placeholder_text="ID do Livro", **self.app._get_entry_style())
        self.livro_id.pack(pady=6, padx=25, fill="x")
        self.livro_titulo = ctk.CTkEntry(self.frame, placeholder_text="Título da Obra", **self.app._get_entry_style())
        self.livro_titulo.pack(pady=6, padx=25, fill="x")
        self.livro_autor = ctk.CTkEntry(self.frame, placeholder_text="Nome do Autor", **self.app._get_entry_style())
        self.livro_autor.pack(pady=6, padx=25, fill="x")

        ctk.CTkFrame(self.frame, height=25, fg_color="transparent").pack() 
        
        ctk.CTkButton(self.frame, text="ADICIONAR LIVRO", command=self.action_add_book, **self.app._get_action_btn_style()).pack(pady=6, padx=25, fill="x")
        
        btn_sec_style = self.app._get_action_btn_style().copy()
        btn_sec_style["fg_color"] = "transparent"
        btn_sec_style["border_width"] = 1
        btn_sec_style["border_color"] = COLORS["accent"]
        btn_sec_style["text_color"] = COLORS["accent"]
        btn_sec_style["hover_color"] = COLORS["input_bg"]

        ctk.CTkButton(self.frame, text="VER ACERVO", command=self.action_list_books, **btn_sec_style).pack(pady=6, padx=25, fill="x")
    
    def action_add_book(self):
        from utils.helpers import safe_invoke
        from componentes.livros import adicionar_livro
        
        vals = [self.livro_id.get(), self.livro_titulo.get(), self.livro_autor.get()]
        result, printed = safe_invoke(adicionar_livro, vals)
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(f"RESULTADO: {result}")

    def action_list_books(self):
        from utils.helpers import safe_invoke
        from componentes.livros import listar_livros
        
        result, printed = safe_invoke(listar_livros, [])
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(str(result))
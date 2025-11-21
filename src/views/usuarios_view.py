import customtkinter as ctk
from styles.colors import COLORS
from utils.helpers import safe_invoke

class UsuariosView:
    def __init__(self, app):
        self.app = app
        self.frame = ctk.CTkFrame(app.left_panel, fg_color="transparent")
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(self.frame, text="GERENCIAR USUÁRIOS", font=("Segoe UI", 18, "bold"), text_color=COLORS["text_main"]).pack(pady=(30,25))
        
        self.usuario_id = ctk.CTkEntry(self.frame, placeholder_text="ID Usuário", **self.app._get_entry_style())
        self.usuario_id.pack(pady=6, padx=25, fill="x")
        self.usuario_nome = ctk.CTkEntry(self.frame, placeholder_text="Nome Completo", **self.app._get_entry_style())
        self.usuario_nome.pack(pady=6, padx=25, fill="x")
        self.usuario_email = ctk.CTkEntry(self.frame, placeholder_text="Endereço de Email", **self.app._get_entry_style())
        self.usuario_email.pack(pady=6, padx=25, fill="x")

        ctk.CTkFrame(self.frame, height=25, fg_color="transparent").pack()
        
        ctk.CTkButton(self.frame, text="CADASTRAR", command=self.action_add_user, **self.app._get_action_btn_style()).pack(pady=6, padx=25, fill="x")
        
        btn_sec_style = self.app._get_action_btn_style().copy()
        btn_sec_style["fg_color"] = "transparent"
        btn_sec_style["border_width"] = 1
        btn_sec_style["border_color"] = COLORS["accent"]
        btn_sec_style["text_color"] = COLORS["accent"]
        btn_sec_style["hover_color"] = COLORS["input_bg"]
        
        ctk.CTkButton(self.frame, text="LISTAR TODOS", command=self.action_list_users, **btn_sec_style).pack(pady=6, padx=25, fill="x")
    
    def action_add_user(self):
        from componentes.usuarios import cadastrar_usuario
        
        vals = [self.usuario_id.get(), self.usuario_nome.get(), self.usuario_email.get()]
        result, printed = safe_invoke(cadastrar_usuario, vals)
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(f"RESULTADO: {result}")

    def action_list_users(self):
        from componentes.usuarios import listar_usuarios
        
        result, printed = safe_invoke(listar_usuarios, [])
        if printed: self.app.write_console(printed)
        if result is not None: self.app.write_console(str(result))
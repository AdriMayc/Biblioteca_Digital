import customtkinter as ctk
from styles.colors import COLORS, setup_theme
from componentes.console import ConsoleComponent

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        setup_theme()
        self.title("Biblioteca Digital")
        self.geometry("1100x700")
        self.configure(fg_color=COLORS["bg_base"])
        self.create_layout()
        self.console_component = ConsoleComponent(self.right_panel)
        
    def create_layout(self):
        # Barra de Título
        self.title_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=COLORS["bg_base"], height=50)
        self.title_frame.pack(fill="x", padx=0, pady=0)

        # Menu Superior
        self.create_menu()
        
        # Área Principal
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=40, pady=(0, 25))

        self.left_panel = ctk.CTkFrame(self.main_container, 
                                       fg_color=COLORS["bg_panel"], 
                                       border_width=1, 
                                       border_color=COLORS["border"], 
                                       corner_radius=8,
                                       width=350)
        self.left_panel.pack(side="left", fill="y", expand=False, padx=(0, 15))
        self.left_panel.pack_propagate(False) 

        self.right_panel = ctk.CTkFrame(self.main_container, 
                                        fg_color=COLORS["bg_panel"], 
                                        border_width=1, 
                                        border_color=COLORS["border"], 
                                        corner_radius=8)
        self.right_panel.pack(side="right", fill="both", expand=True)
        
    def create_menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(fill="x", padx=40, pady=(10, 15))
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)

        btn_menu_style = {
            "fg_color": "transparent",
            "hover_color": COLORS["accent"],
            "border_width": 1,
            "border_color": COLORS["border"],
            "text_color": COLORS["text_main"],
            "corner_radius": 6,
            "height": 32,
            "font": ("Segoe UI", 12, "bold")
        }

        self.btn_livros = ctk.CTkButton(self.menu_frame, text="LIVROS", command=lambda: self.show_view("livros"), **btn_menu_style)
        self.btn_usuarios = ctk.CTkButton(self.menu_frame, text="USUÁRIOS", command=lambda: self.show_view("usuarios"), **btn_menu_style)
        self.btn_emprestimos = ctk.CTkButton(self.menu_frame, text="EMPRÉSTIMOS", command=lambda: self.show_view("emprestimos"), **btn_menu_style)
        self.btn_relatorios = ctk.CTkButton(self.menu_frame, text="RELATÓRIOS", command=lambda: self.show_view("relatorios"), **btn_menu_style)

        self.btn_livros.grid(row=0, column=0, padx=5, sticky="ew")
        self.btn_usuarios.grid(row=0, column=1, padx=5, sticky="ew")
        self.btn_emprestimos.grid(row=0, column=2, padx=5, sticky="ew")
        self.btn_relatorios.grid(row=0, column=3, padx=5, sticky="ew")

        separator = ctk.CTkFrame(self, height=1, fg_color=COLORS["border"])
        separator.pack(fill="x", padx=40, pady=(0, 20))
    
    def write_console(self, text):
        self.console_component.write_console(text)
    
    def clear_console(self):
        self.console_component.clear_console()
    
    def _get_entry_style(self):
        return {
            "fg_color": COLORS["input_bg"], 
            "border_color": COLORS["input_border"],
            "text_color": COLORS["text_main"],
            "placeholder_text_color": COLORS["border"],
            "height": 38,
            "corner_radius": 6
        }
    
    def _get_action_btn_style(self):
        return {
            "fg_color": COLORS["accent"],
            "hover_color": COLORS["accent_hover"], 
            "text_color": "#FFFFFF",
            "height": 40,
            "font": ("Segoe UI", 13, "bold"),
            "corner_radius": 6
        }
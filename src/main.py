from views.base_view import App
from views.livros_view import LivrosView
from views.usuarios_view import UsuariosView
from views.emprestimos_view import EmprestimosView
from views.relatorios_view import RelatoriosView

# Importar funções (mantido igual ao original)
try:
    from componentes.livros import adicionar_livro, listar_livros, buscar_livro, remover_livro, marcar_disponibilidade, livros
except Exception:
    adicionar_livro = None
    listar_livros = None
    livros = []

try:
    from componentes.usuarios import cadastrar_usuario, listar_usuarios, buscar_usuario, remover_usuario, usuarios
except Exception:
    cadastrar_usuario = None
    listar_usuarios = None
    usuarios = {}

try:
    from componentes.emprestimos import registrar_emprestimo, registrar_devolucao, fila_emprestimos, historico, listar_historico
except Exception:
    registrar_emprestimo = None
    registrar_devolucao = None
    fila_emprestimos = []
    historico = []
    listar_historico = None

try:
    from componentes.relatorios import relatorio_livros_disponiveis, relatorio_livros_emprestados, relatorio_historico_completo
except Exception:
    relatorio_livros_disponiveis = None
    relatorio_livros_emprestados = None
    relatorio_historico_completo = None

class BibliotecaApp(App):
    def __init__(self):
        super().__init__()
        self.views = {}
        self.setup_views()
        self.show_view("livros")
    
    def setup_views(self):
        self.views["livros"] = LivrosView(self).frame
        self.views["usuarios"] = UsuariosView(self).frame
        self.views["emprestimos"] = EmprestimosView(self).frame
        self.views["relatorios"] = RelatoriosView(self).frame
    
    def show_view(self, name):
        for k, v in self.views.items():
            v.pack_forget()
        self.views[name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = BibliotecaApp()
    app.mainloop()
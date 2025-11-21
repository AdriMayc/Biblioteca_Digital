### 📂 `readmes/08-main.md`


Este módulo inicializa a aplicação **Biblioteca Digital**, integrando todas as views (Livros, Usuários, Empréstimos e Relatórios) em uma interface única baseada em CustomTkinter.

## 🔶 Objetivo

- Criar uma interface unificada para gerenciar livros, usuários e empréstimos.
- Permitir navegação entre diferentes seções da aplicação.
- Integrar funcionalidades de cadastro, remoção, busca e relatórios.
- Garantir que erros de importação de módulos não quebrem a aplicação, exibindo apenas views disponíveis.



## 🔶 Estrutura utilizada

- Views:
    - ``LivrosView`` → Gerenciamento de livros
    - ``UsuariosView`` → Gerenciamento de usuários
    - ``EmprestimosView`` → Registrar empréstimos e devoluções
    - ``RelatoriosView`` → Exibição de relatórios de livros e histórico

- Funções importadas com fallback seguro:
    - ``livros.py`` → ``adicionar_livro``, ``listar_livros``, ``buscar_livro``, ``remover_livro``, ``marcar_disponibilidade``
    - ``usuarios.py`` → ``cadastrar_usuario``, ``listar_usuarios``, ``buscar_usuario``, ``remover_usuario``
    - ``emprestimos.py`` → ``registrar_emprestimo``, ``registrar_devolucao``, ``listar_historico``
    - ``relatorios.py`` → ``relatorio_livros_disponiveis``, ``relatorio_livros_emprestados``, ``relatorio_historico_completo``


## 🔶 Funcionamento

- Cada view é instanciada dentro de self.views e exibida conforme show_view(name).
- Módulos que falharem ao importar são ignorados, mantendo a aplicação funcional.
- O método mainloop() do Tkinter mantém a aplicação rodando até o usuário fechar.

## 🔶 Resultado

- Interface modular e organizada.
- Integração completa entre livros, usuários, empréstimos e relatórios.
- Sistema robusto: falhas de importação não travam a aplicação.
- Estrutura pronta para expansão, adição de novas funcionalidades ou integração com banco de dados real.

<hr style="height:2px; background-color:#807f7e; border:none;">
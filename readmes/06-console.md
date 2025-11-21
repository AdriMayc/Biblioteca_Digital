### 📂 `readmes/06-console.md`


Este módulo implementa o **System Log** do aplicativo, um console integrado que permite acompanhar mensagens e eventos do sistema em tempo real, sem abrir janelas externas.

## 🔶 Objetivo

- Exibir logs de execução do aplicativo em tempo real.
- Permitir que o usuário visualize erros, status e informações de processamento.
- Possibilitar a limpeza do log com um botão dedicado.
- Integrar com a interface principal do app usando CustomTkinter.



## 🔶 Estrutura utilizada

- Componentes de UI:
    - ``CustomTkinter (ctk)`` para frames, labels e botões estilizados
    - ``tkinter.scrolledtext`` para área de log rolável

- Arquivo de estilos:
    - ``styles/colors.py`` para padronização de cores

- Classe principal:
    - ``ConsoleComponent``

- Métodos principais:
    - ``write_console(text)`` → Adiciona nova linha de log
    - ``clear_console()`` → Limpa todo o conteúdo do console


## 🔶 Como usar

```
from components.console import ConsoleComponent

console = ConsoleComponent(parent_frame)
console.write_console("Sistema iniciado")
console.write_console("Livro adicionado: Python 101")

```
> O System Log garante visibilidade contínua das operações do app e facilita a depuração sem depender do terminal externo.


<hr style="height:2px; background-color:#807f7e; border:none;">
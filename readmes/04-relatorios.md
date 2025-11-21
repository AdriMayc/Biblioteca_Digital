### 📂 `readmes/04-relatorios.md`

Este passo implementa o módulo de relatórios, responsável por gerar listagens de livros e histórico de movimentações em formato de tabela diretamente no **Console/Log da Interface.**

## 🔶 Objetivo

- Listar livros disponíveis com título, autor e ID.
- Listar livros emprestados com título, autor e ID.
- Gerar histórico completo de movimentações (empréstimos e devoluções), incluindo data, tipo e detalhes.
- Fornecer informações de forma legível, ajudando o usuário a ter controle total sobre o acervo e empréstimos.

## 🔶 Estrutura utilizada
- Funções principais:
    - ``relatorio_livros_disponiveis(lista_livros)``
    - ``relatorio_livros_emprestados(lista_livros)``
    - ``relatorio_historico_completo(lista_historico)``

- Módulo Python:
    - ``src/relatorios.py``

- Integração com:
    - ``livros`` (do módulo ``livros.py``)
    - ``historico`` (do módulo ``emprestimos.py``)


## 🔶 Interface
Para ilustrar o fluxo dentro do app, podemos dividir em três momentos principais:

1. App Limpo (tela inicial da seção Relatórios)

![](img/relatorios/limpo-relatorio.png)

2. Relatório de Livros Disponíveis

![](img/relatorios/disponivel-relatorio.png)

3. Relatório de Livros Emprestados

![](img/relatorios/emprestimo-relatorio.png)

4. Histórico Geral

![](img/relatorios/historico-relatorio.png)


## 🔶 Resultado

- Todos os relatórios exibem informações organizadas e fáceis de ler.
- Livros disponíveis e emprestados são claramente separados, ajudando no controle do acervo.
- Histórico completo mantém registro detalhado de todas as movimentações, com data, tipo de ação e envolvidos.
- Integração com o System Log da interface garante que o usuário visualize o fluxo em tempo real.


<hr style="height:2px; background-color:#807f7e; border:none;">
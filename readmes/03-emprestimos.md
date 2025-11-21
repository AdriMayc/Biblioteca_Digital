### 📂 `readmes/03-emprestimos.md`

Este passo implementa o módulo de **registro de empréstimos e devoluções**, responsável por gerenciar a circulação de livros da Biblioteca Digital, mantendo histórico completo e persistindo dados em JSON.


## 🔶 Objetivo

- Registrar empréstimos de livros, vinculando usuário e livro.
- Registrar devoluções e atualizar disponibilidade dos livros.
- Listar o histórico completo de movimentações, mostrando data, tipo (empréstimo/devolução), livro e usuário.
- Persistir todas as alterações em JSON, garantindo que o histórico e o status dos livros sejam mantidos.



## 🔶 Estrutura utilizada
- Funções principais:
    - ``registrar_emprestimo(id_usuario, id_livro)``
    - ``registrar_devolucao(id_livro)``
    - ``listar_historico()``

- Arquivos JSON:
    - ``emprestimos.json`` (histórico de movimentações)
    - ``livros.json`` (status atualizado dos livros)

- Módulo Python:
    - ``src/emprestimos.py``

- Integração com:
    - ``usuarios`` (do módulo ``usuarios.py``)
    - ``livros`` (do módulo ``livros.py``)


## 🔶 Interface
Para ilustrar o fluxo dentro do app, podemos dividir em três momentos principais:

1. App Limpo (tela inicial da seção Empréstimos/Devoluções)

![](img/emprestimo/limpo-emprestimo.png)

2. Registrando um Empréstimo e Capturando o Log

![](img/emprestimo/saida-emprestimo.png)

3. Registrando uma Devolução e Capturando o Log

![](img/emprestimo/devolucao-emprestimo.png)

4. Visualizando o Histórico de Movimentações

![](img/emprestimo/historico-emprestimo.png)


## 🔶 Resultado

- Empréstimos e devoluções atualizam automaticamente o status do livro em JSON.
- Histórico completo de movimentações é persistido e pode ser consultado a qualquer momento.
- Integração direta com o app, mostrando o fluxo completo do usuário, livro e movimentação no System Log.


<hr style="height:2px; background-color:#807f7e; border:none;">
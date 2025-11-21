### 📂 `readmes/01-livros.md`


Este passo implementa o módulo de **gerenciamento de livros**, responsável por armazenar, buscar, listar, remover e alterar disponibilidade dos livros da Biblioteca Digital.


## 🔶 Objetivo

- Adicionar livros ao acervo com ID único, título e autor.
- Remover livros pelo ID.
- Buscar livros pelo ID e exibir status de disponibilidade.
- Listar todos os livros cadastrados com seu status.
- Alterar a disponibilidade de um livro (disponível ↔ indisponível).
- Persistir todas as alterações em JSON, garantindo que os dados não sejam perdidos ao fechar o programa.



## 🔶 Estrutura utilizada
- Arquivo JSON para armazenamento persistente: ``livros.json``
- Módulo Python: ``src/livros.py``
- Funções principais:
    - ``adicionar_livro(id, titulo, autor)``
    - ``remover_livro(id)``
    - ``buscar_livro(id)``
    - ``listar_livros()``
    - ``marcar_disponibilidade(id)``


## 🔶 Interface
Para ilustrar o fluxo dentro do app, podemos dividir em três momentos principais:

1. App Limpo (tela inicial da seção Livros)

![](img/livro/limpo-livro.png)

2. Cadastrando um Livro e Capturando o Log

![](img/livro/cadastro-livro.png)

3. Visualizando o Acervo (Ver Livros)

![](img/livro/acervo-livro.png)


## 🔶 Resultado

- Livro cadastrado corretamente no JSON.
- Listagem mostra quantidade de livros e status.
- Alteração de disponibilidade é refletida no arquivo JSON.
- Integração direta com o app, mostrando o fluxo completo dentro da interface.


<hr style="height:2px; background-color:#807f7e; border:none;">
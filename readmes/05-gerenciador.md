### 📂 `readmes/05-gerenciador.md`


Este passo implementa o módulo de **gerenciamento de livros**, responsável por armazenar, buscar, listar, remover e alterar disponibilidade dos livros da Biblioteca Digital.


## 🔶 Objetivo

- Criar a pasta data/ caso não exista.
- Salvar listas ou dicionários em arquivos JSON com formatação legível.
- Carregar dados existentes de arquivos JSON, retornando lista vazia se não houver arquivo.
- Tratar erros de leitura/escrita e permitir uso de caracteres acentuados.



## 🔶 Funções principais
- ``garantir_pasta()`` → Garante que a pasta ``data/`` exista.
- ``carregar_json(nome_arquivo)`` → Retorna os dados de um arquivo JSON.
- ``salvar_json(nome_arquivo, dados)`` → Salva dados em JSON, com indentação e suporte a acentos.


## 🔶 Como usar

```
from componentes.gerenciador import carregar_json, salvar_json

dados = carregar_json("livros.json")       # Carrega lista de livros
dados.append({"id": 1, "titulo": "Python"}) 
salvar_json("livros.json", dados)          # Salva novamente

```
> Este módulo garante que qualquer alteração em livros, usuários ou empréstimos seja persistida automaticamente, permitindo que o sistema recupere os dados ao reiniciar.


<hr style="height:2px; background-color:#807f7e; border:none;">
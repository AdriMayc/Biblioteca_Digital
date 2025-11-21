# livros.py
# Adaptado para salvar dados automaticamente em JSON

from componentes.gerenciador import carregar_json, salvar_json

ARQUIVO = "livros.json"

livros = carregar_json(ARQUIVO)


def adicionar_livro(id, titulo, autor):
    print("\n--- Adicionar Livro ---")
    
    try:
        id = int(id)
    except ValueError:
        print("Erro: O ID precisa ser um número inteiro.")
        return "Erro de ID"

    for l in livros:
        if l["id"] == id:
            print(f"Erro: Já existe um livro com ID {id}.")
            return "ID Duplicado"

    livro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    }

    livros.append(livro)

    # Adicionou na lista? Salva no arquivo agora mesmo.
    salvar_json(ARQUIVO, livros)

    print(f"Livro '{titulo}' adicionado com sucesso!")
    return "Sucesso"


def remover_livro(id):
    print("\n--- Remover Livro ---")
    try:
        id = int(id)
    except:
        print("Erro: ID inválido.")
        return

    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            
            # Removeu da lista? Atualiza o arquivo.
            salvar_json(ARQUIVO, livros)
            
            print(f"Livro ID {id} removido.")
            return

    print("Livro não encontrado para remoção.")


def buscar_livro(id):
    print("\n--- Buscar Livro ---")
    try:
        id = int(id)
    except:
        print("ID inválido.")
        return

    for livro in livros:
        if livro["id"] == id:
            status = "Disponível" if livro["disponivel"] else "Indisponível"
            print(f"Encontrado: {livro['titulo']} - {livro['autor']} ({status})")
            return livro

    print("Livro não encontrado.")
    return None


def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print(f"Total de livros: {len(livros)}")
        for livro in livros:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"[ID {livro['id']}] {livro['titulo']} - {status}")


def marcar_disponibilidade(id):
    print("\n--- Alterar Disponibilidade ---")
    try:
        id = int(id)
    except:
        return

    for livro in livros:
        if livro["id"] == id:
            livro["disponivel"] = not livro["disponivel"]
            
            # Mudou o status? Salva no arquivo.
            salvar_json(ARQUIVO, livros)
            
            novo_status = "Disponível" if livro["disponivel"] else "Indisponível"
            print(f"Status de '{livro['titulo']}' alterado para: {novo_status}")
            return

    print("Livro não encontrado.")
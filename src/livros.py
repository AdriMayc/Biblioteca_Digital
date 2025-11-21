# livros.py

# Estrutura base: lista de dicionários
livros = []

def adicionar_livro(id, titulo, autor):
    livros = {
        "id":   id,
        "titulo":  titulo, 
        "autor":    autor,
        "disponivel":   True
    }
    livros.append(livros)
    return f"Livro '{titulo}' adicionado."


def remover_livro(id):
    for livro in livros:
        if livro[id] == id:
            livros.remove(livro)
            return f"Livro ID {id} removido."
    return "Livro não encontrado."


def buscar_livro(id):
    for livro in livros: # busca linear O(n)
        if livros["id"] == id:
            return livro
    return None


def listar_livros():
    return livros


def marcar_disponibilidade(id, status: bool):
    for livro in livros:
        if livro["id"] == id:
            livro["disponivel"] = status
            return f"Livro ID {id} atualizado para {'disponivel' if status else 'indisponivel'}."
    return "Livro não encontrado"


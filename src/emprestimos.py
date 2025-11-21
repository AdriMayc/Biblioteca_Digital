from datetime import datetime

# Estruturas de Dados Globais
fila_emprestimos = []  # Fila (FIFO) - O primeiro que pede é o primeiro a levar
historico = []         # Lista para guardar tudo que aconteceu

def registrar_emprestimo(id_usuario, id_livro, lista_livros):
    """
    Adiciona um pedido de empréstimo à fila se o livro estiver disponível.
    Complexidade: O(1) para inserir na fila.
    """
    # 1. Verifique na 'lista_livros' se o livro com 'id_livro' está com "disponivel": True
    # 2. Se SIM:
    #    - Adicione um dicionário à 'fila_emprestimos' com id_usuario, id_livro e data.
    #    - Marque o livro como "disponivel": False na 'lista_livros'.
    #    - Retorne "Empréstimo realizado".
    # 3. Se NÃO:
    #    - Retorne "Livro indisponível".
    pass

def registrar_devolucao(id_livro, lista_livros):
    """
    Registra a devolução e move do status de emprestado para o histórico.
    Complexidade: O(n) pois precisa buscar o livro na lista.
    """
    # 1. Busque o livro na 'lista_livros' e marque "disponivel": True.
    # 2. Registre essa ação na lista 'historico' (quem devolveu, qual livro, data).
    pass

def explicar_complexidade():
    print("Inserção na fila (append): O(1) - Rápido e direto.")
    print("Busca de livro (for loop): O(n) - Depende da quantidade de livros.")
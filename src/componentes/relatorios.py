# relatorios.py
# Gera listagens formatadas como TABELAS para o Console da Interface

from componentes.livros import livros
from componentes.emprestimos import historico


def relatorio_livros_disponiveis(lista_livros):
    """
    Lista todos os livros disponíveis em formato de tabela.
    """
    print("\n--- RELATÓRIO: LIVROS DISPONÍVEIS ---")
    
    if not lista_livros:
        print("A base de dados está vazia.")
        return 0

    # Cabeçalho da Tabela
    # :<5 = alinha à esquerda com 5 espaços
    # :<40 = alinha à esquerda com 40 espaços (para caber títulos longos)
    print(f"{'ID':<5} | {'TÍTULO':<40} | {'AUTOR'}")
    print("-" * 70)

    encontrados = 0
    for livro in lista_livros:
        if livro.get("disponivel") is True:
            print(f"{livro['id']:<5} | {livro['titulo']:<40} | {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro disponível (todos emprestados).")
    else:
        print("-" * 70)
        print(f"Total disponíveis: {encontrados}")
        
    return encontrados


def relatorio_livros_emprestados(lista_livros):
    """
    Lista todos os livros emprestados em formato de tabela.
    """
    print("\n--- RELATÓRIO: LIVROS EMPRESTADOS ---")
    
    if not lista_livros:
        print("A base de dados está vazia.")
        return 0

    print(f"{'ID':<5} | {'TÍTULO':<40} | {'AUTOR'}")
    print("-" * 70)

    encontrados = 0
    for livro in lista_livros:
        if livro.get("disponivel") is False:
            print(f"{livro['id']:<5} | {livro['titulo']:<40} | {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro emprestado no momento.")
    else:
        print("-" * 70)
        print(f"Total emprestados: {encontrados}")
        
    return encontrados


def relatorio_historico_completo(lista_historico):
    """
    Imprime todo o histórico em formato de tabela.
    """
    print("\n--- HISTÓRICO COMPLETO DE MOVIMENTAÇÕES ---")
    
    if not lista_historico:
        print("O histórico está vazio.")
        return 0

    # Cabeçalho
    print(f"{'DATA':<20} | {'AÇÃO':<12} | {'DETALHES'}")
    print("-" * 85)

    # Inverte a lista para mostrar o mais recente primeiro
    for item in lista_historico[::-1]:
        tipo = item.get("tipo", "N/A")
        data = item.get("data", "N/A")
        
        # Formata os detalhes
        titulo = item.get("livro_titulo", f"ID {item.get('livro_id')}")
        
        if tipo == "Empréstimo":
            user = item.get("usuario_nome", f"ID {item.get('usuario_id')}")
            detalhes = f"'{titulo}' -> {user}"
        else:
            detalhes = f"'{titulo}' devolvido"
            
        print(f"{data:<20} | {tipo:<12} | {detalhes}")
            
    return len(lista_historico)
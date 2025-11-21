# relatorios.py
# Gera listagens formatadas para o Console da Interface

# Importamos apenas para garantir que as listas existam, 
# mas as funções recebem os dados como argumentos da Interface.
from livros import livros
from emprestimos import historico


def relatorio_livros_disponiveis(lista_livros):
    """
    Lista todos os livros que estão disponíveis.
    """
    print("\n--- RELATÓRIO: LIVROS DISPONÍVEIS ---")
    encontrados = 0
    
    if not lista_livros:
        print("A base de dados de livros está vazia.")
        return 0

    for livro in lista_livros:
        if livro.get("disponivel") is True:
            print(f"[ID {livro['id']}] {livro['titulo']} | Autor: {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro disponível no momento (todos emprestados).")
    else:
        print(f"Total disponíveis: {encontrados}")
        
    return encontrados


def relatorio_livros_emprestados(lista_livros):
    """
    Lista todos os livros que estão atualmente emprestados.
    """
    print("\n--- RELATÓRIO: LIVROS EMPRESTADOS ---")
    encontrados = 0
    
    if not lista_livros:
        print("A base de dados de livros está vazia.")
        return 0

    for livro in lista_livros:
        if livro.get("disponivel") is False:
            print(f"[ID {livro['id']}] {livro['titulo']} | Autor: {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro emprestado no momento.")
    else:
        print(f"Total emprestados: {encontrados}")
        
    return encontrados


def relatorio_historico_completo(lista_historico):
    """
    Imprime todo o histórico.
    Adaptação: Tenta mostrar Nomes e Títulos se estiverem salvos no registro.
    """
    print("\n--- HISTÓRICO COMPLETO DE MOVIMENTAÇÕES ---")
    
    if not lista_historico:
        print("O histórico de movimentações está vazio.")
        return 0

    # Imprime do mais recente para o mais antigo (inverte a lista na visualização)
    # Se preferir ordem cronológica, remova o [::-1]
    for item in lista_historico[::-1]:
        tipo = item.get("tipo", "N/A")
        data = item.get("data", "N/A")
        
        # Tenta pegar titulo/nome se existir, senão pega o ID
        livro_display = item.get("livro_titulo", f"ID {item.get('livro_id')}")
        
        if tipo == "Empréstimo":
            user_display = item.get("usuario_nome", f"ID {item.get('usuario_id')}")
            print(f"[{data}] SAÍDA: '{livro_display}' -> {user_display}")
        
        elif tipo == "Devolução":
            print(f"[{data}] RETORNO: '{livro_display}' voltou ao acervo.")
            
    return len(lista_historico)
def relatorio_livros_disponiveis(lista_livros):
    """
    Lista todos os livros que estão disponíveis.
    Complexidade: O(n) pois percorre toda a lista de livros.
    """
    print("\n--- LIVROS DISPONÍVEIS ---")
    encontrados = 0
    
    for livro in lista_livros:
        if livro.get("disponivel") is True:
            # Imprime os detalhes do livro de forma limpa
            print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro disponível no momento.")
        
    return encontrados


def relatorio_livros_emprestados(lista_livros):
    """
    Lista todos os livros que estão atualmente emprestados.
    Complexidade: O(n) pois percorre toda a lista de livros.
    """
    print("\n--- LIVROS EMPRESTADOS ---")
    encontrados = 0
    
    for livro in lista_livros:
        if livro.get("disponivel") is False:
            # Imprime os detalhes do livro de forma limpa
            print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
            encontrados += 1
            
    if encontrados == 0:
        print("Nenhum livro emprestado no momento.")
        
    return encontrados

def relatorio_historico_completo(historico):
    """
    Imprime de forma formatada todo o histórico de empréstimos e devoluções.
    Complexidade: O(n) onde n é o número de itens no histórico.
    """
    print("\n--- HISTÓRICO COMPLETO DE MOVIMENTAÇÕES ---")
    if not historico:
        print("O histórico de movimentações está vazio.")
        return 0

    for item in historico:
        tipo = item.get("tipo", "N/A")
        livro_id = item.get("livro_id", "N/A")
        data = item.get("data", "N/A")
        
        if tipo == "Empréstimo":
            usuario_id = item.get("usuario_id", "N/A")
            print(f"[EMPRÉSTIMO] Livro ID: {livro_id} | Usuário ID: {usuario_id} | Data: {data}")
        
        elif tipo == "Devolução":
            print(f"[DEVOLUÇÃO] Livro ID: {livro_id} | Data: {data}")
            
    return len(historico)
from datetime import datetime

# Estruturas de Dados Globais
fila_emprestimos = []  # Fila (FIFO) - O primeiro que pede é o primeiro a levar
historico = []         # Lista para guardar tudo que aconteceu

def registrar_emprestimo(id_usuario, id_livro, lista_livros):
    """
    Adiciona um pedido de empréstimo à fila se o livro estiver disponível.
    Complexidade: O(1) para inserir na fila, O(n) para buscar o livro.
    """
    # 1. Buscar o livro e verificar a disponibilidade (O(n) - busca linear)
    livro_encontrado = None
    for livro in lista_livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break
    
    if livro_encontrado is None:
        return "Erro: Livro não encontrado."
        
    # 2. Se SIM, registra e atualiza
    if livro_encontrado["disponivel"]:
        
        # Cria o registro de empréstimo
        registro_emprestimo = {
            "tipo": "Empréstimo",
            "usuario_id": id_usuario,
            "livro_id": id_livro,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Adiciona à fila de empréstimos (O(1))
        fila_emprestimos.append(registro_emprestimo)
        
        # Adiciona ao histórico (para fins de registro completo)
        historico.append(registro_emprestimo)
        
        # Marca o livro como indisponível
        livro_encontrado["disponivel"] = False
        
        return "Empréstimo realizado com sucesso. Livro marcado como indisponível."
    
    # 3. Se NÃO, retorna indisponível
    else:
        return "Livro indisponível para empréstimo."


def registrar_devolucao(id_livro, lista_livros):
    """
    Registra a devolução e atualiza o status do livro.
    Complexidade: O(n) pois precisa buscar o livro na lista.
    """
    # 1. Busque o livro na 'lista_livros' e marque "disponivel": True.
    livro_encontrado = None
    for livro in lista_livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break
            
    if livro_encontrado is None:
        return "Erro: Livro não encontrado."
        
    # Se o livro for encontrado:
    if not livro_encontrado["disponivel"]: # Verifica se ele estava emprestado
        
        # Marca o livro como disponível
        livro_encontrado["disponivel"] = True
        
        # 2. Registre essa ação na lista 'historico'
        registro_devolucao = {
            "tipo": "Devolução",
            "livro_id": id_livro,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        historico.append(registro_devolucao)
        
        return "Devolução registrada com sucesso. Livro marcado como disponível."
        
    else:
        return "O livro já estava marcado como disponível."
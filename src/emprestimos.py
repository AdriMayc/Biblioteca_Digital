from datetime import datetime
from livros import livros   # Importa a lista de livros que está na memória
from usuarios import usuarios   # Importa o dicionário de usuários

# Estruturas de Dados Globais
fila_emprestimos = []   # fila FIFO
historico = []          # lista normal para log

def registrar_emprestimo(id_usuario, id_livro):
    print("\n--- Registrar Empréstimo ---")

    # 1. Conversão e Validação dos dados vindos da Interface
    try:
        id_usuario = int(id_usuario)
        id_livro = int(id_livro)
    except ValueError:
        print("Erro: Os IDs devem ser números inteiros.")
        return "Erro de Formato"

    # 2. Validar se Usuário existe
    if id_usuario not in usuarios:
        print(f"Erro: Usuário com ID {id_usuario} não encontrado.")
        return "Usuário Inexistente"

    # 3. Buscar o Livro na lista
    livro_encontrado = None
    for livro in livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print(f"Erro: Livro com ID {id_livro} não encontrado.")
        return "Livro Inexistente"

    # 4. Verificar disponibilidade
    if not livro_encontrado["disponivel"]:
        print(f"Indisponível: O livro '{livro_encontrado['titulo']}' já está emprestado.")
        return "Livro Ocupado"

    # 5. Registrar empréstimo
    # DICA: Adicionei o nome e título para o histórico ficar mais legível na tela
    nome_usuario = usuarios[id_usuario]['nome']
    titulo_livro = livro_encontrado['titulo']

    registro = {
        "tipo": "Empréstimo",
        "usuario_id": id_usuario,
        "usuario_nome": nome_usuario, 
        "livro_id": id_livro,
        "livro_titulo": titulo_livro,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    fila_emprestimos.append(registro)
    historico.append(registro)
    
    # Atualiza o status do livro para Indisponível
    livro_encontrado["disponivel"] = False

    print(f"Sucesso! '{titulo_livro}' emprestado para {nome_usuario}.")
    return "Sucesso"


def registrar_devolucao(id_livro):
    print("\n--- Registrar Devolução ---")

    # Validação da entrada
    try:
        id_livro = int(id_livro)
    except ValueError:
        print("Erro: ID do livro inválido.")
        return "Erro Formato"

    # Buscar livro
    livro_encontrado = None
    for livro in livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print("Erro: Livro não encontrado na base de dados.")
        return "Não Encontrado"

    if livro_encontrado["disponivel"]:
        print(f"Atenção: O livro '{livro_encontrado['titulo']}' já consta como disponível.")
        return "Já Disponível"

    # Registrar devolução
    livro_encontrado["disponivel"] = True

    registro = {
        "tipo": "Devolução",
        "livro_id": id_livro,
        "livro_titulo": livro_encontrado['titulo'],
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    historico.append(registro)

    print(f"Devolução confirmada: '{livro_encontrado['titulo']}' está disponível novamente.")
    return "Sucesso"


def listar_historico():
    # Essa função imprime no console, mas a Interface lê a lista 'historico' diretamente.
    # Mantivemos aqui para compatibilidade.
    print("\n=== Histórico de Empréstimos e Devoluções ===")

    if not historico:
        print("Nenhum registro encontrado.")
        return

    for evento in historico:
        print(evento)
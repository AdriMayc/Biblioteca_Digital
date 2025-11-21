from datetime import datetime
from componentes.livros import livros
from componentes.usuarios import usuarios
from componentes.gerenciador import carregar_json, salvar_json

ARQUIVO_EMPRESTIMOS = "emprestimos.json"
ARQUIVO_LIVROS = "livros.json"

fila_emprestimos = [] 
historico = carregar_json(ARQUIVO_EMPRESTIMOS)


def registrar_emprestimo(id_usuario, id_livro):
    
    print("\n--- Registrar Empréstimo ---")
    try:
        id_usuario = int(id_usuario)
        id_livro = int(id_livro)
    except ValueError:
        return "Erro de Formato"

    if id_usuario not in usuarios:
        return "Usuário Inexistente"

    livro_encontrado = None
    for livro in livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        return "Livro Inexistente"

    if not livro_encontrado["disponivel"]:
        return "Livro Ocupado"

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
    livro_encontrado["disponivel"] = False

    salvar_json(ARQUIVO_EMPRESTIMOS, historico)
    salvar_json(ARQUIVO_LIVROS, livros)

    print(f"Sucesso! '{titulo_livro}' emprestado.")
    return "Sucesso"

def registrar_devolucao(id_livro):

    try:
        id_livro = int(id_livro)
    except ValueError:
        return "Erro Formato"

    livro_encontrado = None
    for livro in livros:
        if livro.get("id") == id_livro:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        return "Não Encontrado"

    if livro_encontrado["disponivel"]:
        return "Já Disponível"

    livro_encontrado["disponivel"] = True

    registro = {
        "tipo": "Devolução",
        "livro_id": id_livro,
        "livro_titulo": livro_encontrado['titulo'],
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    historico.append(registro)
    salvar_json(ARQUIVO_EMPRESTIMOS, historico)
    salvar_json(ARQUIVO_LIVROS, livros)

    print(f"Devolução confirmada.")
    return "Sucesso"


def listar_historico():

    print("\n=== HISTÓRICO DE MOVIMENTAÇÕES ===")
    
    if not historico:
        print("Nenhum registro encontrado.")
        return

    # Inverte para mostrar o mais recente primeiro
    for i, evento in enumerate(historico[::-1]):
        data = evento.get('data', 'N/A')
        tipo = evento.get('tipo', 'N/A')
        
        print("=" * 40)
        print(f"REGISTRO #{len(historico) - i}")
        print("-" * 40)
        print(f"DATA:        {data}")
        print(f"TIPO:        {tipo}")
        
        # Mostra dados do livro
        livro_id = evento.get('livro_id')
        livro_tit = evento.get('livro_titulo', 'Desconhecido')
        print(f"LIVRO:       ID {livro_id} - {livro_tit}")
        
        # Se for empréstimo, mostra quem pegou
        if tipo == "Empréstimo":
            user_id = evento.get('usuario_id')
            user_nome = evento.get('usuario_nome', 'Desconhecido')
            print(f"USUÁRIO:     ID {user_id} - {user_nome}")
            
        print("=" * 40) 
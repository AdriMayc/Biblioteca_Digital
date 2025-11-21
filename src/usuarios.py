# usuarios.py

# Adaptado para receber dados da Interface Gráfica

# Estrutura base: dicionário de usuários
# Chave = ID (int), Valor = Dicionário com nome e email
usuarios = {}


def cadastrar_usuario(id, nome, email):
    print("\n--- Cadastrar Usuário ---")
    
    # 1. Validação: Tenta converter o ID para número
    try:
        id = int(id)
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")
        return "Erro ID Inválido"

    # 2. Validação: Verifica se já existe
    if id in usuarios:
        print(f"Erro: ID {id} já está cadastrado para outro usuário.")
        return "ID Duplicado"

    # 3. Validação: Campos vazios
    if not nome or not email:
        print("Erro: Nome e Email são obrigatórios.")
        return "Campos Vazios"

    usuarios[id] = {
        "nome": nome,
        "email": email
    }

    print(f"Usuário '{nome}' cadastrado com sucesso!")
    return "Sucesso"


def remover_usuario(id):
    print("\n--- Remover Usuário ---")
    
    try:
        id = int(id)
    except ValueError:
        print("Erro: ID inválido.")
        return

    if id in usuarios:
        removido = usuarios.pop(id)
        print(f"Usuário '{removido['nome']}' (ID {id}) removido.")
    else:
        print("Erro: Usuário não encontrado.")


def buscar_usuario(id):
    print("\n--- Buscar Usuário ---")
    
    try:
        id = int(id)
    except ValueError:
        print("Erro: ID inválido.")
        return None

    usuario = usuarios.get(id)  # O(1) 
    
    if usuario:
        print(f"Encontrado: ID {id} | {usuario['nome']} ({usuario['email']})")
        return usuario
    else:
        print("Usuário não encontrado.")
        return None


def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print(f"Total de usuários: {len(usuarios)}")
        for id, dados in usuarios.items():
            print(f"[ID {id}] {dados['nome']} | {dados['email']}")
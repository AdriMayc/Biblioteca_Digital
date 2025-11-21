# usuarios.py
# Adaptado para salvar dados em JSON e lidar com chaves numéricas

from componentes.gerenciador import carregar_json, salvar_json

ARQUIVO = "usuarios.json"

# JSON sempre salva chaves de dicionário como TEXTO (String).
# Precisamos converter de volta para INTEIRO ao carregar.
dados_brutos = carregar_json(ARQUIVO)

usuarios = {}

if isinstance(dados_brutos, list):
    # Se for lista vazia (primeira vez), inicia vazio
    usuarios = {}
else:
    # Se for dicionário, converte as chaves de string ("1") para int (1)
    for id_str, dados in dados_brutos.items():
        usuarios[int(id_str)] = dados


def cadastrar_usuario(id, nome, email):
    print("\n--- Cadastrar Usuário ---")
    
    try:
        id = int(id)
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")
        return "Erro ID Inválido"

    if id in usuarios:
        print(f"Erro: ID {id} já está cadastrado para outro usuário.")
        return "ID Duplicado"

    if not nome or not email:
        print("Erro: Nome e Email são obrigatórios.")
        return "Campos Vazios"

    usuarios[id] = {
        "nome": nome,
        "email": email
    }

    # SALVAR: Dicionários são salvos automaticamente no JSON
    salvar_json(ARQUIVO, usuarios)

    print(f"Usuário '{nome}' cadastrado e salvo com sucesso!")
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
        
        # SALVAR: Atualiza o arquivo após remover
        salvar_json(ARQUIVO, usuarios)
        
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

    usuario = usuarios.get(id)
    
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
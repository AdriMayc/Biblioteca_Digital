# usuarios.py

# Estrutura base: dicionário de usuários
usuarios = {}


def cadastrar_usuario(id, nome, email):
    if id in usuarios:
        return "ID já cadastrado"
    
    usuarios[id] = {
        "nome": nome,
        "email": email
    }
    return f"Usuário '{nome}' cadastrado."


def remover_usuario(id):
    if id in usuarios:
        usuarios.pop(id)
        return f"Usuário ID {id} removido."
    return "Usuário não encontrado"


def buscar_usuario(id):
    return usuarios.get(id) # O(1)


def listar_usuarios():
    return usuarios




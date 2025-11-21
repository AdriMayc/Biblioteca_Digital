import json
import os

# Define onde os arquivos vão ficar
PASTA_DADOS = "data"


def garantir_pasta():
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)


def carregar_json(nome_arquivo):

    garantir_pasta()
    caminho_completo = os.path.join(PASTA_DADOS, nome_arquivo)
    
    if not os.path.exists(caminho_completo):
        return [] # Retorna lista vazia por padrão se for o primeiro acesso
    
    try:
        with open(caminho_completo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception as e:
        print(f"Erro ao ler {nome_arquivo}: {e}")
        return []


def salvar_json(nome_arquivo, dados):
    
    garantir_pasta()
    caminho_completo = os.path.join(PASTA_DADOS, nome_arquivo)
    
    try:
        with open(caminho_completo, "w", encoding="utf-8") as arquivo:
            # ensure_ascii=False permite acentos (ç, ã, é) no arquivo
            # indent=4 deixa o arquivo bonitinho para ler
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar {nome_arquivo}: {e}")
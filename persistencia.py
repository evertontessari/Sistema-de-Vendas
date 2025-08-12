import json
import os

ARQUIVO_ESTOQUE = 'produtos.json'
ARQUIVO_VENDAS = 'vendas.json'

def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

def carregar_vendas():
    if os.path.exists(ARQUIVO_VENDAS):
        with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_vendas(vendas):
    with open(ARQUIVO_VENDAS, 'w', encoding='utf-8') as f:
        json.dump(vendas, f, indent=4, ensure_ascii=False)
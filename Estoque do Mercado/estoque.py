import os
from utils import data_hora

estoque = []

def cadastrar_produtos(nome, preco, qtd):
    data_cadastro = data_hora()
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": qtd,
        "data": data_cadastro
    }
    
    estoque.append(produto)
    print(f"\nProduto {nome} cadastrado com sucesso!\n")

def confere_produto(nome):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            if produto["quantidade"] > 0:
                return 1
            else:
                return 0
    return -1

def atualizar_estoque(pedido):
    for item in pedido:
        for produto in estoque:
            if produto["nome"].lower() == item["nome"].lower():
                produto["quantidade"] -= item["quantidade"]

def mostrar_estoque():
    if not estoque:
        print("\nEstoque vazio.\n")
        return
    
    print("========== Estoque Atual ==========\n")
    
    for produto in sorted(estoque, key=lambda p: p["nome"].lower()):
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Data e Hora: {produto['data']}\n")
        print("-" * 36)

def carregar_estoque():
    if not os.path.exists("estoque.csv"):
        print("Arquivo de estoque não encontrado.")
        return

    print("===== Conteúdo do Arquivo estoque.txt =====\n")
    with open("estoque.csv", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

def salvar_estoque():
    with open("estoque.csv", "w", encoding="utf-8") as arquivo:
        for produto in estoque:
            linha = f"{produto['nome']},{produto['preco']},{produto['quantidade']},{produto['data']}\n"
            arquivo.write(linha)

def salvar_estoque_formatado():
    with open("estoque_formatado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("===== Estoque Final Cadastrado =====\n\n")
        for produto in estoque:
            arquivo.write(f"Nome        : {produto['nome']}\n")
            arquivo.write(f"Preço       : R${produto['preco']:.2f}\n")
            arquivo.write(f"Quantidade  : {produto['quantidade']}\n")
            arquivo.write(f"Data e Hora : {produto['data']}\n")
            arquivo.write("-" * 36 + "\n\n")

def ler_estoque():
    if not os.path.exists("estoque.csv"):
        return  # Não faz nada se não houver arquivo

    with open("estoque.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                nome, preco, quantidade, data = linha.strip().split(",")
                produto = {
                    "nome": nome,
                    "preco": float(preco),
                    "quantidade": int(quantidade),
                    "data": data
                }
                estoque.append(produto)
            except ValueError:
                print(f"Erro ao ler a linha: {linha}")

import os
from utils import*
from estoque import*

def criar_pedido():
    pedido = []
    
    while True:
        limpar_tela()
        mostrar_estoque()
        
        nome = input("\nDigite o nome do produto que deseja comprar: ").strip()
        if nome == "":
            break

        status = confere_produto(nome)
        
        if status == -1:
            print("Produto não encontrado no estoque.")
            input("Pressione Enter para tentar novamente...")
            continue
        elif status == 0:
            print("Produto sem unidades disponíveis.")
            input("Pressione Enter para tentar novamente...")
            continue

        for produto in estoque:
            if produto["nome"].lower() == nome.lower():
                print(f"Quantidade disponível: {produto['quantidade']}")
                while True:
                    try:
                        qtd = int(input("Digite a quantidade desejada: "))
                        if 0 < qtd <= produto["quantidade"]:
                            pedido.append({"nome": nome, "quantidade": qtd})
                            break
                        else:
                            print("Quantidade inválida. Tente novamente.")
                    except ValueError:
                        print("Digite um número válido.")
                break

        continuar = input("\nDeseja comprar outro produto? (s/n): ").lower()
        if continuar != "s":
            break

    if not pedido:
        print("Nenhum item comprado.")
        input("Pressione Enter para voltar ao menu...")
        return

    # Imprime o pedido com data e hora
    limpar_tela()
    print("====== Pedido Realizado ======")
    print(f"Data: {data_hora()}\n")
    for item in pedido:
        print(f"Produto: {item['nome']} | Quantidade: {item['quantidade']}")
    print("\n==============================")
    
    atualizar_estoque(pedido)
    salvar_historico(pedido)
    
    input("\nPressione Enter para continuar...")

def salvar_historico(pedido):
    with open("historico.txt", "a", encoding="utf-8") as arq:
        arq.write(f"===== Pedido feito em {data_hora()} =====\n")
        for item in pedido:
            arq.write(f"Produto: {item['nome']} | Quantidade: {item['quantidade']}\n")
        arq.write("-" * 50 + "\n\n")

def mostrar_historico():
    if not os.path.exists("historico.txt"):
        print("Nenhum histórico encontrado.")
        input("Pressione Enter para voltar...")
        return

    print("===== Histórico de Pedidos =====\n")
    with open("historico.txt", "r", encoding="utf-8") as arq:
        print(arq.read())
    input("Pressione Enter para voltar...")
    
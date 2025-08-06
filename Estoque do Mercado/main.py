import os
import time
from utils import limpar_tela
from estoque import*
from pedido import*

def mostrar_menu():
    limpar_tela()
    print("=== Cadastro de Produtos ===\n")
    print("1 - Cadastrar produto")
    print("2 - Mostrar estoque")
    print("3 - Salvar estoque em arquivo")
    print("4 - Fazer pedido")
    print("5 - Ver histórico de pedidos")
    print("6 - Sair")

def main():
    while True:
        mostrar_menu()
        try:
            escolha = int(input("\nEscolha uma opção: "))
            limpar_tela()
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
    
        if escolha == 1:
            while True:
                limpar_tela()
                print("=== Cadastro de Produtos ===\n")
                n = input("Digite o nome do produto: ")
                if n == "":
                    break
                try:
                    p = float(input("Digite o preço do produto: "))
                    q = int(input("Digite a quantidade em estoque: "))
                except ValueError:
                    print("Entrada inválida. Digite números válidos.\n")
                    continue
                cadastrar_produtos(n, p, q)
                
                limpar_tela()
                continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
                if continuar != "s":
                    limpar_tela()
                    break
    
        elif escolha == 2:
            mostrar_estoque()
            input("\nPressione Enter para continuar...")
    
        elif escolha == 3:
            salvar_estoque()
            salvar_estoque_formatado()
            print("\nEstoque salvo com sucesso no arquivo 'estoque.txt'.")
            input("\nPressione Enter para continuar...")
    
        elif escolha == 4:
            criar_pedido()
            
        elif escolha == 5:
            mostrar_historico()
    
        elif escolha == 6:
            confirmar = input("Tem certeza que deseja sair? (s/n): ").lower()
            limpar_tela()
            if confirmar != 's':
                limpar_tela()
                continue
            
            salvar_estoque()
            salvar_estoque_formatado()
            limpar_tela()

            print("Saindo do programa...")
            break
    
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

ler_estoque()
main()

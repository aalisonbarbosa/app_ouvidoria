from operacoesbd import *

#Variável de opção
opcao = 0

while opcao != 7:
    print(
        "\n1. Listar manifestações\n2. Listar manifestações por tipo\n3. Criar manifestação\n4. Exibir quantidade de manifestações\n5. Visualizar manifestação pelo código\n6. Excluir manifestação por código\n7. Sair ")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print("Listar manifestações")

    elif opcao == 2:
        print("Listar manifestações por tipo")

    elif opcao == 3:
        print("Criar manifestação")

    elif opcao == 4:
        print("Exibir quantidade de manifestações")

    elif opcao == 5:
        print("Visualizar manifestação pelo código")

    elif opcao == 6:
        print("Excluir manifestação por código")

    else:
        print("Código inválido.")

print("Obrigado por utilizar nossa ouvidoria!")
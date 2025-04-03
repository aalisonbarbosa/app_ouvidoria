from operacoesbd import *
from metodos import *

conn =  criarConexao("localhost","root","12345", "app_ouvidoria")
opcao = 0 

print("🔰 Óla! Bem-vindo a ovidoria ")

while opcao != 7:
    print(f"{"="*30}\n            OPÇÕES            \n{"="*30}")
    print(
        "\n📋 1. Listar manifestações\n📝 2. Listar manifestações por tipo\n🆕 3. Criar manifestação\n👀 4. Exibir quantidade de manifestações\n🔎 5. Visualizar manifestação pelo código\n🗑️  6. Excluir manifestação por código\n🚪 7. Sair ")

    opcao = input("\nDigite sua opção: ")

    if validarNumero(opcao):
       opcao = int(opcao)
    else: 
        print("\n⚠️  Digite uma opção válida!")

    if opcao == 1:

        print(f"\n{"=" * 22} Manifestações {"=" * 22}\n")

        listandoManifestacoes = listarManifestacoes(conn)

        if len(listandoManifestacoes) == 0:
            print("\n❌ Não há manifestações cadastradas!")
        else:
            for manifestacao in listandoManifestacoes:
                print("\n💠 Categoria:",manifestacao [1],"\nAssunto:",manifestacao [2],"\nCodigo:",manifestacao [0])

    elif opcao == 2:
        
        categoria = escolherCategoria()
        
        if len(categoria) > 0:
            listarManifestacoesCategoria(conn, categoria)


    elif opcao == 3:

        categoria = escolherCategoria()
        assunto = input("\nDigite sua manifestação: ")

        criarManifestacao(conn,categoria, assunto)
        
        print("\n✅ Nova manifestação criada com sucesso!")

    elif opcao == 4:

        tamanhoListaManifestacoes = exibirQuantidadeManifestacoes(conn)

        print(f"\nNo momento temos {tamanhoListaManifestacoes[0][0]} manifestações cadastradas!")

    elif opcao == 5:
        pesquisarCodigo(conn)

    elif opcao == 6:
        remover(conn)
    else:
        print("\nCódigo inválido.")

print("🤝 Obrigado por utilizar nossa ouvidoria!")

encerrarConexao(conn)
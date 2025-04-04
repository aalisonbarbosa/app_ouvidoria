from metodos import *

conn =  criarConexao("localhost","root","casam10", "app_ouvidoria")
opcao = 0 

print("\n🔰 Olá, Bem-vindo a ovidoria!\n")

while opcao != 7:
    print(f"{'='*30}\n            OPÇÕES            \n{'='*30}")
    print("\n📋 1) Listar manifestações\n📝 2) Listar manifestações por tipo\n🆕 3) Criar manifestação\n👀 4) Exibir quantidade de manifestações\n🔎 5) Visualizar manifestação pelo código\n🗑️  6) Excluir manifestação por código\n🚪 7) Sair ")

    opcao = input("\nDigite sua opção: ")

    # verifica se a opção é um número válido
    if validarNumero(opcao):
       opcao = int(opcao)
    else: 
        print("\n⚠️  Digite uma opção válida!")

    if opcao == 1:

        print(f"\n{'=' * 23}\n     MANIFESTAÇÕES     \n{'=' * 23}\n")

        listaManifestacoes = listarManifestacoes(conn)

        if len(listaManifestacoes) == 0:
            print("❌ Não há manifestações cadastradas!\n")
        else:
            for manifestacao in listaManifestacoes:
                print(f"▫️  Categoria: {manifestacao [1]}\nAssunto: {manifestacao [2]}\nCódigo: {manifestacao [0]}\n")

    elif opcao == 2:
        
         # obtém categoria escolhida
        categoria = escolherCategoria()
        
        if len(categoria) > 0:
            print(f"\n{'=' * 23}\n     MANIFESTAÇÕES     \n{'=' * 23}\n")

            listarManifestacoesCategoria(conn, categoria)


    elif opcao == 3:

        # obtém categoria escolhida
        categoria = escolherCategoria()

        if len(categoria) > 0:
            assunto = input("Digite sua manifestação: ")

            criarManifestacao(conn,categoria, assunto)
        
            print("\n✅ Nova manifestação criada com sucesso!\n")

    elif opcao == 4:

        tamanhoListaManifestacoes = exibirQuantidadeManifestacoes(conn)

        print(f"\n🔎 No momento temos:\n{tamanhoListaManifestacoes[0]} Reclamações\n\n{tamanhoListaManifestacoes[1]} Sugestões\n\n{tamanhoListaManifestacoes[2]} Elogios\n\nNo total: {tamanhoListaManifestacoes[3]} manifestações cadastradas!")

    elif opcao == 5:

        pesquisarManifestacaoCodigo(conn)

    elif opcao == 6:

        removerManifestacao(conn)

    elif opcao != 7:

        print("\n⚠️  Digite um código válido!\n")

print("\n🤝 Obrigado por utilizar nossa ouvidoria!\n")

encerrarConexao(conn)
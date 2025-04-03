from operacoesbd import *

# função para verificar se um número é válido
def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

# função que solicita a escolha de uma categoria e a retorna
def escolherCategoria():
        print(f"\n{"="*22}\n      CATEGORIAS      \n{"="*22}\n ")
        print("1) Reclamação\n2) Sugestão\n3) Elogios\n")

        escolha = input("Escolha a categoria da manifestação: ")
        
        if not validarNumero(escolha):
            print("\n⚠️  Digite uma opção válida!\n")
            return ""
        else: 
            escolha = int(escolha)

            if escolha > 0 and escolha < 4:
                if escolha == 1:
                    categoria = "reclamação"
                elif escolha == 2:
                    categoria = "sugestão"
                elif escolha == 3:
                    categoria = "elogio"

                return categoria
            else:
                print("\n⚠️  Digite uma opção válida!\n")
                return ""

# função para listar todas as manifestações
def listarManifestacoes(conn):
    sql = "select * from manifestacoes"

    # pega todas as manifestações cadastradas no bd
    manifestacoes = listarBancoDados(conn, sql)

    return manifestacoes


# função para listar todas as manifestações da categoria escolhida 
def listarManifestacoesCategoria(conn, categoria):
    sql = "select * from manifestacoes where categoria = %s"
    dados = [categoria]

    manifestacoes =  listarBancoDados(conn, sql, dados)

    if len(manifestacoes) == 0:
        print("❌ Não há manifestações cadastradas!\n")
    else:
        for manifestacao in manifestacoes:
            print(F"▫️  Categoria: {manifestacao[1]}\nCódigo: {manifestacao[0]}\nAssunto: {manifestacao[2]}\n")


# função para criar uma nova manifestação
def criarManifestacao(conn, categoria, assunto):
    
    sql = "insert into manifestacoes(categoria, assunto)values(%s,%s)"
    dados = [categoria, assunto]

    insertNoBancoDados(conn, sql, dados)


# função para exibir a quantidade de manifestações cadastradas no bd
def exibirQuantidadeManifestacoes(conn):
    sql = "select count(*) from manifestacoes"

    # pega o número de manifestação cadastradas no bd
    quantidadeManifestacoes = listarBancoDados(conn, sql)

    return quantidadeManifestacoes


# função para pesquisar um manifestação pelo código
def pesquisarManifestacaoCodigo (conn):
    codigoPesquisa = input("Informe o codigo para pesquisa: ")
    
      # verifica se o código digitado é um número válido
    if not validarNumero(codigoPesquisa):
        print("\n⚠️  Digite um código válido!\n")
    else:
        # se o código digitado for um número válido ele executa as linhas debaixo
        codigoPesquisa = int(codigoPesquisa)
        sql = "select * from manifestacoes where id = (%s)"
        dados = [codigoPesquisa]
        manifestacao = listarBancoDados(conn, sql, dados)

        if len(manifestacao) == 0:
            print("\n❌ Manifestação não encontrada!\n")
        else:
            print(f"\n🔎 Categoria: {manifestacao[0][1]}\nAssunto: {manifestacao[0][2]}\nCódigo: {manifestacao[0][0]}\n")


# função para remover uma manifestação
def removerManifestacao(conn):
    codigoRemocao = input("Digite o código da manifestção a ser removida: ")
    
    # verifica se o código digitado é um número válido
    if not validarNumero(codigoRemocao):
        print("\n⚠️  Digite um código válido!\n")
    else:
        # se o código digitado for um número válido ele executa as linhas debaixo
        codigoRemocao = int(codigoRemocao)

        sql = "delete from manifestacoes where id = %s"
        dados = [codigoRemocao]

        linhasAfetadas = excluirBancoDados(conn,sql,dados)
        
        # verifica se houve alguma alteração no bd
        if linhasAfetadas == 0:
            print("\n❌ Nenhuma manifestação removida!\n")
        else:
            print("\n✅ Manifestação removida com sucesso!\n")

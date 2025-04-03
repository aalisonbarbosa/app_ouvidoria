from operacoesbd import *

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False




def escolherCategoria():
        print("======================")
        print("      CATEGORIAS      ")
        print("======================")
        print("1) Reclamação\n2) Sugestão\n3) Elogios")

        escolha = input("Escolha a categoria da manifestação: ")
        
        if validarNumero(escolha):
            escolha = int(escolha)
        else: 
            print("⚠️  Digite uma opção válida!")

        if escolha > 0 and escolha < 4:
            if escolha == 1:
                categoria = "reclamação"
            elif escolha == 2:
                categoria = "sugestão"
            elif escolha == 3:
                categoria = "elogio"

            return categoria
        else:
            print("\n⚠️  Digite uma opção válida!")
            return ""




def criarManifestacao(conn, categoria, assunto):
    
    sql = "insert into manifestacoes(categoria, assunto)values(%s,%s)"
    dados = [categoria, assunto]

    insertNoBancoDados(conn, sql, dados)



def listarManifestacoesCategoria(conn, categoria):
    sql = "select * from manifestacoes where categoria = %s"
    dados = [categoria]

    manifestacoes =  listarBancoDados(conn, sql, dados)

    if len(manifestacoes) == 0:
        print("\n❌ Não há manifestações cadastradas!")
    else:
        print("\nLista de manifestações:")
        for manifestacao in manifestacoes:
            print("\n💠 Categoria:", manifestacao[1], "\nCódigo:", manifestacao[0],"\nAssunto:",manifestacao[2])



def pesquisarCodigo (conn):
    while True:
        codigo = input("\nInforme o codigo para pesquisa: ")
        if not codigo.isdigit():
            print("\n❌ Digmanifestacao novamente em numeral")
            continue
        break
    codigo = int(codigo)
    perquisarcodigo = "select * from manifestacoes where id = (%s)"
    dados = [codigo]
    manifestacao = listarBancoDados(conn, perquisarcodigo, dados)

    if len(manifestacao) == 0:
        print("\n⚠️ Não contem item na lista")
    else:
        print("\n🔎 codigo:", manifestacao[0][0], "\nTipo:", manifestacao[0][1],"\nManifestação:", manifestacao[0][2] )




def remover(conn):
    codigoRemocao = int(input("\n🗑 Qual o codigo a ser removido? "))
    consultaRemocao = "delete from manifestacoes where id = %s"
    dadosRemocao = [codigoRemocao]

    excluirBancoDados(conn,consultaRemocao,dadosRemocao)
    print("\n✅ Removido com sucesso!")




def listarManifestacoes(conn):
    sql = "select * from manifestacoes"

    manifestacoes = listarBancoDados(conn, sql)

    return manifestacoes

#Exibir quantidade de informações
def exibirQuantidadeManifestacoes(conn):
    sql = "select count(*) from manifestacoes"

    quantidadeManifestacoes = listarBancoDados(conn, sql)

    return quantidadeManifestacoes


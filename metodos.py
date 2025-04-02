from operacoesbd import *

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

# escolhe a categoria da manifestação
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
            print("⚠️  Digite uma opção válida!")
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
        print("❌ Não há manifestações cadastradas!")
    else:
        print("Lista de manifestações:")
        for manifestacao in manifestacoes:
            print(f"manifestação {manifestacao[0]}) categoria: {manifestacao[1]} - {manifestacao[2]}")
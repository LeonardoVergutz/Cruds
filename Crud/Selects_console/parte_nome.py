import mysql.connector
from prettytable import PrettyTable

cnx = mysql.connector.connect(user='root', host='localhost', password="ceub123456", database='test')
cursor = cnx.cursor()

sql = "SELECT * FROM tb_imoveis WHERE endereco_imovel LIKE CONCAT('%', %s, '%') ORDER BY endereco_imovel;"



rodar = True
while rodar:
    nme = input("Qual é o CEP do estabelecimento a procurar [FIM - Termina]? ")

    if nme == "FIM":
        rodar = False
    else:
        cursor.execute(sql, (nme,))
        tab = PrettyTable(["Identificador", "Tipo", "Endereço", "Metragem", "Valor (R$)"])
        for (idt_imovel,tipo_imovel,endereco_imovel,metragem_imovel,preco_imovel) in cursor:
            tab.add_row([idt_imovel,tipo_imovel,endereco_imovel,metragem_imovel,preco_imovel])

        if cursor.rowcount == 0:
            print("Nenhum resultado encontrado.")
        else:
            print("\n")
            print(tab)
            print("\n")

cursor.close()
cnx.close()

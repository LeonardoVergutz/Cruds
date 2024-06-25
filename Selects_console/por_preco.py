import mysql.connector
from prettytable import PrettyTable

cnx = mysql.connector.connect(user='root', host='localhost', password="ceub123456", database='test')
cursor = cnx.cursor()

sql = "SELECT * FROM tb_imoveis WHERE preco_imovel BETWEEN %s AND %s ORDER BY preco_imovel DESC;"

rodar = True
while rodar:
    # Qual a faixa de preço?
    preco_inicial = float(input("Qual o preço inicial [0 - Termina]? "))
    if preco_inicial == 0:
        rodar = False
    else:
        preco_final = float(input("Qual o preço final? "))

        cursor.execute(sql, [preco_inicial, preco_final])
        tab = PrettyTable(["Identificador", "Tipo", "Endereço", "Metragem", "Valor (R$)"])

        print("Tabela de Imoveis")
        for (idt_imovel, tipo_imovel, endereco_imovel, metragem_imovel, preco_imovel) in cursor:
            tab.add_row([idt_imovel, tipo_imovel, endereco_imovel, metragem_imovel, preco_imovel])

    if cursor.rowcount == 0:
        print("Nenhum resultado encontrado.")
    else:
        print("\n")
        print(tab)
        print("\n")

cursor.close()
cnx.close()

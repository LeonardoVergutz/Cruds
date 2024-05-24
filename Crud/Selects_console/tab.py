import mysql.connector
from prettytable import PrettyTable

cnx = mysql.connector.connect(user='root', host='localhost', password="ceub123456", database='test')
csCil = cnx.cursor()
cursor = cnx.cursor()

sql = "SELECT distinct num_cilindrada_veiculo FROM tb_veiculo ORDER BY num_cilindrada_veiculo"

csCil.execute(sql)
menu = "Escolha a cilindrada:\n"
for [valor] in csCil:
   menu += str(valor) + "\n"
csCil.close()

sql = "SELECT * FROM tb_veiculo WHERE num_cilindrada_veiculo = %s"

rodar=True
while rodar:
  # Qual a cilindrada
  print(menu)
  cil=input("Qual a cilindrada [0 - Termina]? ")
  if cil=="0":
      rodar=False
  else:
      cursor.execute(sql, [cil])
      tab = PrettyTable(["Identificador", "Modelo", "Cilindrada", "Peso", "Valor (R$)"])

      for reg in cursor:
         tab.add_row(reg)

      print("\n")
      print(tab)
      print("\n")

cursor.close()
cnx.close()


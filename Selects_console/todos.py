import mysql.connector

cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              password="ceub123456",
                              database='test')
cursor = cnx.cursor()

sql = "SELECT * FROM tb_veiculo;"

cursor.execute(sql, [])

print("Tabela de Veículos")
print("identificador nome cilindrada peso valor")
for (idt, nome, cilindrada, peso, valor) in cursor:
   print(idt, nome, cilindrada, peso, valor)

cursor.close()
cnx.close()


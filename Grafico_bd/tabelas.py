from sql.banco import SQL
mysql = SQL()
comando = "DROP TABLE IF EXISTS tb_software;"

if mysql.upd_del(comando, ()) == 0:
  print ("Tabela de software excluída com sucesso!")

comando = "DROP TABLE IF EXISTS tb_tipo;"

if mysql.upd_del(comando, ()) == 0:
  print ("Tabela de tipo excluída com sucesso!")

comando = '''CREATE TABLE tb_tipo (
             idt_tipo INT AUTO_INCREMENT PRIMARY KEY,
             nme_tipo VARCHAR(50) NOT NULL);'''

if mysql.upd_del(comando, ()) == 0:
  print ("Tabela de tipo criado com sucesso!")

comando = '''CREATE TABLE tb_software (
        idt_software INT AUTO_INCREMENT PRIMARY KEY,
        nme_software VARCHAR(50) NOT NULL,
        ver_software VARCHAR(8) NOT NULL,
        cod_tipo INT NOT NULL,
        CONSTRAINT fk_tipo_software FOREIGN KEY (cod_tipo) REFERENCES tb_tipo(idt_tipo));'''

if mysql.upd_del(comando, ()) == 0:
  print ("Tabela de software criado com sucesso!")

comando = '''INSERT INTO tb_tipo(nme_tipo) VALUES
        ('Linguagem'), ('SGBD'), ('Sistema Operacional');'''


if mysql.upd_del(comando, ()) == 3:
  print ("Tipos cadastrados com sucesso!")


comando = '''INSERT INTO tb_software(nme_software, ver_software, cod_tipo) VALUES
        ('Pascal', '7.0', 1), ('Python', '3.7', 1), ('Java', '1.8', 1), ('Postgres', '9', 2),
        ('MySQL', '5.6', 2), ('Android', '10', 3), ('Linux', 'RedHat', 3), ('Windows', '10', 3);'''


if mysql.upd_del(comando, ()) == 8:
  print("Softwares cadastrados com sucesso!")

from sql.banco import SQL
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/barras')
def barras():
    # Recuperando Tipos de Software existentes na base de dados
    mysql = SQL()
    comando = "SELECT nme_tipo, COUNT(idt_software) AS qtd FROM tb_tipo JOIN tb_software ON idt_tipo=cod_tipo GROUP BY nme_tipo;"
    dados = mysql.get_list(comando, ())
    return render_template('barras.html', dados=dados)


@app.route('/org')
def org():
    # Recuperando Tipos de Software existentes na base de dados
    mysql = SQL()
    comando = "SELECT * FROM tb_tipo ORDER BY nme_tipo;"
    lista_tipos = mysql.get_list(comando, ())

    comandoSoft = "SELECT nme_software, ver_software FROM tb_software WHERE cod_tipo=%s ORDER BY nme_software;"
    for tipo in lista_tipos:
        tipo['softwares'] = mysql.get_list(comandoSoft, [tipo['idt_tipo']])

    return render_template('org.html', dados=lista_tipos)


if __name__ == '__main__':
    app.run(debug=1)

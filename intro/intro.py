from sql.banco import SQL
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accordion')
def accordion():
    banco = SQL("localhost", "root", "12345", "test")
    comando = "SELECT * FROM tb_veiculo ORDER BY vlr_veiculo DESC;"
    cs = banco.get_cursor(comando)
    dados = ""
    for (idt, nme, vlr) in cs:
        dados += '''
            <h3>{}</h3>
            <div>
                <table>
                    <tr>
                        <td style='padding: 30px'>
                            <p>Número: {}</p>
                            <p>Veículo: {}</p>
                            <p>Valor: {}</p>
                        </td>
                        <td style='padding: 30px'>
                            <img src="/static/{}.jpg" width="300px" height="200px">
                        </td>
                    </tr>
                </table>
            </div>
        '''.format(nme, idt, nme, vlr, idt)
    return render_template('accordion.html', dados=dados)

@app.route('/tabs')
def tabs():
    banco = SQL("localhost", "root", "12345", "test")
    comando = "SELECT * FROM tb_veiculo ORDER BY vlr_veiculo DESC;"
    cs = banco.get_cursor(comando)
    links = ""
    divs = ""
    for (idt, nme, vlr) in cs:
        links += "<li><a href='#id_{}'>{}</a></li>\n".format(idt, nme)
        divs += '''
            <div id="id_{}">
                <p>Número: {}</p>
                <p>Veículo: {}</p>
                <p>Valor: {}</p>
                <br>
                <p><img src="/static/{}.jpg" width="300px" height="200px"></p>
            </div>
        '''.format(idt, idt, nme, vlr, idt)
    return render_template('tabs.html', links=links, divs=divs)

@app.route('/dialogs')
def dialogs():
    banco = SQL("localhost", "root", "12345", "test")
    comando = "SELECT * FROM tb_veiculo ORDER BY vlr_veiculo DESC;"
    cs = banco.get_cursor(comando)
    rads = ""
    dlgs = ""
    for (idt, nme, vlr) in cs:
        rads += '''
            <label for="rad_{}">{}</label>
            <input type="radio" name="rad" id="rad_{}">
        '''.format(idt, nme, idt)
        dlgs += '''
            <div id="dlg_{}" class="dialogo" title="Dados de Veículo">
                <p>Número: {}</p>
                <p>Veículo: {}</p>
                <p>Valor: {}</p>
                <p><img src="/static/{}.jpg" width="300px" height="200px"></p>
            </div>
        '''.format(idt, idt, nme, vlr, idt)
    return render_template('dialogs.html', rads=rads, dlgs=dlgs)

if __name__ == '__main__':
    app.run(debug=True)

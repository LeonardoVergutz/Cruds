from funcoes import Action
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa'

act = Action()


@app.route('/', methods=['GET', 'POST'])
def index():
    # Teste se a forma de entrada na rota é por formulário, senão é por URL
    if request.method == 'POST':
        # Pegando os dados de usuário e senha digitados no formulário
        usr = request.form['usuario']
        pwd = request.form['senha']
        obj = act.login(usr, pwd)
        # Se retornou um usuário (Logou com sucesso)
        if obj is not None:
            session['usuario'] = obj
            return render_template('menu.html')
        else:
            return render_template('index.html', msg='Falha no Login ao Sistema')
    else:
        return render_template('index.html', msg="")


@app.route('/sair')
def sair():
    # Matar o usuário da sessão, não permitindo acesso a rotas protegidas
    session.pop('usuario', None)
    return render_template('index.html', msg="")


@app.route('/senha', methods=['GET', 'POST'])
def senha():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        senha_atual = request.form['senha_atual']
        senha = request.form['senha']
        confirma = request.form['confirma']
        msg = act.alterar_senha(session['usuario']['idt_usr'], senha_atual, senha, confirma)
        return render_template('senha.html', msg=msg)
    else:
        # A rota foi chamada por URL
        return render_template('senha.html', msg="")


@app.route('/resetar', methods=['GET', 'POST'])
def resetar():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if session['usuario']['pfl_usr'] != 'G':
        return render_template('index.html', msg="Está tentando burlar o sistema! Você não é gerente!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        usuario = request.form['usuario']
        senha = act.resetar_senha(usuario)
        return render_template('resetar.html', msg="Senha resetada para: " + senha)
    else:
        # A rota foi chamada por URL
        return render_template('resetar.html', msg="")


@app.route('/form_inc', methods=['GET', 'POST'])
def form_inc():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if session['usuario']['pfl_usr'] != 'A':
        return render_template('index.html', msg="Está tentando burlar o sistema! Você não é Administrador!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        nme_usr = request.form['nme_usr']
        eml_usr = request.form['eml_usr']
        pwd_usr = request.form['pwd_usr']
        pfl_usr = request.form['pfl_usr']

        retorno = act.incluir(nme_usr, eml_usr, pwd_usr, pfl_usr)

        return render_template('form_inc.html',
                               msg="Criado o usuário com id: {0}, senha: {1}".format(retorno[0], retorno[1]))
    else:
        # A rota foi chamada por URL
        return render_template('form_inc.html', msg="")


@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if session['usuario']['pfl_usr'] != 'A':
        return render_template('index.html', msg="Está tentando burlar o sistema! Você não é Administrador!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        nme_usr = request.form['nme_usr']
        pfl_usr = request.form['pfl_usr']

        lista = act.listar(nme_usr, pfl_usr)

        return render_template('modificar.html', msg="Retornado(s) {0} usuário(s).".format(len(lista)), lista=lista)
    else:
        # A rota foi chamada por URL
        return render_template('modificar.html', msg="", lista=[])


@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if session['usuario']['pfl_usr'] != 'A':
        return render_template('index.html', msg="Está tentando burlar o sistema! Você não é Administrador!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        idt_usr = request.form['idt_usr']
        nme_usr = request.form['nme_usr']
        eml_usr = request.form['eml_usr']
        pwd_usr = request.form['pwd_usr']
        pfl_usr = request.form['pfl_usr']

        retorno = act.alterar(idt_usr, nme_usr, eml_usr, pwd_usr, pfl_usr)
        usr = act.get_usuario(idt_usr)

        return render_template('alterar.html', msg=retorno, usr=usr)
    else:
        idt_usr = request.args.get("id")
        usr = act.get_usuario(idt_usr)
        return render_template('alterar.html', msg="", usr=usr)
@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
    # Proteção para que só entre se o usuário estiver logado
    try:
        usr = session['usuario']
    except:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if session['usuario']['pfl_usr'] != 'A':
        return render_template('index.html', msg="Está tentando burlar o sistema! Você não é Administrador!!!")

    # Verifica se a rota está sendo chamada pelo formulário "POST"
    if request.method == 'POST':
        # Recupera dados do formulário
        idt_usr = request.form['idt_usr']

        retorno = act.excluir(idt_usr)

        return render_template('modificar.html', msg=retorno)
    else:
        idt_usr = request.args.get("id")
        usr = act.get_usuario(idt_usr)
        return render_template('excluir.html', msg="", usr=usr)


if __name__ == '__main__':
    app.run(debug=True)

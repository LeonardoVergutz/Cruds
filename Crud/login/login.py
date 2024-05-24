from flask import Flask, render_template, request, session, redirect, url_for
from funcoes import Action

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa'

act = Action()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usr = request.form['usuario']
        pwd = request.form['senha']
        obj = act.login(usr, pwd)
        if obj is not None:
            session['usuario'] = obj
            return render_template('menu.html')
        else:
            return render_template('index.html', msg='Falha no Login ao Sistema')
    else:
        return render_template('index.html', msg="")

@app.route('/sair')
def sair():
    session.pop('usuario', None)
    return render_template('index.html', msg="")

@app.route('/senha', methods=['GET', 'POST'])
def senha():
    if 'usuario' not in session:
        return render_template('index.html', msg="Está tentando burlar o sistema! Não pode!!!")

    if request.method == 'POST':
        senha_atual = request.form['senha_atual']
        senha = request.form['senha']
        confirma = request.form['confirma']
        msg = act.alterar_senha(session['usuario']['idt_usr'], senha_atual, senha, confirma)
        return render_template('senha.html', msg=msg)
    else:
        return render_template('senha.html', msg="")

@app.route('/resetar', methods=['GET', 'POST'])
def resetar():
    if 'usuario' not in session or session['usuario']['pfl_usr'] != "G":
        return render_template('index.html', msg="Acesso negado!")

    if request.method == 'POST':
        nme_user = request.form['usuario']
        nova_senha = act.resetar_senha(nme_user)
        if nova_senha:
            msg = f"Senha resetada com sucesso. Nova senha: {nova_senha}"
        else:
            msg = "Erro ao resetar a senha. Usuário não encontrado."
        return render_template('reset.html', msg=msg)
    else:
        return render_template('reset.html', msg="")

if __name__ == '__main__':
    app.run(debug=True)
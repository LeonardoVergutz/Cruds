from sql.banco import SQL
import random
import string


class Action:
    def __init__(self):
        self.mysql = SQL()

    def login(self, usr, pwd):
        cmd = "SELECT * FROM tb_usr WHERE nme_usr = %s AND pwd_usr = SHA(%s);"
        obj = self.mysql.get_object(cmd, [usr, pwd])
        return obj

    def alterar_senha(self, idt_usr, senha_atual, senha, confirma):
        cmd = "SELECT COUNT(idt_usr) as qtd FROM tb_usr WHERE idt_usr=%s AND pwd_usr=SHA(%s);"
        num = self.mysql.get_int(cmd, [idt_usr, senha_atual])
        if num == 1:
            if senha == confirma:
                cmd = "UPDATE tb_usr SET pwd_usr=SHA(%s) WHERE idt_usr=%s;"
                ret = self.mysql.upd_del(cmd, [senha, idt_usr])
                if ret == 1:
                    return "Senha alterada com sucesso."
                else:
                    return "Erro ao tentar mudar a senha"
            else:
                return "Senha nova e confirmação não são iguais!"
        else:
            return "Senha atual está errada!"

    def gerar_senha_aleatoria(self):
        caracteres = string.ascii_letters + string.digits
        senha_aleatoria = ''.join(random.choice(caracteres) for i in range(8))
        return senha_aleatoria

    def resetar_senha(self, nme_user):
        nova_senha = self.gerar_senha_aleatoria()
        cmd = "UPDATE tb_usr SET pwd_usr=SHA(%s) WHERE nme_usr=%s;"
        ret = self.mysql.upd_del(cmd, [nova_senha, nme_user])
        if ret == 1:
            return nova_senha
        else:
            return None
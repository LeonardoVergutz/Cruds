from sql.banco import SQL
from prettytable import PrettyTable


class CRUD:
    def __init__(self):
        self.sql = SQL()

    def incluir(self):
        self.titulo('Inclusão de Disciplina')
        sigla = self.input_str('Sigla')
        nome = self.input_str('Nome')
        ch = int(input("Carga Horária"))
        cmd = 'INSERT INTO tb_dis(sgl_dis, nme_dis, num_ch_dis) VALUES (%s, %s, %s)'
        id = self.sql.insert(cmd, [sigla, nome,ch])
        print('Incluída Disciplina de ID:', id)

    def consultar(self):
        self.titulo('Consulta de Disciplina por Nome')
        nome = input('Digite parte do nome da Disciplina: ')
        cmd = 'SELECT * FROM tb_dis WHERE nme_dis LIKE CONCAT("%", %s, "%")'
        disc = self.sql.get_list(cmd, [nome])
        pt = PrettyTable(['Identificador', 'Sigla', 'Nome', 'Carga Horária'])
        for uf in disc:
            pt.add_row([str(uf['idt_dis']), uf['sgl_dis'], uf['nme_dis'], str(uf['num_ch_dis'])])
        print(pt)

    def alterar(self):
        self.titulo('Alteração de Disciplina por ID')
        id = int(input('Qual o ID da Disciplina para Alterar? '))
        cmd = 'SELECT * FROM tb_dis WHERE idt_dis = %s'
        dis = self.sql.get_object(cmd, [id])
        if dis is None:
            print('Disciplina não encontrada')
        else:
            sigla = self.input_str(f'Sigla atual: {dis["sgl_dis"]} - Nova')
            nome = self.input_str(f'Nome atual: {dis["nme_dis"]} - Novo')
            ch = int(input(f'Carga Horária atual: {dis["num_ch_dis"]} - Novo'))
            cmd = 'UPDATE tb_dis SET sgl_dis = %s, nme_dis = %s, num_ch_dis = %s WHERE idt_dis = %s'
            reg = self.sql.upd_del(cmd, [sigla, nome,ch, id])
            print('Foi alterado', reg, 'registro.')

    def excluir(self):
        self.titulo('Exclusão de Disciplina por ID')
        id = int(input('Qual o ID da disciplina para Excluir? '))
        cmd = 'SELECT * FROM tb_dis WHERE idt_dis = %s'
        uf = self.sql.get_object(cmd, [id])
        if uf is None:
            print('UF não encontrada')
        else:
            print('Sigla:', uf['sgl_dis'])
            print('Nome:', uf['nme_dis'])
            confirma = input('Confirma Exclusão [S/N]? ')
            if confirma == 'S':
                cmd = 'DELETE FROM tb_dis WHERE idt_dis = %s'
                reg = self.sql.upd_del(cmd, [id])
                print('Foi excluído', reg, 'registro.')
            else:
                print('Exclusão Cancelada')

    def titulo(self, texto):
        print('-' * 30)
        print(texto)
        print('-' * 30)

    def input_str(self, rotulo):
        ret = ''
        while ret == '':
            ret = input(rotulo + ': ')
        return ret

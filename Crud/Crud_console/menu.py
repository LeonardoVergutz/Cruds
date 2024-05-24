from prettytable import PrettyTable
from funcoes import CRUD


def menu():
    crud = CRUD()
    opcoes = [(1, 'Incluir'),
              (2, 'Consultar'),
              (3, 'Alterar'),
              (4, 'Excluir'),
              (5, 'Finalizar')]
    pt = PrettyTable(('Número', 'Função'))
    for opc in opcoes:
        pt.add_row(opc)
    permanecer = True
    while permanecer:
        print('\n' * 2)
        print(pt)
        escolha = int(input('Qual o número da função? '))
        print('\n' * 2)
        if escolha == 1:
            crud.incluir()
        elif escolha == 2:
            crud.consultar()
        elif escolha == 3:
            crud.alterar()
        elif escolha == 4:
            crud.excluir()
        elif escolha == 5:
            print('Fim do CRUD')
            permanecer = False
        else:
            print('Opção Inexistente')


if __name__ == '__main__':
    menu()

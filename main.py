from cadastrar_animais import cadastrar_animais
from cadastrar_pessoa import cadastrar_pessoa
from cruzamento import cruzamento
from pesquisar import pesquisar

if __name__ == '__main__':
    print(20 * '=' + ' Bem vindo ao sistema de adoção ' + 20 * '=')
    while True:
        print('\n[1] Cadastrar animais\n'
              '[2] Cadastrar pessoas\n'
              '[3] Pesquisar\n'
              '[4] Cruzamento\n'
              '[0] Sair')
        op = int(input('\nEscolha uma opção: '))

        if op == 0:
            break

        while op == 1:
            cadastrar_animais()
            print('[1] Continuar\n'
                  '[0] Voltar')
            op = int(input('\nEscolha uma opção: '))
        while op == 2:
            cadastrar_pessoa()
            print('[1] Continuar\n'
                  '[0] Voltar')
            op = int(input('\nEscolha uma opção: '))
            if op == 1:
                op = 2
        while op == 3:
            pesquisar()
            print('[1] Continuar\n'
                  '[0] Voltar')
            op = int(input('\nEscolha uma opção: '))
            if op == 1:
                op = 3
        while op == 4:
            cruzamento()
            print('[1] Continuar\n'
                  '[0] Voltar')
            op = int(input('\nEscolha uma opção: '))
            if op == 1:
                op = 4
        else:
            print('Opção inválida')







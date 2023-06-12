from erro_int import erro_int

def cadastrar_pessoa():
    print(20 * '=' + ' Cadastro de Pessoas ' + 20 * '=')

    # Dados para contato

    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    email = str(input('E-mail: '))
    numero = 0
    numero = erro_int(numero, 'Número + DDD: ')


    # Preferência do animal
    print('Preferência do animal')
    r_tipos = open(f'tipos.txt', 'r', encoding='UTF-8')
    c = 1
    for linha in r_tipos:
        dado = linha.split(';')
        print(f'[{dado[0]}] {dado[1]}', end='')
        c += 1
    print(f'[{c}] Outro tipo de animal')

    while True:
        tipo = int(input('Tipo do animal: '))
        if tipo < c:
            r_tipos = open(f'tipos.txt', 'r+', encoding='UTF-8')
            for linha in r_tipos:
                dado = linha.split(';')
                if dado[0] == str(tipo):
                    tipo = dado[1]
                    break
            break

        elif tipo == c:
            r_tipos = open(f'tipos.txt', 'a', encoding='UTF-8')
            tipo = str(input('Qual novo tipo deseja cadastrar: '))
            tipo = tipo + '\n'
            r_tipos.write(f'{c};{tipo}')
            break

        else:
            print('Tipo inválido, tente novamente')

    preferencia = str(input('Possui alguma outra preferência? [S/N]: ')).upper().strip()

    idade = 'N/a'
    cor = 'N/a'
    porte = 'N/a'

    if preferencia == 'S':
        preferencia = int(input(f'[1] Idade\n'
                                f'[2] Cor\n'
                                f'[3] Porte\n'))

        if preferencia == 1:
            idade = int(input('Idade preferencial: '))
        elif preferencia == 2:
            cor = str(input('Cor prefencial: ')).upper()
        elif preferencia == 3:
            porte = str(input('Porte preferencial: ')).upper()
        else:
            print('Escolha inválida!')
    elif preferencia == 'N':
        pass

    try:
        a = open('pessoas.txt', 'a', encoding='UTF-8')
        a.write(f'\nNome: {nome}\n'
                f'CPF: {cpf}\n'
                f'E-mail: {email}\n'
                f'Numero: {numero}\n'
                f'Tipo preferencial: {tipo}'
                f'Idade preferencial: {idade}\n'
                f'Cor preferencial: {cor}\n'
                f'Porte preferencial: {porte}\n')
    except FileNotFoundError:
        print('Houve um erro na criação do arquivo')

cadastrar_pessoa()
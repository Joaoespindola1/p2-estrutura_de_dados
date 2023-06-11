def cadastrar_animais():
    print(20*'=' + ' Cadastro de Animais ' + 20 * '=')
    r_tipos = open(f'tipos.txt', 'r', encoding='UTF-8')
    c = 1
    for linha in r_tipos:
        dado = linha.split(';')
        print(f'[{dado[0]}] {dado[1]}', end='')
        c += 1
    print(f'[{c}] Cadastrar outro tipo de animal')

    while True:
        tipo = int(input('Tipo do animal: '))
        if tipo < c:
            r_tipos = open(f'tipos.txt', 'r+', encoding='UTF-8')
            for linha in r_tipos:
                dado = linha.split(';')
                if dado[0] == str(tipo):
                    tipo = dado[1].upper()
                    break
            break

        elif tipo == c:
            r_tipos = open(f'tipos.txt', 'a', encoding='UTF-8')
            tipo = str(input('Qual novo tipo deseja cadastrar: ')).upper()
            tipo = tipo + '\n'
            r_tipos.write(f'{c};{tipo}')
            break

        else:
            print('Tipo inválido, tente novamente')

    idade = int(input('Idade aproximada do animal (em anos): '))
    cor = str(input('Cor do animal: ')).upper()
    porte = str(input('Porte do animal: ')).upper()
    particularidade = str(input('Possui alguma particularidade? [S/N]: ')).upper().strip()
    if particularidade == 'S':
        particularidade = str(input('Qual? ')).upper()
    elif particularidade == 'N':
        pass

    try:
        a = open('animais.txt', 'a', encoding='UTF-8')
        a.write(f'\nTipo: {tipo}'
                f'Idade aproximada: {idade}\n'
                f'Cor: {cor}\n'
                f'Porte: {porte}\n'
                f'Particularidade: {particularidade if (particularidade != "N") else "Nenhuma"}\n')
    except FileNotFoundError:
        print('Houve um erro na criação do arquivo')


def cadastrar_pessoa():
    print(20 * '=' + ' Cadastro de Pessoas ' + 20 * '=')

    # Dados para contato

    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    email = str(input('E-mail: '))
    numero = int(input('Número + DDD: '))

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


def inicializar():
    r_animais = open(f'animais.txt', 'r', encoding='UTF-8')
    global animais
    animais = [{}]
    c = 0
    for linha in r_animais:
        dado = linha.split(':')
        if dado[0] == "\n":
            animais.append({})
            c += 1
            pass
        else:
            animais[c][dado[0]] = dado[1].replace('\n', '').strip()

    r_pessoas = open(f'pessoas.txt', 'r', encoding='UTF-8')
    global pessoas
    pessoas = [{}]
    c = 0
    for linha in r_pessoas:
        dado = linha.split(':')
        if dado[0] == "\n":
            pessoas.append({})
            c += 1
            pass
        else:
            pessoas[c][dado[0]] = dado[1].replace('\n', '').strip()


def pesquisar():
    inicializar()
    r_tipos = open(f'tipos.txt', 'r', encoding='UTF-8')
    c = 1
    for linha in r_tipos:
        dado = linha.split(';')
        print(f'[{dado[0]}] {dado[1]}', end='')
        c += 1

    while True:
        tipo = int(input('Tipo do animal: '))
        if tipo < c:
            r_tipos = open(f'tipos.txt', 'r+', encoding='UTF-8')
            for linha in r_tipos:
                dado = linha.split(';')
                if dado[0] == str(tipo):
                    tipo = dado[1].replace('\n', '')
                    break
            break
        else:
            print('Tipo inválido, tente novamente')

    idade = int(input('Idade aproximada do animal (em anos): '))
    cor = str(input('Cor do animal: ')).upper()
    porte = str(input('Porte do animal: ')).upper()

    c = 0
    for i in animais:
        if idade+2 > int(i['Idade aproximada']) > idade-2:
            if tipo == i['Tipo'] and cor.upper() == i['Cor'].upper() and porte.upper() == i['Porte'].upper():
                print(f'===== Animal número {c} =====')
                print(i)
        c += 1

# no final do mês a prefeitura emitirá um relatório de cruzamento de espécies disponíveis x possíveis candidatos
def cruzamento():
    inicializar()
    c = 0
    for a in animais:
        print(f'\nAnimal id: {c}\n')
        for k, v in a.items():
            print(f'{k}: {v} | ', end='')
        print('\n')
        print(f'====== Possiveis candidatos para o id: {c} ======')
        for p in pessoas:
            if p['Idade preferencial'] == 'N/a':
                idade = int(a['Idade aproximada'])
            else:
                idade = int(p['Idade preferencial'])

            if p['Cor preferencial'] == 'N/a':
                cor = a['Cor']
            else:
                cor = p['Cor preferencial']

            if p['Porte preferencial'] == 'N/a':
                porte = a['Porte']
            else:
                porte = p['Porte preferencial']

            if idade + 2 >= int(a['Idade aproximada']) >= idade - 2:
                if p['Tipo preferencial'] == a['Tipo'] and cor == a['Cor'] and porte == a['Porte']:
                    print(p)

        c += 1



cruzamento()


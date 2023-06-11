# A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto,
# é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade
# aproximada, cor, porte e se possui alguma particularidade.

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

    idade = int(input('Idade aproximada do animal (em anos): '))
    cor = str(input('Cor do animal: '))
    porte = str(input('Porte do animal: '))
    particularidade = str(input('Possui alguma particularidade? [S/N]: ')).upper().strip()
    if particularidade == 'S':
        particularidade = str(input('Qual? '))
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


# um cadastro de pessoas interessadas na adoção, contendo os dados principais de contato e qual espécie teria o
# interesse de adotar. Ao escolher a espécie, deve também informar se possui alguma preferência do animal.

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
            cor = str(input('Cor prefencial: '))
        elif preferencia == 3:
            porte = str(input('Porte preferencial: '))
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
                f'Tipo preferêncial: {tipo}'
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
    #for i in pessoas, animais:
     #   for j in i:
     #       print(j)


#que o atendente possa pesquisar se há algum animal com as características informadas.
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
        if int(i['Idade aproximada']) < idade+2 and int(i['Idade aproximada']) > idade-2:
            if tipo == i['Tipo'] and cor.upper() == i['Cor'].upper() and porte.upper() == i['Porte'].upper():
                print(f'===== Animal número {c} =====')
                print(i)
pesquisar()

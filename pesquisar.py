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


def cadastrar_animais():
    print()
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


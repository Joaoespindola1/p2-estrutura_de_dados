#A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto,
# é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade.

def cadastrar_animais():
    r_tipos = open(f'tipos.txt', 'r', encoding='UTF-8')
    c = 1
    for linha in r_tipos:
        dado = linha.split(';')
        print(f'[{dado[0]}] {dado[1]}',end='')
        c += 1
    print(f'[{c}] Cadastrar outro tipo de animal')

    while True:
        tipo = int(input('Tipo do animal: '))
        if tipo <= c:
            r_tipos = open(f'tipos.txt', 'r+', encoding='UTF-8')
            for linha in r_tipos:
                dado = linha.split(';')
                if dado[0] == str(tipo):
                    tipo = dado[1]
                    break
        elif tipo == c:
            r_tipos = open(f'tipos.txt', 'a', encoding='UTF-8')
            tipo = str(input('Tipo do animal: '))
            r_tipos.write(f'{c};{tipo}')
            break
        else:
            print('Tipo inválido, tente novamente')


    idade = int(input('Idade aproximada do animal: '))
    cor = str(input('Cor do animal: '))
    porte = str(input('porte do animal: '))
    particularidade = str(input('Possui alguma particularidade? [S/N]: ')).upper().strip()
    if particularidade == 'S':
        particularidade = str(input('Qual? '))
    elif particularidade == 'N':
        pass

    try:
        a = open('animais.txt', 'wt+', encoding='UTF-8')
    except:
        print('Houve um erro na criação do arquivo')

    a.write(f'Tipo: {tipo}\n'
            f'Idade aproximada: {idade}\n'
            f'Cor: {cor}\n'
            f'Porte: {porte}\n'
            f'Particularidade: {particularidade if (particularidade != "N") else "Nenhuma"}\n')


cadastrar_animais()


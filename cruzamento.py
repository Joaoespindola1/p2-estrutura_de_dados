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

def cruzamento():
    inicializar()
    c = 0
    for a in animais:

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
                    print(f'\nAnimal id: {c}\n')
                    for k, v in a.items():
                        print(f'{k}: {v} | ', end='')
                    print('\n')
                    print(f'------- Possiveis candidatos para o id: {c} -------\n')
                    print(p)
                    print()
                    print('=' * 50)
        c += 1



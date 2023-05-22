#A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto,
# é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade.

def cadastrar_animais():
    tipo = str(input('Tipo do animal: '))
    idade = int(input('Idade aproximada do animal: '))
    cor = str('Cor do animal: ')
    porte = str('porte do animal: ')
    particularidade = str(input('Possui alguma particularidade? [S/N]: ')).upper().strip()
    if particularidade == 'S':
        particularidade = str(input('Qual?'))
    elif particularidade == 'N':
        pass


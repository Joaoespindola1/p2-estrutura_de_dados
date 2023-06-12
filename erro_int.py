def erro_int(v,m):
    try:
        v = int(input(m))
    except:
        print('Inválido')
        erro_int(v,m)
    return v
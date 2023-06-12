def erro_int(v,m):
    while True:
        v = (input(m))
        if v.isdigit():
            return v
            break
        print("Inválido")


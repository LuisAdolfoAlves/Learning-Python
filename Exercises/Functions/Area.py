def main():
    cabecalho()
    calc_area()


def cabecalho():
    print("Controle de Terrenos")
    print("----------------------")


def calc_area():
    l = float(input("LARGURA (m): "))
    c = float(input("COMPRIMENTO (m): "))
    total_area = l * c
    print(f"A área total de um terreno {l} x {c} é de {total_area} m^2")
    terreno(l, c)


def terreno(a, b):
    a = int(a)
    b = int(b - 1)
    for linha in range(a):
        for coluna in range(b):
            print("#", end="")
        print("#")


if __name__ == '__main__':
    main()

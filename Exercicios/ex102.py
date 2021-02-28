def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')


def linha():
    print('-'*40)


def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número inteiro
    :param num: O número a a ser calculado.
    :param show: (Opcional) mostra ou não o processo de fatorial.
    :param return: O resultado do farorial de num
    """
    f = 1
    r = list()
    for c in range(num, 0, -1):
        f *= c
        r.append(c)
        if c > 1:
            r.append('x')
        else:
            r.append('=')
    if show == True:
        for c, v in enumerate(r):
            print(f'{v} ', end='')
    return f


titulo('Calculando Fatorial')
n = int(input('Digite um valor: '))
fat = fatorial(n, True)
print(f'{fat}')
linha()
linha()
print(help(fatorial))
linha()

def linha(txt):
    print(f'\033[034m{txt}\n{"-"*40}')


def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a} métros quadrados:')


linha(' Controle de Terrenos')
print("\033[030m")
larg = float(input('LARGURA: '))
comp = float(input('COMPRIMENTO: '))
area(larg, comp)

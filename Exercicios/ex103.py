def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')


def linha():
    print('-'*40)


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato')


titulo('Ficha do Jogador')
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

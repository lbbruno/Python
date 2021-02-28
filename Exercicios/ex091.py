from random import randint
from time import sleep
from operator import itemgetter
ranking = dict
jogadores = dict()
pos = 0
jogadores['jogador1'] = randint(1, 12)
jogadores['jogador2'] = randint(1, 12)
jogadores['jogador3'] = randint(1, 12)
jogadores['jogador4'] = randint(1, 12)
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v}')
print('='*40)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    pos += 1
    print(f'{pos}º lugar {k} com {v}')
print('='*40)

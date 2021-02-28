from time import sleep
from random import randint


def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')


def linha():
    print('-'*40)


lista = list()
titulo('Somando os pares')


def sorteio():
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]} ', end='')
    print('PRONTO!')
    return lista


def somapar():
    lista = sorteio()
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares: {s}')


somapar()

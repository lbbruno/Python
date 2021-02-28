from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos quer fazer?'))
for j in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for i, j in enumerate(jogos):
    print(f'Jogo: {i+1}º: {j}')
    sleep(1)
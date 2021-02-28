n = int(input('Quantos valores você quer digitar:'))
lista = list()
for i in range(0, n):
    vlr = int(input('Informe o valor:'))
    lista.append(vlr)
    if i == 0:
        maior = vlr
        menor = vlr
    else:
        if vlr >= maior:
            maior = vlr
        elif vlr <= menor:
            menor = vlr
print(f'O menor valor digitado é: {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado é: {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
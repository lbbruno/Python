lista = list()
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    choice = str(input('Deseja Continuar? [S/N]')).lower()
    while choice not in 'sn':
        choice = str(input('Deseja Continuar? [S/N]')).lower()
    if choice in 'n':
        break
lista.sort(reverse=True)
print('-=-'*15)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os elementos na ordem decrescente são: {lista}')
print(f'O número 5 foi encontrado na lista.' if 5 in lista else 'O número 5 não foi encontrado na lista.')
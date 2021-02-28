dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if maior == menor == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    dados.clear()
    r = str(input('Deseja continuar? [S/N]')).lower()
    if r in 'n':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso é {maior:.2f}Kg. Peso de ', end='')
for n, p in pessoas:
    if p == maior:
        print(f'[{n}]', end='')
print(f'\nO menor peso é {menor:.2f}Kg. ', end='')
for n, p in pessoas:
    if p == menor:
        print(f'[{n}]', end='')
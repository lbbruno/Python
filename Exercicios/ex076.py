lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)
print(lista)
div = '-'*40
title = 'Lista de Preços'
print(f'{div}\n{title: ^40}\n{div}')
for i in range(0, len(lista)):
     #print(f'{i} - {lista[i]} === {lista[i]}')
    if i % 2 == 0:
        print(f'{lista[i]:.<31}', end='')
    else:
        print(f'R$ {lista[i]: >6.2f}')
print(div)

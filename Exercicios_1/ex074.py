from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados são: ', end='')
for i in numeros:
    print(f'{i} ', end='')
print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')

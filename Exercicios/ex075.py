par = 0
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(num)
print(f'O número 9 parareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares digitados são: \n ')
for i in num:
    if i % 2 == 0:
        print(f'{i} ', end='')


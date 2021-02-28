num = int(input('Digite um número: '))
div = 0
for i in range(1, num+1):
    if num % i != 0:
        print('\033[031m', end='')
    else:
        print('\033[033m', end='')
        div += 1
    print('{} '.format(i), end='')
print('\033[m')
if div > 2:
    print('\nO número {} foi divisível {} vezes'.format(num, div))
    print('Por isso não é número primo.')
else:
    print('\nO número {} foi divisível {} vezes'.format(num, div))
    print('Por isso é número primo.')

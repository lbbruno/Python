from math import factorial
n = int(input('digite um número: '))
c = n
fat = factorial(n)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '', end='')
    c -= 1
print('\nO fatorial de {} = {}'.format(n, fat))


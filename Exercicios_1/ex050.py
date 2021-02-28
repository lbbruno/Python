s = 0
for i in range(0, 6):
    num = int(input('Digite um valor inteiro:'))
    if num % 2 == 0:
        s += num
print('A soma dos números pares é {}'.format(s))

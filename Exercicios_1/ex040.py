frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Calculo de nota final '))
print(frame)

a1 = float(input('Nota A1: '))
a2 = float(input('Nota A2: '))
a3 = float(input('Nota A3: '))
a4 = float(input('Nota A4: '))
a5 = float(input('Nota A5: '))
n1 = (((a1 + a2 + a3 + a4) / 4) * 0.4)
n2 = (a5 * 0.6)
res = n1 + n2

if res >= 6:
    print('Nota Fianl: \033[033m {} - Aprovado.'.format(res))
else:
    print('Nota Final: \033[031m {} - Reprovado.'.format(res))
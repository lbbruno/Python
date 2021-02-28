d = float(input('Quantidade de dias: '))
km = float(input('Quantos Km rodados:'))
t = (60 * d) + (0.15 * km)
print('O valor total a ser pago é: R${:.2f}'.format(t))
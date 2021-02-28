salario = float(input('Informe o salário: '))
print('Aumento de 10%: {:.2f}'.format(salario * 1.10) if salario > 1250 else 'Aumento de 15% {:.2f}: '.format(salario * 1.15))

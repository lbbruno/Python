frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Testando Números '))
print(frame)
num1 = int(input('Informe o primeiro número:'))
num2 = int(input('Informe o segundo número:'))

if num1 == num2:
    print('\033[035mO número {} = {}. Não existe número maior, os dois são iguais.'.format(num1, num2))
elif num1 > num2:
    print('\033[032mO número {} > {}. O prinmeiro número é maior'.format(num1, num2))
else:
    print('\033[033mO número {} < {}. O segundo número é maior'.format(num1, num2))

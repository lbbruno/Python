frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Conversor de números '))
print(frame)
print('1. Binário\n2. Octal\n3. Hexadecimal')
op = int(input('Escolha uma opção:'))
num = int(input('informe o número a ser convertido:'))

if op == 1:
    print(bin(num)[2:])
elif op == 2:
    print(oct(num)[2:])
elif op == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida, reinicie o programa')
frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Teste Triangulo '))
print(frame)

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))
print('#'*60)
triang = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2

if triang:
    if r1 == r2 == r3:
        print('Triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Não é triângulo.')






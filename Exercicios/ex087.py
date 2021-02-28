div = '* - *'*6
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna3 = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]

print(div)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^6}|', end='')
    print()
print(div)
print(f'A soma dos números pares é {pares}')
print(f'A soma dos números da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')

valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp in 'n':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)
print(f'A lista completa é: {valores}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números impares é: {impares}')
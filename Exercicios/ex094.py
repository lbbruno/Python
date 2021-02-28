div = '='*33
    # Inicialização de Variáveis
cadastro = list()
ficha = dict()
médiaidade = 0
    # Principal
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    ficha['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
    if ficha['sexo'] not in 'MF':
        while ficha['sexo'] not in 'MF':
            print('ERRO! Por favor digite somente "M" ou "F"')
            ficha['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    ficha['idade'] = int(input('Idade: '))
    médiaidade += ficha['idade']
    cadastro.append(ficha.copy())
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r not in 'SN':
        print('ERRO! Digite apenas "S" ou "N"')
        r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r == 'N':
        break
print(div)
print(f'{"Nome":<15} {"Sexo":^8} {"Idade":^8}')
for i, f in enumerate(cadastro):
    print(f'{f["nome"]:<15} {f["sexo"]:^8} {f["idade"]:^8}')
print(div)
print(f'A) Ao todo temos {len(cadastro)} cadastradas.')
print(f'B) A média de idade é {médiaidade/len(cadastro):.2f}')
print(f'C) As mulheres cadastradas foram ')
for i, f in enumerate(cadastro):
    if f["sexo"] == 'F':
        print(f'{f["nome"]}', end='')
print(f'\nD) Lista de pessoas que estão acima da média:')
for i, f in enumerate(cadastro):
    if f["idade"] > médiaidade/len(cadastro):
        print(f'Nome: {f["nome"]} Sexo: {f["sexo"]} Idade: {f["idade"]}')

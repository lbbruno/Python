maior18 = 0
mulheres20 = 0
homens = 0
div = '-'*30
while True:
    print(div)
    print('     CADASTRE UMA PESSOA ')
    print(div)
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print(div)
    if idade >= 18:
        maior18 += 1
    if idade < 20 and sexo in 'Ff':
        mulheres20 +=1
    if sexo in 'Mm':
        homens += 1
    resp = ' '
    while resp not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {homens} homem(s) cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
print('FIM')

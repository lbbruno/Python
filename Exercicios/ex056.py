from datetime import date
mediaIdade = 0
homemMaior = 0
homemMaiorNome = ''
qntFeminino = 0
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    mediaIdade += idade
    if sexo == 'M':
        if i == 1:
            homemMaior = idade
            homemMaiorNome = nome
        else:
            if idade > homemMaior:
                homemMaior = idade
                homemMaiorNome = nome
    if sexo == 'F' and idade < 20:
        qntFeminino += 1
print('A média de idade do grupo é de {}.'.format(idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemMaior, homemMaiorNome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qntFeminino))

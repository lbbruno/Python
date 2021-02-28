sexo = str(input('Informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor, informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
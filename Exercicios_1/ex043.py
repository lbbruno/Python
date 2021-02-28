frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Cálculo IMC '))
print(frame)

peso = float(input('Informe o peso: '))  # Recebe o peso pelo usuário
altura = float(input('Informe a altura: '))  # Recebe Alatura pelo usuário
imc = (peso / (altura * altura))  # Calculo do IMC
situacao = ''
pesoMax = (24.99 * (altura ** 2))  # Peso máximo ideal
pesoMin = (18.5 * (altura ** 2))  # Peso mínimo ideal

#### Verificação dentro da tabela de IMC
if imc >= 40:
    situacao = 'Obesidade Morbida'
elif 30 <= imc < 40:
    situacao = 'Obesidade'
elif 25 <= imc < 30:
    situacao = 'Sobrepeso'
elif 18.5 <= imc < 25:
    situacao = 'Peso Ideal'
else:
    situacao = 'Abaixo do Peso'

print('{: ^20}|{: ^20}|{: ^20}|{: ^20}'.format('Peso', 'Altura', 'IMC', 'Situação'))
print('{: ^19.2f} | {: ^18.2f} | {: ^18.2f} | {: ^20}'.format(peso, altura, imc, situacao,))
print('\nSeu peso ideal está entre {:.2f}Kg e {:.2f}Kg'.format(pesoMin, pesoMax))


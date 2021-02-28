v = float(input('Digite a velocidade do veículo: '))
x = (v-80)*7
if v > 80:
    print('\033[0;31mVocê ultrapassou o limite de 80km/h e receberá uma multa de R${:.2f}'.format(x))
print('\033[0;32mVocê não recebeu multa pois está dentro do limite de velocidade.')

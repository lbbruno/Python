distancia = float(input('Digite a distância da viagem em Km: '))
if distancia > 200:
    print('Para a viagem de {}Km o valor da passagem é {}'.format(distancia,distancia*0.45))
else:
    print('Para a viagem de {}Km o valor da passagem é {}'.format(distancia, distancia * 0.5))
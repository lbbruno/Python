pmaior = 0
pmenor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}° pessoa: '.format(c)))
    if c == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O peso maior é {}Kg e o menor é {}Kg.'.format(pmaior, pmenor))

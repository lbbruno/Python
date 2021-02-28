lista = list()
while True:
    vlr = int(input('Digite um valor: '))
    if vlr in lista:
        print('Este valor já existe na lista..,')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(vlr)
    op = str(input('Deseja continuar? [S/N]')).strip().upper()
    if op in 'Nn':
        break
print(f'Os valores digitados são: {sorted(lista)}')
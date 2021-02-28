div1 = '='*40
div2 = '-'*40
    # Inicialização de Variáveis
time = list()
gols = list()
ficha = dict()
cod = 0
while True:
    ficha.clear()
    gols.clear()
    ficha['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantos partidas {ficha["nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}?')))
    ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Favor, digite apenas S ou N.')
    if r == 'N':
        break
print(div1)
print(f'{"cod.":<5}{"Nome":<15}{"Gols":<15}{"Total ":<15}')
print(div2)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(div2)
while True:
    r = int(input('Mostrar dados de qual jogador? (000 para parar)'))
    if r == 000:
        break
    if r <= len(time):
        print(f'-- LEVANTAMENTO DO JOGADOR {time[r]["nome"]}:')
        for i, v in enumerate(time[r]['gols']):
            print(f'\tNa partida {i+1} fez {v} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {r}')

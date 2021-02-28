div1 = '='*40
div2 = '-'*40
    # Inicialização de Variáveis
jogador = dict()
partidas = list()
saldo = 0
    # Principal
jogador['nome'] = str(input('Nome do Jogador: '))
numpart = int(input(f'Quantas pardidas {jogador["nome"]} jogou? '))
for p in range(1, numpart+1):
    gols = int(input(f'\tQuantos gols na partida {p}? '))
    partidas.append(gols)
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(div1)
print(jogador)
print(div2)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(div2)
print(f'O jogador {jogador["nome"]} jogou {numpart} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'\t=> Na partida {i+1} fez {v} gols.')

alunos = []
dados = []
notas = []
resp = 's'
while resp not in 'n':
    dados.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1:')))
    notas.append(float(input('Nota 2:')))
    dados.append((notas[0] + notas[1]) / 2)
    dados.append(notas[:])
    alunos.append(dados[:])
    dados.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N]')).lower()
print(f'{"Nº.":<3}{"Nome":<15}{"Média":>5}')
print('-'*25)
for i, aluno in enumerate(alunos):
    print(f'{i:<3}{aluno[0]:<15}{aluno[1]:>5.1f}')
print('-'*50)
while True:
    opc = int(input('Quer ver as notas de qual aluno? Interromper...999'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(alunos)-1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][2]}')
        print('-'*50)

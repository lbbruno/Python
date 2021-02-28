aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} -> {v}')

termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite razão da PA: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo+1, razao):
    print('{}'. format(i), end='-')
print('FIM')

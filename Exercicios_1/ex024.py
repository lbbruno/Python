cidade = str(input('Cidade: '))
cidade = cidade.lower()
cidade = cidade.split()
print('santo' in cidade[0])


cidade = str(input('Cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
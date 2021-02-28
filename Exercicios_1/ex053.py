frase = str(input('Frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Esta frase é um palíndromo')
else:
    print('Essa frase não é um palindromo.')
print('{} - {} letras'.format(inverso, len(junto)))

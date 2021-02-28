n = cont = soma = maior = menor = media = 0
repetir = 'S'
while repetir == 'S':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma = soma + n
        media = float(soma / cont)
    cont += 1
    repetir = str(input('Quer continuar? [S/N]:')).upper().strip()

print('Você digitou {} e a soma entre eles é {} e a média é {:.2f}'.format(cont, soma, media))
print(' O maior número entre eles é {} e o menor é {}'.format(maior, menor))
print('FIM')
from random import randint
print('Tente adivinhar o número!')

pc = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10... Tente adivihar!')
acertou = False
tentativa = 0
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativa += 1
    if palpite == pc:
        acertou = True
    else:
        if palpite < pc:
            print('Mais... Tente novamente!')
        elif palpite > pc:
            print('Menos... Tente mais uma vez!')

print('Você acertou! O número é {} com {} tentativas.'.format(pc, tentativa))

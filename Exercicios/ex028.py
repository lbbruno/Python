import random
x = int(random.randint(1,10))
num = int(input('Adivinhe o número que pensei entre 1 e 10: '))
print('Você acertou o número é {}' if x == num else 'Você errou o número é {}'.format(x))

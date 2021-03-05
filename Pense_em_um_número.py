import random
from time import sleep

def computador_adivinha(x):
    menor_num = 1
    maior_num = x
    feedback = ''
    while feedback != 'C':
        sleep(1)
        escolha_pc = random.randint(menor_num, maior_num)
        feedback = str(input(f'Acho que é {escolha_pc}! O número é maior[H], menor[L] ou está correto[C]??')).upper()
        if feedback in 'H':
            menor_num = escolha_pc + 1
        elif feedback in 'L':
            maior_num = escolha_pc - 1
    print('Acertei!!! Vamos jogar novamente?')

computador_adivinha(10)
import random
import time

print('''\033[033mEste algoritmo pretende comparar o tempo de execução
do Navie Search com o Binary Search\033[m''')

def navie_serach(l, targert):
    for i in range(len(l)):
        if l[i] == targert:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(navie_serach(l, target))
    # print(binary_search(l, target))

    length = 100000

    print('-> Iniciando variável de lista ordenada para o teste.')

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    print(f'-> {len(sorted_list)} números aleatórios foram adicionados a lista de maneira ordenada.\n')

    print('-' * 50)
    print('O Navie Search será iniciado em 5 segundos...')
    time.sleep(5)
    print('Iniciado, aguarde um momento...')

    start = time.time()
    for target in sorted_list:
        navie_serach(sorted_list, target)
    end = time.time()

    print(f'\033[034mNavie Search tempo: {(end - start)} segundos.\033[m\n')

    print('-' * 50)

    print('Binary Search será iniciado em 5 segundos...')
    time.sleep(5)
    print('Iniciado, aguarde um momento...')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()

    print(f'\033[034mBinary Search tempo: {(end - start)} segundos.\033[m')

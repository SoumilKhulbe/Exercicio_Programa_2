import random

def rolar_dados(num_dados):
    lista = []
    for x in range(num_dados):
        dado = random.randint(1, 6)
        lista.append(dado)

    return lista


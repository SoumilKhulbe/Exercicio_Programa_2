import random

def rolar_dados(num_dados):
    lista = []
    for x in range(num_dados):
        dado = random.randint(1, 6)
        lista.append(dado)

    return lista




def guardar_dado(dados_rolados,dados_guardados,numero):
    lista = []
    if numero in dados_rolados:
        dados_guardados.append(numero)
        dados_rolados.remove(numero)
    lista.append(dados_rolados)
    lista.append(dados_guardados)

    return lista

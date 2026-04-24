import random

def rolar_dados(num_dados):
    lista = []
    for x in range(num_dados):
        dado = random.randint(1, 6)
        lista.append(dado)

    return lista




def guardar_dado(dados_rolados,dados_guardados,numero):
    lista = []
    
    dados_guardados.append(dados_rolados[numero])
    del dados_rolados[numero]
    lista.append(dados_rolados)
    lista.append(dados_guardados)

    return lista



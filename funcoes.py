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





def remover_dado(dados_rolados, dados_no_estoque, indice):
    lista = []
    dados_rolados.append(dados_no_estoque[indice])
    del dados_no_estoque[indice]
    lista.append(dados_rolados)
    lista.append(dados_no_estoque)

    return lista







def calcula_pontos_regra_simples(numeros):
    dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    
    for x in numeros:
        dic[x] += numeros[x]

    return dic
        
    




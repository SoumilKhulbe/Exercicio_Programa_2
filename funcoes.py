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
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for x in numeros:
        dic[x] += x

    return dic
        
    



def calcula_pontos_soma(numeros):
    contagem = 0
    for x in numeros:
        contagem += x

    return contagem




def calcula_pontos_sequencia_baixa(numeros):
    for n in numeros:
        if (n+1 in numeros and n+2 in numeros and n+3 in numeros):
            return 15
        
    return 0



def calcula_pontos_sequencia_alta(numeros):
    for n in numeros:
        if (n+1 in numeros and n+2 in numeros and n+3 in numeros and n+4 in numeros):
            return 30
        
    return 0




def calcula_pontos_full_house(lista):
    dic = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for x in lista:
        dic[x] += 1
    tres = False
    dois = False

    for y in dic:
        if dic[y] == 3:
            tres = True
        elif dic[y] == 2:
            dois = True
    if tres and dois:
        total = 0
        for x in lista:
            total += x
        return total
    return 0



def calcula_pontos_quadra(lista):
    dic = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for x in lista:
        dic[x] += 1

    quatro = False
    
    for y in dic:
        if dic[y] >= 4:
            quatro = True

    if quatro:
        total = 0
        for z in lista:
            total += z

        return total 
       
    return 0




def calcula_pontos_quina(lista):
    dic = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for x in lista:
        dic[x] += 1

    cinco = False
    
    for y in dic:
        if dic[y] >= 5:
            cinco = True

    if cinco:
        return 50
       
    return 0




def calcula_pontos_regra_avancada(lista):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(lista)
    dic['full_house'] = calcula_pontos_full_house(lista)
    dic['quadra'] = calcula_pontos_quadra(lista)
    dic['sem_combinacao'] = calcula_pontos_soma(lista)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)

    return dic




def faz_jogada(dados, categoria, cartela_de_pontos):
    simples = [1, 2, 3, 4, 5, 6]
    avancada = ["cinco_iguais", "full_house", "quadra", "sem_combinacao", "sequencia_alta", "sequencia_baixa"]
    
    if (categoria) in avancada:
        b = calcula_pontos_regra_avancada(dados)
        pontos = b[categoria] 
        cartela_de_pontos["regra_avancada"][categoria] = pontos
        return cartela_de_pontos
    
    if int(categoria) in simples:
        a = calcula_pontos_regra_simples(dados)
        pontos = a[int(categoria)]
        cartela_de_pontos["regra_simples"][int(categoria)] = pontos
        return cartela_de_pontos
    


def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)


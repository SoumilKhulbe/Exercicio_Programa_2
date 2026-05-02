from funcoes import *

simples = [1, 2, 3, 4, 5, 6]
avancada = ["cinco_iguais", "full_house", "quadra", "sem_combinacao", "sequencia_alta", "sequencia_baixa"]

cartela = {
    "regra_simples": {1 : -1, 2 : -1, 3 : -1, 4 : -1, 5 : -1, 6 : -1}, "regra_avancada": {"cinco_iguais": -1, "full_house": -1, "quadra": -1, "sem_combinacao": -1, "sequencia_alta": -1, "sequencia_baixa": -1}}

imprime_cartela(cartela)


for rodada in range(12):
    rolados = rolar_dados(5)
    guardados = []
    rerrolar = 0

    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")

    a = input(">")

    while a != "0":

        if a == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            guardado = guardar_dado(rolados, guardados, indice)

            rolados, guardados = guardado

            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")

            a = input(">")


        
        elif a == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            
            indice = int(input(">"))
            removido = remover_dado(rolados, guardados, indice)

            rolados, guardados = removido

            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
        
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")


            a = input(">")

        elif a == "3":
            if rerrolar == 2:
                print("Você já usou todas as rerrolagens.")
                print(f"Dados rolados: {rolados}")
                print(f"Dados guardados: {guardados}")

                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")


                a = input(">")
            else: 
                rolados = rolar_dados(len(rolados))
                rerrolar += 1
                print(f"Dados rolados: {rolados}")
                print(f"Dados guardados: {guardados}")

                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")


                a = input(">")

        elif a == "4":
            imprime_cartela(cartela)
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")


            a = input(">")


    while True:
        print("Digite a combinação desejada:")
        opcao = input(">")

        if opcao in avancada:
            if cartela["regra_avancada"][opcao] != -1:
                print("Essa combinação já foi utilizada.")
                continue
            else:
                c = opcao
                dados = rolados + guardados
                cartela = faz_jogada(dados, c, cartela)
                break
        elif int(opcao) in simples:
            if cartela["regra_simples"][int(opcao)] != -1:
                print("Essa combinação já foi utilizada.")
                continue
            else:
                c = opcao
                dados = rolados + guardados
                cartela = faz_jogada(dados, c, cartela)
                break
        else:
            print("Combinação inválida. Tente novamente.")
            continue

somas = 0
somaa = 0
soma_total = 0

for x in cartela["regra_simples"].values():
    somas += x

for y in cartela["regra_avancada"].values():
    somaa += y

soma_total = somas + somaa

if somas >= 63:
    soma_total += 35


imprime_cartela(cartela)

print(f"Pontuação total: {soma_total}")

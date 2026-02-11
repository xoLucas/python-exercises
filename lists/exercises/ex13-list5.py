def le_gab ():
    G = input("Escreva o gabarito da loteria: ").split(",")
    G = [int(x) for x in G] #torna o gabarito em int

    return(G)

def le_apostador ():

    apostador = input("Digite o nome do apostador: ")
    cartao = input("Digite as respostas do cartao do apostador: ").split(",")
    cartao = [int(x) for x in cartao]

    return(apostador, cartao)

def confere_cartao(G, cartao):

    acertos = 0
    for i in range(len(G)):
        if G[i] == cartao[i]:
            acertos += 1
    return(acertos)

def main ():
    apostadores_result = []
    G = le_gab()
    entre_10a13 = 0
    menor_10 = 0
    for k in range(10):
        apostador, cartao = le_apostador()
        acertos = confere_cartao(G, cartao)
        if acertos >= 10 and acertos <= 13:
            entre_10a13 += 1
        elif acertos < 10:
            menor_10 += 1
        apostadores_result += [f"{apostador}:{acertos}"]
    print(apostadores_result)
    print(f"{(entre_10a13/10)*100}% dos apostadores ficaram entre 10 e 13 acertos e {(menor_10/10)*100}% dos apostadores ficaram com menos de 10 acertos.")

main()
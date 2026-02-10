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
    for k in range(10):
        apostador, cartao = le_apostador()
        acertos = confere_cartao(G, cartao)
        apostadores_result += [f"{apostador}:{acertos}"]
    print(apostadores_result)

main()
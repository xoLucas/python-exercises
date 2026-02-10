import random

def cria_lista ():
    #L = random.sample(range(1,21), 10) #Gera a lista sem repetição
    L = list()
    while len(L) < 10:
        n = random.randint(0,15)
        L.append(n) #Gera a lista podendo ter repetição
    return(L)

def intersecao (L,M):
    I = list()
    for i in L:
        if i in M and i not in I: #i not in I é apenas para garantir que I não vai ter repetição
            I.append(i)
    return(I)

def main ():

    L = cria_lista()
    M = cria_lista()

    print(L)
    print(M)
    print(intersecao(L,M))

main()
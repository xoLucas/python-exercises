import random

def cria_lista ():

    L = list()
    while len(L) < 10:

        n = random.randint(0,10)
        L.append(n)
    return(L)
'''
def verifica(L):

    R = list()
    
    for i in L:
        iguais = 0
        for j in L:

            if i == j:
                iguais += 1
                if iguais > 1:

                    R.append(i)
    return(R)
'''
def verifica(L):

    A = L.copy()
    R = list()

    for i in L:
        if i in A:
            A.remove(i)
            if i in A and i not in R:
                R.append(i)

    return(R)



def main ():

    L = cria_lista()
    R = verifica(L)

    print(f"A lista de números repetidos é: {R}")
    print(L)

main()
#tente refazer essa solução usando set()
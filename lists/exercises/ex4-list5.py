import random

def criar_lista ():

    D = []

    while len(D) < 60:
        D.append(random.randint(0, 100))
    return(D)

def algoritimo (L):

    a = 0
    b = 30

    for i in range(30):

        x = L[a]
        L[a] = L[b]
        L[b] = x
        a += 1
        b += 1

def main ():

    D = criar_lista()
    E = D.copy()
    algoritimo (E)

    print (D[30])
    print (E[30])
    print(f"Lista normal: {D}")
    print(f"\nLista modificada: {E}")

main()
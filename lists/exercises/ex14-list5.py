import random

def ler_lista():
    L = []
    while len(L) < 30:
        n = random.randint(0,50)
        L.append(n)
    return(L)
def verifica_PI(i):
    if i%2 == 0:
        r = "P"
    else:
        r = "I"
    return(r)
def adiciona_PI(i,r,L,P,I):
    if r == "P":
        if len(P)<10:
            P.append(i)
        else:
            print(f"Lista P: {P}")
            P = []
            P.append(i)
    else:
        if len(I)<10:
            I.append(i)
        else:
            print(f"Lista I: {I}")
            I = []
            I.append(i)
    return(P,I)
def main ():

    L = ler_lista()
    P = []
    I = []

    for i in L:
        r = verifica_PI(i)
        P,I = adiciona_PI(i,r,L,P,I)
    if len(P)<10:
        print(f"Lista P: {P}")
    if len(I)<10:
        print(f"Lista I: {I}")
    print(L)
main()    

import random

def cria_lista ():

    L = []

    '''
    while len(L) < 16:

        L.append(random.randint(0, 100))
    '''
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print(L)
    return (L)

def algoritimo (L):

    for i in range(8):
        a = i+8
        b = L[i]
        L[i] = L[a]
        L[a] = b
    return(L)

def main ():
    
    print(algoritimo(cria_lista()))
    
main()
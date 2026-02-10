import random

def ler_lista ():

    L = list()

    while len(L) < 25:

        n = random.randint(0, 10)
        L.append(n)
    
    '''
    while len(L) < 25:

        n = int(input("Escreva um valor para a lista: "))
        L.append(n)
    '''
    #print(len(L))
    return(L)

def busca_valor (L):

    X = int(input("Digite um valor X qualquer: "))
    ocorrencias = 0

    for i in range(len(L)):

        if L[i] == X:
            
            ocorrencias += 1

            if ocorrencias == 1:

                print(f"A primeira ocorrência foi encontrada na prosição de índice {i}.")
    return(ocorrencias)

def verifica_ocorrencias (o):

    if o == 0:
        print("Não foi encontrado ocorrências.")
    else:
        print(f"Foram encontradas {o} ocorrências.")

    

def main ():

    verifica_ocorrencias(busca_valor(ler_lista()))

main()
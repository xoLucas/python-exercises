def criar_lista ():

    A = []
    while len(A) < 10:

        n = int(input("Me de um número: "))
        A.append(n)
    return(A)

def algoritimo (L):

    print("Valores menores do que 10: \n")
    lista_menor_dez = []

    for i in range(len(L)):

        if L[i] <= 10:

            print(f"A posição {i} armazena o valor {L[i]}")
            lista_menor_dez.append(L[i])

def main ():

    algoritimo(criar_lista())

main()
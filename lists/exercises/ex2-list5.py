def ler_lista ():
    teste1 = []
    
    while len(teste1) < 10:
        
        n = int(input("Escreva um valor inteiro: "))
        teste1.append(n)
    return(teste1)

def forma_teste2 (L):
    teste2 = []

    for i in range(len(L)):

        if i % 2 == 0:
            teste2.append (L[i] * 5)
        else:
            teste2.append (L[i] + 5)
    return(teste2)

def main ():

    lista1 = ler_lista()
    lista2 = forma_teste2(lista1)
    print (f"A primeira lista é: {lista1} e a segunda lista é: {lista2}")

main()
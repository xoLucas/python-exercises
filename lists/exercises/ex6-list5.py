def ler_lista ():

    L = []

    while len(L) < 5:
        n = int(input("Escreva um número: "))
        L.append(n)
    return(L)

def algoritimo (L):

    soma_par = 0
    soma_impar = 0

    for i in range(len(L)):

        if L[i] % 2 == 0:

            soma_par += L[i]
        
        else:

            soma_impar += L[i]
    
    return (soma_par, soma_impar)

def main ():

    A = ler_lista()
    s_p, s_i = algoritimo(A)
    print(f"A soma dos números pares dessa lista é {s_p} e a soma dos números ímpares é {s_i}")

main()
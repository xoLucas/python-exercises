#Faça um algoritmo que leia um lista de números V[6]. Contar a seguir, quantos valores de V são negativos e mostre essa informação.


def pede_lista ():
    V = []
    while len(V) < 6:
        n = int(input("Digite um número: "))
        V.append(n)
    return V

def conta_negativo (L):
    c_n = 0
    for i in L:
    
        if i < 0 :
            c_n += 1
    return c_n

def main ():
    
    print(f"Existem {conta_negativo(pede_lista())} núumeros negativos na lista")

main()
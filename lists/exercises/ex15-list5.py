import random
def ler_lista():
    V = []
    X = []
    while len(V)<10:
        n = random.randint(0,100)
        V.append(n)
    while len(X)<10:
        m = random.randint(0,100)
        X.append(m)
    Y = V + X
    return(Y)
def algoritimo(Y):

    for i in range(len(Y)):
        for j in range(len(Y)):
            if Y[i] > Y[j]:
                Y[i], Y[j] = Y[j], Y[i] #troca atomica do python
    return(Y)
def main():

    Y = ler_lista()
    print(Y)
    print(algoritimo(Y)[::-1])

main()
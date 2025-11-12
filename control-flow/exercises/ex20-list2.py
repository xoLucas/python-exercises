#Faça um programa que, dado três valores a, b e c, verifique se eles podem ser os comprimentos dos lados de um triângulo. Caso positivo, seu programa deve informar se o triângulo é equilátero, isósceles ou escaleno. Caso contrário, seu programa deve escrever a mensagem “Não formam triângulo”.

def triangulo (a, b, c):
    return a + b > c and a + c > b and b + c > a

lado_a = int(input("\nDiga o tamanho de um lado a: "))
lado_b = int(input("Diga o tamanho de um lado b: "))
lado_c = int(input("Diga o tamanho de um lado c: "))

if (triangulo (lado_a, lado_b, lado_c)):
    if ((lado_a**2 + lado_b**2)**(1/2) == lado_c):
        print("O triangulo é retângulo!")
    elif (lado_a != lado_b and lado_b != lado_c and lado_a != lado_c):
        print("O triangulo é escaleno!")
    else:
        print("O triangulo é equilátero!")
else:
    print("A figura não é um triangulo.")
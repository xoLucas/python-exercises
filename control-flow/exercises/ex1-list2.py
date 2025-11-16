#Faça um programa que leia um número inteiro maior que zero e informe se tal número é par ou ímpar

num_1 = int(input("\nMe diga um número inteiro maior do que zero: "))

if num_1%2 == 0:
    print(f"\n{num_1} é par.\n")
else:
    print(f"\n{num_1} é ímpar.\n")
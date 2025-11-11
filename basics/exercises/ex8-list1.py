#Implemente e teste um programa que leia 3 números reais (ponto flutuante) e imprima a sua média aritmética.

print("\nO seguinte programa solicitará 3 números reais e lhe retornará sua média aritmética\n")

num1 = float(input("Me diga o primeiro número: "))
num2 = float(input("Me diga o segundo número: "))
num3 = float(input("Me diga o terceiro número: "))

media = (num1 + num2 + num3)/3

print(f"A média de {num1}, {num2} e {num3} é {media}")
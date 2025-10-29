#Implementação de um programa que leia 3 números inteiros e retorne sua média aritmética

#Explicando o programa ao usuário

print("\nO seguinte programa pedirá 3 números inteiros e retornará a média aritmética deles!\n")

#Pedindo os 3 números

num1 = int(input("Me diga o primeiro número: "))
num2 = int(input("Me diga o segundo número: "))
num3 = int(input("Me diga o terceiro número: "))

#Realizando a média entre eles

media = (num1 + num2 + num3)/3
t = 3 # Casas decimais a truncar
media_truncada = int(media * 10**t)/10**t

#Retornando a média deles

print(f"\nA média de {num1}, {num2} e {num3} é {media_truncada}")

#Implementação de um programa que Leia 2 números inteiros e imprima seu Produto

#Explicando ao usuário o que o programa fará

print("\nO programa a seguir pedirá 2 números inteiros e responderá com o produto deles!\n")

#Pedindo op números ao Usuário

num1 = int(input("Escreva o primeiro número inteiro: "))
num2 = int(input("Escreva o segundo número inteiro: "))

#Realizando seu produto

produto = num1 * num2

#Retornando o produto ao usuário

print(f"O produto dos números {num1} e {num2} é {produto}")
#Implementação de um programa que pede um número inteiro ao usuário e retorna seu antecessor e seu sucessor

#Explicando o programa ao usuário

print("\nO seguinte programa pedirá 1 número inteiro e lhe fornecerá seu antecessor e seu sucessor.\n")

#Pedindo o número ao usuário

num = int(input("Entre com um número inteiro qualquer: "))

#Declarando seu sucessor e antecessor

antecessor = num - 1
sucessor = num + 1

#Retornando antecessor e sucessor ao usuário

print(f"Seu antecessor eh: {antecessor}")
print(f"Seu sucessor eh: {sucessor}")

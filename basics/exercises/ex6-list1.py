#Implementação de um programa que leia duas notas de um aluno, calcule e imprima sua média, sabendo que a primeira nota tem peso 3 e a segunda peso 7.

#Explicando o programa

print("\nO seguinte programa solicitará 2 notas e fará a média delas, sabendo que as notas tem peso 3 e 7 respectivamente\n")

#Pedindo as notas

nota1 = int(input("Coloque aqui a sua nota 1: "))
nota2 = int(input("Coloque aqui a sua nota 2: "))

#Fazendo a média ponderada entre elas

peso1 = 3
peso2 = 7
fator_ponderacao = peso1 + peso2

media_ponderada = ((nota1 * peso1) + (nota2 * peso2))/fator_ponderacao

print(f"A média ponderada de {nota1} com peso {peso1} e {nota2} com peso {peso2} é: {media_ponderada}")
#Escrever um programa que leia três valores correspondentes às medidas dos lados (a, b e c) de uma figura geométrica, e verifica se eles formam ou não um triângulo. Caso os valores formem um triângulo, calcular e escrever a área deste. Caso contrário, escrever os valores lidos com a mensagem: “Não formam triângulo”.
'''
tamanho_a = int(input("Escreva o valor de um dos 3 lados de uma figura geométrica qualquer: "))
tamanho_b = int(input("Escreva o valor de outro dos 3 lados de uma figura geométrica qualquer: "))
tamanho_c = int(input("Escreva o valor de outro dos 3 lados de uma figura geométrica qualquer: "))

if (tamanho_a + tamanho_b <= tamanho_c or
    tamanho_a + tamanho_c <= tamanho_b or
    tamanho_b + tamanho_c <= tamanho_a):
    print("A figura formada pelos 3 lados que você me disse não é um triângulo.")
else:
    print("É um triângulo!")
'''

#tentando fazer com def

def nao_triangulo (a, b, c):
    return a + b <= c or a + c <= b or b + c <= a

lado_a = int(input("Escreva o valor de um dos 3 lados de uma figura geométrica qualquer: "))
lado_b = int(input("Escreva o valor de outro dos 3 lados de uma figura geométrica qualquer: "))
lado_c = int(input("Escreva o valor de outro dos 3 lados de uma figura geométrica qualquer: "))

if (not(nao_triangulo (lado_a, lado_b, lado_c))):
    print("A figura é um triângulo!")
else:
    print("A figura que você criou não é um triângulo")
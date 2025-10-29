#Implementação de um programa que lerá as coordenadas de 2 pontos e calculará a distância Manhattan entre eles.

#Explicando o programa

print("\nO seguinte programa pedirá 2 pontos e responderá com a distância Manhattan entre eles.\n")

#Programa

x1 = int(input("Escreva o x da sua coordenada 1: "))
y1 = int(input("Escreva o y da sua coordenada 1: "))
x2 = int(input("Escreva o x da sua coordenada 2: "))
y2 = int(input("Escreva o y da sua coordenada 2: "))

modulo_dif_x1_x2 = (x1 - x2)**2
modulo_dif_x1_x2 = (modulo_dif_x1_x2)**(1/2)
modulo_dif_y1_y2 = (y1 - y2)**2
modulo_dif_y1_y2 = (modulo_dif_y1_y2)**(1/2)

distancia_manhattan = modulo_dif_x1_x2 + modulo_dif_y1_y2

print(f"A distância Manhattan dos pontos ({x1},{y1}) e ({x2},{y2}) é: {distancia_manhattan}")
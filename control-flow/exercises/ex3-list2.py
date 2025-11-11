#Construa um programa que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.


print("\nO programa a seguir lê dois valores inteiros e, caso a adição deles seja maior que 10, imprimir-lhe-ei: \n")

value_1 = int(input("Me diga um primeiro valor inteiro: "))
value_2 = int(input("Me diga um segundo valor inteiro: "))

if (value_1 + value_2 > 10):
    print(value_1 + value_2)
#else:
    #print("O valor não é maior do que 10.")
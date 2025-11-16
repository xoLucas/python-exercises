#Escreva um programa que leia um número e informe se ele é divisível por 10, por 5 ou por 2, ou se não é divisível por nenhum deles

num = int(input("Me diga um número qualquer: "))

if num%2 == 0:
    print(f"O número {num} é divisível por 2.")
if num%5 == 0:
    print(f"O número {num} é divisível por 5.")
if num%2 == 0 and num%5 == 0:
    print(f"O número {num} é divisível por 10.")
if num%2 != 0 and num%5 != 0:
    print(f"O número {num} não é divisível nem por 2, nem por 5 e nem por 10.")

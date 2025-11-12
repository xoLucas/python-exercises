print("\nO programa a seguir lerá sua idade e lhe classificará como Menor de Idade, Maior de Idade ou Idoso.\n")

idade = int(input("Qual a sua idade? "))

if (idade >= 0 and idade <= 18):
    print("Menor de Idade.")
elif (idade <= 64):
    print("Maior de Idade.")
else:
    print("Idoso.")
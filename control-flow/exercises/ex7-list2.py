#Ler um número inteiro, e verificar se o número corresponde a um mês válido no calendário e escrever o nome do mês, senão escrever uma mensagem ‘Mês Inválido’.

mes = int(input("\nEscreva um número inteiro que corrêsponda a um mês: "))

if (mes < 13 and mes > 0):
    if (mes == 12):
        print("Dezembro!")
    elif (mes == 11):
        print("Novembro!")
    elif (mes == 10):
        print("Outubro!")
    elif (mes == 9):
        print("Setembro!")
    elif (mes == 8):
        print("Agosto!")
    elif (mes == 7):
        print("Julho!")
    elif (mes == 6):
        print("Junho!")
    elif (mes == 5):
        print("Maio!")
    elif (mes == 4):
        print("Abril!")
    elif (mes == 3):
        print("Março!")
    elif (mes == 2):
        print("Fevereiro!")
    elif (mes == 1):
        print("Janeiro!")
else:
    print("Mês inválido.")
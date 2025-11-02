#Implemente e teste um programa que leia um valor de despesa de restaurante, o valor da gorjeta (em porcentagem) e o número de pessoas para dividir a conta, e imprima o valor que cada um deve pagar. Assuma que a conta será dividida igualmente

despesa_rest = float(input("Qual foi o valor de despesa de restaurante? "))
gorjeta = float(input("Qual % será destinada a gorjeta? "))
pessoas_conta = int(input("Quantas pessoas dividirão a conta? "))

print("O valor que cada um deve pagar é: ", (despesa_rest * (1+gorjeta/100))/pessoas_conta)
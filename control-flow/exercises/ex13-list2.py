#Faça um programa que leia a data de nascimento (valores dd, mm e aaaa) de uma pessoa e o dia atual. Calcule e mostre a idade da pessoa em dias, meses e anos. Verifique e mostre, também, se ela já tem idade suficiente para tirar carteira de habilitação e votar. Obs.: Ignore os anos bissextos, ou seja, 1 ano equivale a 12 meses que equivale a 365 dias

dd_nasc, mm_nasc, aaaa_nasc = input("Qual sua data de nascimento (dd/mm/aaaa)? ").split("/")
dd, mm, aaaa = input("Qual a data de hoje (dd/mm/aaaa)? ").split("/")

dd_nasc = int(dd_nasc)
mm_nasc = int(mm_nasc)
aaaa_nasc = int(aaaa_nasc)

dd = int(dd)
mm = int(mm)
aaaa = int(aaaa)

dias_de_idade = dd - dd_nasc + (mm - mm_nasc)*30 + (aaaa - aaaa_nasc)*365

'''#Teste, mas não está correto.
anos_idade = dias_de_idade//365
mes_idade = ((dias_de_idade%365)*12)//10
dias_idade = ((((dias_de_idade%365)*12)%10)*30)//10
'''

print(f"Sua idade em dias é {dias_de_idade} dias, em meses é {dias_de_idade//30} e em anos é {dias_de_idade//365}.")
#print(f"Sua idade é {anos_idade} anos, {mes_idade} meses e {dias_idade} dias.")
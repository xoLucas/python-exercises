value_1 = float(input("\nescreva 1 valor qualquer: "))
value_2 = float(input("\nescreva 1 valor qualquer: "))
value_3 = float(input("\nescreva 1 valor qualquer: "))

if value_1 > value_2 and value_1 > value_3:
    print(f"{value_1} é o maior")
elif value_2 > value_1 and value_2 > value_3:
    print(f"{value_2} é o maior")
elif value_3 > value_2 and value_3 > value_1:
    print(f"{value_3} é o maior")
else:
    print("São iguais")
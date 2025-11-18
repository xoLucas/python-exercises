#Faça um programa que dados três números os imprima em ordem crescente

a, b, c = input("Me diga 3 números quaisquer separados por espaço: ").split( )
a = float(a)
b = float(b)
c = float(c)


'''
if a > b and b > c:
    print(f"{c}{b}{a}")
elif b > a and a > c:
    print(f"{c}{a}{b}")
elif c > a and a > b:
    print(b, a, c)
elif b > a and a > c:
    print(c, a, b)
elif 
'''


if a > b:
    x = a
    if b > c:
        y = b
        z = c
    elif c > a:
        x = c
        y = a
        z = c
    else:
        y = c
        z = b
else: #b > a
    x = b
    if a > c:
        y = a
        z = c
    elif c > b:
        x = c
        y = b
        z = a
    else: #b > c
        y = c
        z = a

print(z, y, x)


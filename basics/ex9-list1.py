#O programa a seguir lê 2 valores inteiros, respectivamente, um valor da hora e um dos minutos e imprimirá o valor equivalente em minutos.


print("\nO programa a seguir pedirá 2 valores inteiros, de horas e minutos separados por espaço e lhe entregará o resultado em minutos\n")

a, b = (input("Me diga 2 valores inteiros, onde o primeiro será a hora e o segundo os mintuos (separe-os por espaço): ").split(" "))
a = int(a)
b = int(b)
resposta = (a * 60) + b

print(f"Tempo decorrido: {resposta} minutos")
#input -> solicite a input for user: a = input("Tell me a number: ")
#output -> print(f"Your number is: {a}")

#test
a = input("Tell me your name: ")
print(f"Your name is: {a}")
b = input("Right? (yes or no): ")

if b == "yes":
    print("Haha, i know!")
elif b == "no":
    print("...so sorry, i dont know :(")
#Calcule a média aritmética das três notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6,0, ou a mensagem "Reprovado", caso contrário.

grade_1 = float(input("Diga a nota 1 do seu aluno: "))
grade_2 = float(input("Diga a nota 2 do seu aluno: "))
grade_3 = float(input("Diga a nota 3 do seu aluno: "))
avg = (grade_1 + grade_2 + grade_3)/3

if (avg >= 6):
    print(f"A média foi {avg} e o aluno foi Aprovado!")
else: 
    print(f"A média foi {avg} e o aluno foi Reprovado.")
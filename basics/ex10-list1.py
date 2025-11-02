#Um programa que lerá 2 horários no formato hora:minuto e imprimirá quanto tempo, no formato hh:mm se passou entre o primeiro e segundo horário

h1_hh, h1_mm =input("Me diga o horário 1 (no formato hh:mm): ").split(":")
h2_hh, h2_mm =input("Me diga o horário 1 (no formato hh:mm): ").split(":")

h1_hh = int(h1_hh)
h1_mm = int(h1_mm)
h1 = (h1_hh*60) + h1_mm 
h2_hh = int(h2_hh)
h2_mm = int(h2_mm)
h2 = (h2_hh*60) + h2_mm

hf = h2 - h1

hf_hh = hf//60
hf_mm = hf%60

print(hf_mm)
print(f"O tempo que se passou entre o primeiro e o segundo horário foi: {hf_hh}:{hf_mm:}")
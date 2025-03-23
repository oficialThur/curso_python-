nota1 = float(input("Digite a nota do primeiro bimestre:"))
nota2 = float(input("Digite a nota do segundo bimestre:"))
nota3 = float(input("Digite a nota do terceiro bimestre:"))

#calculo
total = (nota1 + nota2 + nota3)

#verificação
if total >= 60:
    print("Você passou de ano !!! ",total,)
elif total >= 45:
    print("Você estade recuperação.")
else:
    print("Vocẽ repetiu de ano.")
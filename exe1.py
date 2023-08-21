
nota1= float(input("Digite a primeira nota"))
nota2= float(input("Digite a primeira nota"))
nota3= float(input("Digite a primeira nota"))
nota4= float(input("Digite a primeira nota"))
media= (nota4+nota3+nota2+nota1)/4

if media >= 7:

    print("Aprovado")

elif media>=5 and media<7:
    print("Exame")
else:
    print("Reprovado")


#1)	Escreva um programa que leia um nome completo de uma pessoa e depois mostre letra por letra  for.

#2)	Crie um programa que pegue o nome “João carlos rocha”  e separe usando o split os nomes e só imprima o nome “carlos” na tela usando um loop “for”.

#3)	Leia um texto vindo do teclado e separe ele em pelas letras “o”, texto= “Vamos pensar no dia que você para de ir em casa”, depois conte quantos elementos tem dentro da nova lista.

#•	Len()
#•	Split()

#1) Exercicio 1
nome="Carlos José Maria"

for i in range(len(nome)):
    print(nome[i])

tamanho=len(nome)
print("#"*30)

for i in range(tamanho):
    print(nome[i])


print("#"*30)
for letra in nome:
    print(letra)

print("#"*30)
#2) Exercicio 2

nomeCompleto="João carlos rocha"
nomeSeparado=nomeCompleto.split(" ")

for i in range(len(nomeSeparado)):
    if nomeSeparado[i]=="Carlos":
        print(f"Achei o nome {nomeSeparado[i]}")
    else:
        print(f"O nome que eu não achei foi {nomeSeparado[i]}")

print("#" * 30)
#3) Exercicio 3
texto= "Vamos pensar no dia que você para de ir em casa"
separandoTexto=texto.split("o")
print(separandoTexto)
print(len(separandoTexto))


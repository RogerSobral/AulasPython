#Strings
#vetor
texto="roGerio"  # é um objeto  -Atributos e -metodos
#index  0  1 2 3 4 5 6
# input  | coverter | output
print(texto.upper())
texto= texto.upper()
print(texto)
print(texto.lower())

#texto=input("Digite o seu nome completo:")
texto=texto.lower()
print(texto.title())
print("#"*30)

texto="11/02/1983"
print(texto.strip())

#resposta=input("Desejar entrar no sistema sim ou não").strip()[0].upper()

#if resposta=="S":
#    print("entrou")

#Ele separa os elementos tendo como o nosso separados o simbolo que você passar como parametro
lista=texto.split("/")
print(2023-int(lista[2]))


print("#"*30)
lista=list()
lista.append(1)
lista.append(1)
print(len(lista))
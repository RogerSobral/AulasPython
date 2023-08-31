#Funções

#Eu preciso calcular a média
#Metodo 1
valor1 = 4.5
valor2 = 7
valor3 = 8.5


media = (valor1+valor2+valor3)/3
print(media)

#As duas maneiras vai dar o mesmo resultado
#Metodo 2
valores = [4.5,7,8.5,7]
media = sum(valores) / len(valores)
print(media)


# Imagina que fazer media na minha empresa é um rotina diaria
# vou fazer essa ação de modo pratico
# se eu for criar uma função para o (metodo 1) posso fazer assim:

# Para criar uma função preciso suar a palavra reservada "def"
# O que vai entre os parenteses é chamado de paramentros

print("Funções".center(20,"#"))

#é uma função com parametros posicionais
def media( n1 , n2 , n3):
    if n1.isdigit() and n2.isdigit() and n3.isdigit():
        print((int(n1)+int(n2)+int(n3))/3)
    else:
        print("Você precisa digitar um valor Inteiro")


#n1=input("valor 1")
#n2=input("valor 1")
#n3=input("valor 1")
#media(n1,n2,n3)
media("56","45","112")

# Imagine que quero somar 4 valores
#criar
def soma(n1,n2,n3,n4):
    print(n1+n2+n3+n4)

#usar
soma(45,78,90,1)


#criar
def dividir(n1,n2):
    print(n1/n2)

#usar
dividir(5,109)


def contarTamanho(lista):
    cont=0
    for valor in lista:
        cont=cont+1

    return cont


print(contarTamanho([2,3,4,5,10, "Sobral"]))
print(len([2,3,4,5,10, "Sobral"]))

nome="carlos"
idade=12

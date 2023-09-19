#-*- coding: latin-1 -*-
"""
Orienta��o a Objeto

Programa��o orientada a objetos (POO, ou OOP segundo as suas siglas em ingl�s) � um paradigma de programa��o baseado no conceito de "objetos", que podem conter dados na forma de campos, tamb�m conhecidos como atributos, e c�digos, na forma de procedimentos, tamb�m conhecidos como m�todos. Uma caracter�stica de objetos � que um procedimento de objeto pode acessar, e geralmente modificar, os campos de dados do objeto com o qual eles est�o associados (objetos possuem uma no��o de "this" (este) ou "self" (pr�prio)).

Em POO, programas de computadores s�o projetados por meio da composi��o de objetos que interagem com outros.[1][2] H� uma diversidade significante de linguagens de POO, mas as mais populares s�o aquelas baseadas em classes, significando que objetos s�o inst�ncias de classes, que, normalmente, tamb�m determinam seu tipo.

Fonte: Disponivel em<https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos> Acessado em <13/06/2022>
"""

import datetime as dt


#Classes
# deve-se usar a palavra reservada class
# a primeira letra � maiuscula
#class Pessoa:
#    nome:str
#    data_nasc:str
#    rg:str
#    tel:str


#p1 = Pessoa()
#p1.rg="234455666"
#p1.nome="Rog�rio"
#p1.tel="11 47474747"
#p1.data_nasc=" 22/02/1990"

#print(p1.nome)
#p2=Pessoa()
#print(p2.nome)

# No P1 eu inicializei os valores j� no p2 n�o , por isso vai lan�ar um erro no print

#Construtor

class Pessoa:

    def __init__(self,nome,data,rg,tel):
        self.nome:str=nome
        self.data_nasc:str=data
        self.rg:str=rg
        self.tel:str=tel

#para chamar uma classe devo colocar o nome da classe mais os ( )
p1= Pessoa("Carlos","29/10/2013","1234345","11 23232323")
#print(p1)

p2= Pessoa("pEDRO","30/10/2013","1234345","11 33332323")
#print(p2)

#crie uma classe Animal, colocando os atributos que voc� Achar importante salvar,
# depois Imprime os valores dela

class Animal:


    def __init__(self, tipo,status, classe, porte):
        self.tipo=tipo
        self.status=status
        self.classe=classe
        self.porte=porte



gato=Animal("Felino", True, "Mamifero", "p")


print(Animal("Felino", True, "Mamifero", "p"))


print("#"*30)

class Usuario:

    data_atual=dt.datetime.today().year


    def __init__(self, nome, data,rg,vigor=5):
        self.nome=nome
        self.data_nas=data
        self.rg=rg
        self.vigor=vigor


    def idade(self):
        return Usuario.data_atual - int(self.data_nas)


    def correr(self):
        self.vigor -= 1





user1=Usuario("Pedro","2010","23.233.45-5")


print(f" o vigor � {user1.vigor}")
user1.correr()
user1.correr()
print(f" o vigor � {user1.vigor}")

print(user1.idade())


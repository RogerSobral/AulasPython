#-*- coding: latin-1 -*-
"""
Orientação a Objeto

Programação orientada a objetos (POO, ou OOP segundo as suas siglas em inglês) é um paradigma de programação baseado no conceito de "objetos", que podem conter dados na forma de campos, também conhecidos como atributos, e códigos, na forma de procedimentos, também conhecidos como métodos. Uma característica de objetos é que um procedimento de objeto pode acessar, e geralmente modificar, os campos de dados do objeto com o qual eles estão associados (objetos possuem uma noção de "this" (este) ou "self" (próprio)).

Em POO, programas de computadores são projetados por meio da composição de objetos que interagem com outros.[1][2] Há uma diversidade significante de linguagens de POO, mas as mais populares são aquelas baseadas em classes, significando que objetos são instâncias de classes, que, normalmente, também determinam seu tipo.

Fonte: Disponivel em<https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos> Acessado em <13/06/2022>
"""

import datetime as dt


#Classes
# deve-se usar a palavra reservada class
# a primeira letra é maiuscula
#class Pessoa:
#    nome:str
#    data_nasc:str
#    rg:str
#    tel:str


#p1 = Pessoa()
#p1.rg="234455666"
#p1.nome="Rogério"
#p1.tel="11 47474747"
#p1.data_nasc=" 22/02/1990"

#print(p1.nome)
#p2=Pessoa()
#print(p2.nome)

# No P1 eu inicializei os valores já no p2 não , por isso vai lançar um erro no print

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

#crie uma classe Animal, colocando os atributos que você Achar importante salvar,
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


print(f" o vigor é {user1.vigor}")
user1.correr()
user1.correr()
print(f" o vigor é {user1.vigor}")

print(user1.idade())


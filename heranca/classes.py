# -*- coding: utf-8 -*-

class Animal:
    # nome do animal
    # idade do animal
    # cor do animal
    # espécies do animal
    # porte do animal
    # raça do animal
    def __init__(self, nome, idade, cor,especie, porte, genero):
        self.nome=nome
        self.idade=idade
        self.cor= cor
        self.genero=genero
        self.especie=especie
        self.porte=porte



# veja que cachorro herda de animal os atributos  e tem uma especialização possui patas
class Cachorro(Animal):

    def __init__(self,nome, idade, cor,especie, porte, genero,patas):
        super(Cachorro, self).__init__(nome, idade, cor,especie, porte, genero)
        self.patas=patas
        print("nova classe")

class Gato(Animal):
    ronrronar=True
    pass



#Herança multipla
class PastorAlemao(Cachorro,Gato):
    pass

a = Animal("Bob", "seila","Amarelo","Canis familiaris","Grande","Masculino")
c=Cachorro("Bob", 9,"Amarelo","Canis familiaris","Grande","Masculino",8)
print(c.patas)


# -*- coding: utf-8 -*-
from POO.associacao import Escritor, Ferramenta

"""
#escritor1=Escritor("Carlos")
escritor2=Escritor("Pedro")

#f1=Ferramenta("Caneta")
f2=Ferramenta("Computador")

#escritor1.ferramenta=f1
escritor2.ferramenta=f2
#print(escritor1.ferramenta.escrever())
print(escritor2.ferramenta.nome)
"""

# Crie uma aplicação que vai ter uma classe do tipo (Piloto) e outra do tipo (Carro)
# Faça a Associação deles, lembrando que queremos somente o nome de ambos,
# O Carro vai estar associado ao piloto.
# E a classe carro tem um metodo chamado andar() que mostra uma mensagem
# f"Estou dirigindo o carro {nome do carro}"


class Piloto:

    def __init__(self, nome):
         self.nome=nome
         self.carro=None



class Carro:

    def __init__(self, modelo):
        self.modelo=modelo


    def andar(self):
        print(f"Estou dirigindo o carro {self.modelo}")



p1=Piloto("José")
c1=Carro("Siena 2010")
print(c1)
p1.carro=c1
print(p1.carro.modelo)
# Piloto/nome
# Piloto/carro/modelo
# Piloto/carro/cor
# Piloto/carro/motor
# Piloto/carro/marca

# -*- coding: utf-8 -*-

class Escritor:

    def __init__(self, nome):
        self.nome=nome
        self.ferramenta=None




class Ferramenta:

    def __init__(self, nome):
        self.nome = nome


    def escrever(self):
        print(f"Estou escrevendo um texto usando {self.nome}")


if __name__ == "__main__":
    print("rogerio")

    for i in range(10):
        print(i)
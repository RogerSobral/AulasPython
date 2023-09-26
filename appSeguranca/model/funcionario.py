#-*- coding: utf-8 -*-
import datetime as dt

import appSeguranca.util.verificador as verificar

class Funcionario:

    #Construtor
    def __init__(self, nome, data_nasc,cargo, contato, senha, nivel):
        self.__nome=nome
        self.__cpf=None
        self.__data_nasc=data_nasc
        self.__cargo=cargo
        self.__contato=contato
        self.__senha=senha
        self.__nivel=nivel

#getter
    @property
    def nome(self):
        return self.__nome

#Setter
    @nome.setter
    def nome(self, nome):

        self.__nome=nome


#getter
    @property
    def cpf(self):
        return self.__cpf

#Setter

    @cpf.setter
    def cpf(self, cpf):

        if  verificar.validarCPF(cpf)!=None:
            self.__cpf= verificar.validarCPF(cpf)
        else:
            print("CPF não é valido")

#getter
    @property
    def data_nasc(self):
        return self.__data_nasc

#Setter
    @data_nasc.setter
    def data_nasc(self, data_nasc):
        self.__data_nasc=data_nasc

    # getter
    @property
    def cargo(self):
        return self.__cargo

    # Setter

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo


    # getter
    @property
    def contato(self):
        return self.__contato

    # Setter

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

    # getter
    @property
    def senha(self):
        return self.__senha

    # Setter

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def nivel(self):
        return self.__nivel

    # Setter

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    def idade(self):
        anoAtual=dt.datetime.today().year
        return anoAtual - int(str(self.data_nasc).split("/")[2])


    def __str__(self):
        return f"{self.nome} {self.cpf} {self.data_nasc} {self.cargo} {self.contato} {self.senha} {self.nivel}"





nome="Carlos"
cpf="12344"
data_nasc="29/07/1983"
cargo="Segurança"
contato=1
senha="123"
nivel="ADM"

f1=Funcionario(nome,data_nasc,cargo,contato,senha,nivel)

print(f1.idade())
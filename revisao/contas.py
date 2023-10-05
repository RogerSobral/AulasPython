# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, valor, cliente):
        self.__saldo = valor
        self.__cliente = cliente
        self.__status = True
        self.__id=None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def status(self):
        return self.__status

    def alterarStatus(self, status:bool):
        self.__status=status



    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor):
        self.__saldo=valor

 #Quando eu usar esse metodo tenho que tratar o erro
    def deposito(self, valor):
        if self.status:
            self.__saldo += valor
        else:
            raise "A conta não esta ativa"

    @abstractmethod
    def saque(self,valor): # assinatura
        pass


class ContaCorrente(Conta):

    def __init__(self,valor:float, cliente,limite:float):
        super().__init__(valor, cliente)
        self.__limite=limite


    @property
    def limite(self):
        return self.__limite

    def saque(self,valor):
        if self.status:
            if isinstance(valor,(int, float)):
                if self.saldo>= valor:
                    self.saldo = valor
                elif self.saldo+self.__limite>=valor:
                    self.saldo=self.saldo-valor
                    self.__limite=self.__limite+self.saldo
                    print("Você esta no limite")
                else:
                    raise "Saldo não cobre o valor de saque"
            else:
                raise "Digite um valor valido"
        else:
            raise "A conta não esta ativa"



class ContaPoupanca(Conta):

    def saque(self,valor):
        if self.status:
            if self.saldo>=valor:
                self.saldo-=valor
            else:
                raise "Você não tem saldo."
        else:
            raise "A conta não esta ativa"


class Cliente:

    def __init__(self, nome:str, data_nasc:str ):
        self.nome=nome
        self.data_nasc=data_nasc
        self.__id=None


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id=id





if __name__ == '__main__':
    cp= ContaPoupanca(1200,"Carlos")
    cc = ContaCorrente(1100, "Maria",1000)

    print(cp.saldo)
    cp.deposito(350)
    print(cp.saldo)
    cp.saque(1230.56)
    print(cp.saldo)

    cp.saque(300.56)
    print(cp.saldo)



    print("#" * 30)
    print(cc.saldo)
    cc.deposito(350)
    print(cc.saldo)
    cc.saque(1700)
    print(cc.saldo)
    print("Limite")
    print(cc.limite)

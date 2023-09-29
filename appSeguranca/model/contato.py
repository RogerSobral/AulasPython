from typing import Any
import appSeguranca.util.verificador as verificar

class Contato:

    id_da_classe=0
    def __init__(self, email, telefone, rua, numero, bairro, cep, cidade, estado):
        self.__email=email
        self.__telefone=telefone
        self.__rua=rua
        self.__bairro=bairro
        self.__numero=numero
        self.__cep=cep
        self.__cidade=cidade
        self.__estado=estado
        self.__id=Contato.addID()

    @classmethod
    def inicializadorID(csl, id):
        csl.id_da_classe=id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email=email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if verificar.validarTelefone(telefone)!=None:
            self.__telefone = verificar.validarTelefone(telefone)
        else:
            print("Telefone Invalido")


    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep


    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado


    def __str__(self) -> str:
        return f"{self.id} {self.email} {self.telefone} {self.rua} {self.numero} {self.bairro} {self.cidade} {self.cep} {self.estado}"


    @property
    def id(self):
        return self.__id
    @classmethod
    def addID(csl):
        csl.id_da_classe += 1
        return  csl.id_da_classe





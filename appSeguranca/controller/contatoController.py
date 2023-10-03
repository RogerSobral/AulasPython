from appSeguranca.model.contato import Contato

class ControllerContato:

    def __init__(self,email, telefone, rua, numero, bairro, cep, cidade, estado):
        self.contato=Contato(email, telefone, rua, numero, bairro, cep, cidade, estado)
        self.contato.inicializadorID(
            self.lerUltimoIdContatosTxt())
        self.criarTxtContato(self.contato)


    def criarTxtContato(self, contato):
        with open(r"C:\Users\rogerio.sribeiro\PycharmProjects\AulasPython\appSeguranca\tabelas\contato.txt", "a") as file:
            file.writelines(f'\n{contato.__str__()}')
            return f"Arquivo Salvo com sucesso ! {file.name}"

    def id(self):
        return self.contato.id



    def lerUltimoIdContatosTxt(self):
        with open(r"C:\Users\rogerio.sribeiro\PycharmProjects\AulasPython\appSeguranca\tabelas\contato.txt", "r+") as file:
            lista=list()
            separador=file.read().split(" ")
            print(separador)




            return lista




c=ControllerContato("email", "telefone", "rua", "numero", "bairro", "cep", "cidade", "estado")

#print(c.lerUltimoIdContatosTxt())
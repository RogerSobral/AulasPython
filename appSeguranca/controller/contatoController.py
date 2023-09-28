from appSeguranca.model.contato import Contato

class ControllerContato:

    def __init__(self,email, telefone, rua, numero, bairro, cep, cidade, estado):
        self.contato=Contato(email, telefone, rua, numero, bairro, cep, cidade, estado)
        self.criarTxtContato(self.contato)
    def criarTxtContato(self, contato):
        with open("tabelas/contato.txt", "a+") as file:
            file.write((f'{contato.__str__()}\n'))
            return f"Arquivo Salvo com sucesso ! {file.name}"

    def id(self):
        return self.contato.id
from appSeguranca.model.funcionario import Funcionario
class FuncionarioController:

    def __init__(self,nome,cpf,data_nascimento,cargo,id,senha,nivel):
        self.nome=nome
        self.cpf=cpf
        self.data_nascimento=data_nascimento
        self.cargo=cargo
        self.id=id
        self.senha=senha
        self.nivel=nivel

        self.funcionario=Funcionario(self.nome,self.data_nascimento,self.cargo,self.id,self.senha,self.nivel)
        Funcionario.cpf=cpf

        self.criarTxtFuncioario(self.funcionario)

    def criarTxtFuncioario(self, funcionario):
        with open("tabelas/funcinario.txt","a+") as file:

            file.write(f'{funcionario.__str__()}\n')
            return f"Arquivo Salvo com sucesso ! {file.name}"








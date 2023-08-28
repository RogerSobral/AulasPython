#Sistema de controle


usuarios = list()

while True:

    #Pegando os dados do usuario
    nome=input("Digite o seu nome: ")
    rg=input("Digite o seu rg: ")
    ano_nasc=int(input("Digite o ano em que nasceu: "))
    tel1=input("Digite o seu Primeiro telefone: ")
    tel2=input("Digite o seu Segundo telefone: ")


    telefones = list() # criando uma lista de telefones desse usuario
    telefones.append(tel1) # add o tel 1 dentro da lista de telefones
    telefones.append(tel2) # add o tel 1 dentro da lista de telefones

    # vou começar a Cadastrar uma despesa
    print("Cadastrando a despesa")
    #pegando os dados da despesa
    descricao=input("Descrição da Despesa: ")
    valor=float(input("Valor da Despesa: "))

    #criando um dicionario de um usuario
    dicionario={"nome":nome,"rg":rg,"ano":ano_nasc,"telefones":telefones,
                "despesas":{"descricao":descricao, "valor":valor}}

    usuarios.append(dicionario)

    resposta=input("deseja Continuar sim ou não").strip()[0].lower()
    if resposta=="n":
        break

print(usuarios)

#Estudar

#dicionario2 =[
#    {"nome":nome,"rg":rg,"ano":ano_nasc,"telefones":["1145454545","145454545"]},

#    {"nome":"Carlos","rg":"121212","ano":2010,"telefones":["114444444","1145454545"]}
#]

#print(dicionario2[0]["telefones"][0])
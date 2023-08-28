#Trabalhando com Listas 2
#Pegando data do sistema
#importar uma lib
import datetime as dt


#anoAtual= dt.date.today().year
#print(f"Data: {anoAtual}")

#Incerindo valores na lista
listaTeste=[1,2] # aqui eu estou iniciando minha lista com 2 valores
print(listaTeste[0]) # estou lendo o primeiro valor na lista
listaTeste[0]=5 # estou atualizando o end 0 da minha lista com um novo valor
print(listaTeste[0])
print("#"*30)

# Exe.1 criar uma lista com 3 nomes e modifique os seus valores
nomes=["rogerio","pedro","maria"]
nomes[0]="Mudei 1"
nomes[1]="Mudei 2"
nomes[2]="Mudei 3"
print(nomes)

print("#"*30)
#vamos colocar todas com letra maiusculas
lista = ["rogerio","pedro","maria","joão"]
print(lista)
for i in range(len(lista)):
#    pos 0  = pos 0  transforma em title
    lista[i] = lista[i].upper()

print(lista)

#outra maneira de gerar uma lista
print("#"*30)
novaLista=list()

print(type(novaLista))

#Add valores dentro da minha lista
novaLista.append("Rogério")
novaLista.append("Carlos")
novaLista.append(1)
novaLista.append(34.56)
print(novaLista)

#diferente maneira de criar lista
novaLista2=[]
novaLista2.append("T")
novaLista2.append("D")
novaLista2.append("A")
novaLista2.append("B")
novaLista2.append("A")
print(novaLista2)
# cont() vai contar a ocorrencia do paramentro
print("Quantidade de A :",novaLista2.count("A")) # ele retorna a quantidade
novaLista2.remove("D") # ele remove o valor e atualiza a lista
print(novaLista2)

novaLista2.append("a")
novaLista2.sort() # organiza e não retorna nada, atualiza a lista
print(novaLista2)

# Estudo de listas dentro de listas
"""
print("#"*39)
listas=[
         ["Pedro","1235","678888","1990"],
         ["Maria","333333","5555555","2010"],
         ["Carlos","34343434","7777777","2019"],
       ]

print(listas[1][0])
"""
# Vamos Praticar
# Primeira Parte
# vamos criar um programa de cadastro de usuarios
# vamos cadastrar: Nome | RG | CPF | Ano_nasc
# O nosso sistema vai estar dentro de um loop
# Cadastrando varios usuarios
# só vamos sair do cadastro quando estivermos prontos


print("#"*30)

print("Seja Bem vindo ao Sistema!")
print("Você precisa Logar para entrar no sistema:")
nome:str = input("Digite seu nome: ")
senha:str = input("Senha: ")

clientes=list()

# validando a entrada no sistema
if nome in ["pedro", "maria", "santos", "josé"] and senha =="1234":

    while True : # vou fazer um loop para poder ficar cadastrando pessoas livrimente
        print("""
        Para cadastrar clientes digite 1 :
        Para mostrar a idade dos usuarios digite 2:
        Para mostrar todos os usuarios no sistema digite 3:
        Deseja sair do sistema digite 4: 
        """)
        menu= int(input("Digite qual opção você deseja fazer: "))


        if menu==1:
            print("Tela Cadastrando Cliente")

            nome:str = input("Digite seu nome: ")
            rg: str = input("Digite seu rg: ")
            cpf: str = input("Digite seu cpf: ")
            ano_nasc:int = int(input("Digite o seu Ano de Nascimento: "))

            cliente=[nome,rg,cpf,ano_nasc] # criar um cliente novo
            clientes.append(cliente) # add o cliente novo na lista


        elif menu==2:

        #Calcular a idade

            #para pegar cada lista
            for linha in range(len(clientes)):
                idade= dt.date.today().year-clientes[linha][3]
                print(f"Cliente: {clientes[linha][0]} idade: {idade}")

        if menu == 3:
            print(clientes)
        if menu==4:
            break



else:
    print("Nome ou senha não existe no sistema")




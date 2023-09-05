#Funções 2
#Importação
import datetime as dt

#def somar(n1:float,n2:float,n3:float):
#    return n1+n2+n3 # ele vai me retornar a soma em um tipo float

#print(type(somar(123.45,56,67.89)))


# O procedimento não devolve nada
def multiplicacao(numero1,numero2):
    mult=numero1*numero2
    print(mult)


# Função devolve um valor, cujo o tipo é o retorno do objeto
def multiplicacao2(numero1,numero2):
    mult=numero1*numero2
    return mult



multiplicacao(45678,565656)

multiplicacao(13,565656)


print("Valor Multiplicado ",multiplicacao2(45678.78,565656))

#Maquina de refri

def maquina(Garrafa,liq):
    print(Garrafa+" ",liq)

print("#"*40)
#Ela so faz o que esta dentro dela não retornando nada
def separarNome(nomeCompleto):
    lista=nomeCompleto.split(" ")
    print(lista)

def separarNome2(nomeCompleto):
    lista=nomeCompleto.split(" ")
    return lista


separarNome("Rogério Sobral Ribeiro")
print("Separando os nomes usando a função 2")

#A função se torna o que retorna
separarNome2("Rogério Sobral Ribeiro")

lista=["Rogério","Sobral","Ribeiro"]
lista

"""
def validarCPF(cpf):
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
        return False

cpf=input("Digite o seu cpf").strip()
nome=input("Digite o seu nome")
cliente=list()

if validarCPF(cpf):
    cliente.append(nome)
    cliente.append(cpf)
    print("Cadastrado com sucesso!")
else:
    print("Cpf invalido")
"""
print("#"*30)
nome="carlos"


def titulo():

    return nome.title()


print(titulo().center(20,"#"))

for i in range(10):
    titulo()

# trabalhando com uma lista como parametro

def somatoria(n1,n2,n3,n4,n5):
    return n1+n2+n3+n4+n5

print(somatoria(23,55,105,3,45))


def somatoria2(lista):
    soma=0
    for valor in lista:
        soma+=valor
    return soma

lista2=[3,5,56,102,45, 56,999]

print(somatoria2(lista2))

# 1 Exercicio
# Criar uma função que calcule a idade de alguem
# sabendo que ele vai entrar com o ano em que nasceu como parametro
# vai ter que importar a biblioteca datetime para pegar o ano atual

print("Exer1".center(30,"#"))
def idade(ano_nasc):
    if ano_nasc.isdigit() and len(ano_nasc)==4:
        return dt.datetime.today().year - int(ano_nasc)
    else:
        return -1



print(idade("1994"))


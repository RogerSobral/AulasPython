# Funções v.2

from datetime import datetime



def mensagem(resposta):
    if resposta=="1":
        print("Você pediu para Imprimir")
    elif resposta =="2":
        print("Você pediu para salvar")
    elif resposta =="3":
        print("Você pediu para sair")
    else:
        print("digite um valor valido")



#while True:
#    print("""
#    Para imprimir digite-> 1
#    Para salvar digite-> 2
#    Para sair digite-> 3
 #   """)
 #   resposta = input("Qual opção deseja: ")
#    mensagem(resposta)
 #   if resposta=="3":
 #       break

#Funções Nomeadas e posicionais

def pessoa(nome, idade,rg):
    nome=nome.strip()
    idade=idade.strip()
    rg=rg.strip()

    if len(nome)!=0 and nome.isalpha():
        if idade.isdigit() and len(idade)<3:
            if int(idade)<=120:
                if len(rg)>=9 and len(rg)<11:

                    return {"nome": nome, "idade": idade, "rg": rg}

                else:
                    print("O valor do RG não é valido")
            else:
                print("A idade deve ser menor do que 120 anos")
        else:
            print("O valor de idade deve ser Numerico")
    else:
        print("Nome digitado não é valido:")



print("Cadastro de Pessoa".center(30,"#"))



"""
x=0
pessoas=list()
while True:
    nome=input("Digite o seu nome: ")
    idade=input("digite a sua idade: ")
    rg=input("digite a sua rg: ")
    if isinstance(pessoa(nome,idade,rg),dict):
        pessoas.append(pessoa(nome,idade,rg))
    x+=1
    if x==2:
        break

print(pessoas)
"""
#Exe2
# Criar uma função que cadastre uma lista de produtos, onde cada produto vai ter:
# Tipo -> ok
# Descrição  ->ok
# Quantidade -ok
# Você deve validar o campo quantidade para ser um int -> ok

def produto(descricao, tipo,quantidade):
    descricao=descricao.strip()
    tipo=tipo.strip()
    quantidade=quantidade.strip()
    if quantidade.isdigit():
        return {"descricao":descricao,"tipo":tipo,"quantidade":int(quantidade)}
    else:
        print("O valor da quantidade não é valido")


produtos=list()

while True:
    descricao=input("Digite a descrição do produto: ")
    tipo = input("Digite o tipo do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    if isinstance(produto(descricao=descricao,tipo=tipo,quantidade=quantidade),dict):
        produtos.append(produto(descricao=descricao,tipo=tipo,quantidade=quantidade))
    else:
        print("Não foi possivel cadastrar")

    resp=input("Deseja sair sim ou não").strip()[0].upper()

    if resp=="S":
        break

print(produtos)




#exe 3:
#Criar um sistema que cadastre as receitas financeiras
# descrição   -> ok
# valor (validar o valor)  -> ok
# data   -> ok
# categoria -> ok
# salvar como um dicionario cada receita -> ok
# salvar dentro de uma lista de receitas -> ok
# mostrar na tela -> ok

def verificarValor(valor):
    valor=valor.strip()
    if valor.isdigit() or str.isdigit(valor.replace(".", "")) or str.isdigit(valor.replace(",", "")):
        valor=valor.replace(",",".")
        return float(valor)


#"234.567

def receita(descricao, valor,data,categoria):
    descricao=descricao.strip()
    data=data.strip()
    categoria=categoria.strip()
    # eu vou criar uma função para validar meu valor
    if isinstance( verificarValor(valor), float):
        return {"descricao":descricao,"data":data,"categoria":categoria,"valor":verificarValor(valor)}

    else:
        print("Valor digitado errado")


receitas=list()
while True:
    descricao=input("Digite a descrição da receita: ")
    valor = input("Digite o valor da receita:  ")
    data = datetime.today()
    categoria= input("Digite a categoria da receita:  ")
    if isinstance(receita(descricao,valor,data,categoria),dict):
        receitas.append(receita(descricao,valor,data,categoria))
    else:
        print("Não foi possivel cadastrar")

    resp=input("Deseja sair sim ou não").strip()[0].upper()

    if resp=="S":
        break

#vamos imprimir as receitas de modo organizado

print(receitas)


#exe 4:
#Criar um sistema que para cadastrar livros
# Titulo
# autor
# data
# Editora
# salvar como um dicionario cada livro
# salvar dentro de uma lista de livros
# mostrar na tela





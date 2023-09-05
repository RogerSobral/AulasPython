# Funções v.2
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
#Criar um sistema que cadastra receitas financeiras
# descrição
# valor ( validar o valor)
# data
# categoria
# salvar como um dicionario cada receita
# salvar dentro de uma lista de receitas
# mostrar na tela

#exe 4:
#Criar um sistema que para cadastrar livros
# Titulo
# autor
# data
# Editora
# salvar como um dicionario cada livro
# salvar dentro de uma lista de livros
# mostrar na tela


# Função args kargs



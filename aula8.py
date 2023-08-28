#Collections
# List
# . permite buscar pelo index
# . Listas são mutaveis
# Tupla
# . permite buscar pelo index
# . tuplas não são mutaveis
# Dict
# Set

lista=[12,45,55,66,1]

lista.append(70)

# Pegar index
print(lista[2])

#Multavel
lista[1]=67

for i in range(len(lista)):
    print(lista[i])

print("#"*30)

#           [12,45,55,66,1]
for n,valor in enumerate(lista):
    print(valor)


#Tupla

tupla=(2,378,34,67)
print(tupla[0])
#tupla[1]=78  isso não é permitido
print(tupla[1])

#1) Maneira
for i in range(len(tupla)):
    print(tupla[i])
print("#"*30)

#2) Maneira
# Pegando somente o valor
for valorTupla in tupla:
    print(f"  valor: {valorTupla}")


#3) Maneira
# dessa maneira eu posso pegar o numero do index de cada valor e atribuir a uma variavel temporaria
#                  0, 1, 2, 3
#                 (2,378,34,67)
for num,valorTupla in enumerate(tupla):
    print(f"posição: {num}  valor: {valorTupla}")


#dict
#print("#"*30)
aluno={"nome":"Carlos","idade":34,"RG":"567.78.23-45"}

#pegando as chaves
#chaves=aluno.keys()
#print(chaves)

#pegando os valores
#valores=aluno.values()
#print(valores)

#pegando os itens
#itens= aluno.items()
#print(itens)

#Pegando somente os valores
for n,valor in enumerate(aluno.values()):
    print(f"numero: {n} valor:{valor}")

#
for n,chave in enumerate(aluno.keys()):
    print(f"numero: {n} valor:{chave}")

print("#"*30)
print("Break")
for chave,valor in aluno.items():
    if chave=="idade":
        break
    print(f"Chave: {chave} valor:{valor}")

print("#"*30)
print("continue")

#  "nome":"Carlos","idade":34,"RG":"567.78.23-45"
for chave,valor in aluno.items():
    print(f"Chave: {chave} valor:{valor}")
    if chave=="idade":
        continue
    print("Passo pelo continue")


print("#" * 30)
#Criando uma nova chave e valor
aluno["cpf"]="444.555.666-78"

for n,chave in enumerate(aluno.keys()):
    print(f"numero: {n} valor:{chave}")

#mudar um valor
aluno["nome"]="Pedro"


print("#" * 30)

alunos=[
    {"nome":"Carlos","idade":34,"RG":"567.78.23-45"},
    {"nome":"Pedro","idade":18,"RG":"777.78.23-45"},
    {"nome":"Maria","idade":22,"RG":"666.786.45-00"}
]
print(alunos[0]["RG"])

#Estou cadastrando varios dicionario em loop dentro da minha lista
while True:
    nome=input("digite o seu nome: ")
    idade=int(input("digite sua idade: "))
    rg=input("digite seu RG: ")
    alunos.append({"nome":nome, "idade":idade, "RG":rg})
    resposta=input("deseja continuar sim ou não").strip()[0].upper()
    if resposta=="N":
        break
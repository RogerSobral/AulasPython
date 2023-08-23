
#Quando eu tiver duas opções de valores que depende de uma condição
# Posso usar o operador ternario
media=8.7
nome="Aprovado"if media >=8 else "Reprovado"
print(nome)

print("#"*30)

#Aluno 1
nome1="Carlos"
idade1=45
nota1_aluno_1=7
nota2_aluno_1=6
nota3_aluno_1=8
media_a1=(nota1_aluno_1+nota2_aluno_1+nota3_aluno_1)/3
#Aluno 2
nome2="Pedro"
idade2=45
nota1_aluno_2=9
nota2_aluno_2=9
nota3_aluno_2=7.9
media_a2=(nota1_aluno_2+nota2_aluno_2+nota3_aluno_2)/3
print(f"Aluno {nome1} tirou a média: {media_a1}")
print(f"Aluno {nome2} tirou a média: {media_a2}")

# Estudos de Listas
# Primeira versão
#index      0     1  2   3  4
#aluno1=["carlos",45,7.7,6.5,8]

#print("Nome: ",aluno1[0])
#print("Idade: ",aluno1[1])
#print("Nota1: ",aluno1[2])
#print("Nota2: ",aluno1[3])
#print("Nota3: ",aluno1[4])

# quero somente usar as notas
#media=(aluno1[2]+aluno1[3]+aluno1[4])/3
#print(f"Nome {aluno1[0]} tirou a média {media}")

# Metodos de uma lista

#print(len(aluno1)) # a quantidae de elementos

#index   0 1  2   3
#numeros=[3,5,67,100.89,67,100]
#sum(jogar a lista aqui dentro) é a  função que soma todos os valores dentro de uma lista
#print(sum(numeros)/len(numeros))

# Segunda versão
#estou criando uma lista so para nostas e essa lista esta dentro da principal
#index     0      1       2
aluno1=["carlos",45,[7.7,6.5,8]]
#index lista interna 0    1  2
print("Média: ",sum(aluno1[2])/len(aluno1[2]))

# digamos que eu quero pegar um valor da nota sendo ela a primeira
print(aluno1[2][1])

# Criar uma lista que vai conter o nome do cliente
# criar uma lista interna que vai ter o contato ( tel, email)
# criar uma lista  interna que tenha 3 notas do cliente
# 1) imprima o nome do cliente
# 2) imprima o somente o telefone  do cliente
# 3) imprimir a soma das notas sum()
# 4) imprimir a contagem do numero das notas len()
# 5) imprimir a a media das notas do cliente junto com o seu nome

# -*- coding: utf-8 -*-
import timeit


# Boolean

# True False

# se for numero e ele for igual a 0 vai ser False
# se for numero e ele for diferente de 0 vai ser True


variavel = -18
n2 = variavel+1

#if variavel:
#    print("Esta dentro")
#else:
#    print("Final")
"""
texto=input("Digite o seu nome: ").strip()

if texto:
    print("Entrou dentro da condição com texto")
else:
    print("Não Entrou dentro da condição com texto")
"""

#lista=[]
#lista.append("s")
#if lista:
#    print("Entrou dentro da condição com lista")
#else:
#    print("Não entrou dentro da condição com lista")




#print("Tempo: ",timeit.timeit('''lista2= [23,56,67,777,123,789,908,1090,44,88];lista=for valores in lista2:print(valores)''',number=1000000))

#valor=[x for x in lista2 if x%2==0]

#print(valor)

#for x in lista:
#    print(x)
"""
lista2= [23,56,67,777,123,789,908,1090,44,88]
compa_list=(x for x in lista2 if x>50)
for valor in compa_list:
    print(valor)

for valor in compa_list:
    print(valor)
"""
#print("List Comprehension",timeit.timeit('''lista2= [23,56,67,777,123,789,908,1090,44,88,23,56,67,777,123,789,908,1090,44,88,23,56,67,777,123,789,908,1090,44,88];compa_list=[x for x in lista2 if  x % 2 == 0]''', number=1000000)," milissegundos")
#print("Generator Expression",timeit.timeit('''lista2= [23,56,67,777,123,789,908,1090,44,88,23,56,67,777,123,789,908,1090,44,88,23,56,67,777,123,789,908,1090,44,88];generation=(x for x in lista2 if  x % 2 == 0)''', number=1000000), " milissegundos")


print("List Comprehension",
      timeit.timeit('''[x for x in range(10000)]''', number=1000000), " milissegundos")

print("Generator Expression",
     timeit.timeit('''(x for x in range(100000))''', number=1000000), " milissegundos")
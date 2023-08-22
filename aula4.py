from typing import Final



#String é vista como um Vetor de elementos
#Existe uma diferença entre o valor do indice e o tamanho do objeto
# indice  0 1 2 3 4
# len     1,2,3,4,5
#nome="Pedro"

texto="stsrsrsrlrkslr"
# Len() conta a quantidade de elementos dentro do meu vetor
#print(len(texto))
#print(texto[1:4])
# intervalo  1   - 8



# for
#( 1,2,3,4,5,6,7,8,9)
# i = 1
# range (1ª= inicio | 2ª= Fim | 3ª= passo)
#n=range(1,9)

#interar a String texto
#indice 0 1 2 3 4 5 6 7 8 9 10 11 12 13
#"     (s,t,s,r,s,r,s,r,l,r,k ,s, l, r)"
#for i in range(len(texto)):
#    print(texto[i])

#"(s,t,s,r,s,r,s,r,l,r,k,s,l,r)"
#for letras in texto:
#    print(letras)

#for i in range(1,11):
#    for j in range(1,11):
#        print(f"{i}x{j}={i*j}")
#    print("#"*30)


#( 1,2,3,4,5,6,7,8,9)
#n="srrtsrstyy"
#len(n) # o tamanho em elementos

#gerando um range (10) usando uma tupla gera um intervalo
#for i in (0,1,2,3,4,5,6,7,8,9):
#    print(i)


#Usando o range geram os mesmos resultados
#for i in range(10):
#    print(i)


#print("#"*30)
#Constante
VALOR:Final =23

VALOR=45

idade:int=13
idade="srsrs"
nome:str="Rogerio"
#nome=12
#print(type(nome))

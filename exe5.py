# -*- coding: latin-1 -*-

# Voc� deve criar uma aplica��o que vai cadastrar 4 topicos
#salvando esses topicos, na seguinte formata��o dentro do arquivo txt
import sys
#|__Topico 1
#    |__Topico 2
#        |__Topico 3
#            |__Topico 4

try:
    arquivo=open("topicos.txt","+a")
    tab = ""
    for i in range(4):
        topico = input("Digite o topico Desejado")
            # "|__Topico 1
            #    |__Topico 2
        arquivo.write(f'{tab}|__{topico}\n')
        tab = tab+"\t"
except Exception as e:
    print("N�o foi possivel salvar dentro do arquivo\nErro:",e)
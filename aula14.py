#-*- coding: latin-1 -*-
#Gerenciador de Contexto
#Ele nos ajuda e fechar nosso contexto caso venhamos esquecer.
'''
with open("despesas.txt","+a") as despesas:
    print(despesas.closed)
    for i in range(1):
        #topicos=input("Digite um topico: ")
        despesas.writelines("""
|__Topico 2
    |__Topico 3
        |__Topico 4
        """)
'''

def despesa(descricao,valor,data):
    #Depois vamos tratar melhor essa fun��o
    return [descricao,valor,data]


despesas=list()
while True:
    print("""
    Op��o 1-> Cadastrar despesas
    Op��o 2-> sair do sistema
    Op��o 3-> salvar em um arquivo txt
    """)

    ask=input("Qual op��o deseja: ")
    if ask=="1":
        print("Cadastro".center(30,"#"))
        descricao= input("Descri��o: ")
        valor = float(input("Valor: "))
        data = input("Data")
        despesas.append(despesa(descricao,valor,data))
    elif ask=="2":
        break
    elif ask == "3":
        try:
          with open("despesas.txt","+a") as arquivo:
              for des in despesas:
                  for  num, atributos in enumerate(des):
                      if num!=(len(des)-1):
                          arquivo.write(f'{atributos},')
                      else:
                          arquivo.write(f'{atributos}')
                  arquivo.write("\n")
        except Exception as e:
            print("N�o foi possivel salvar o arquivo")
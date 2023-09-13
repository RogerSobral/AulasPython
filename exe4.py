#  Exe.1 = Cadastrar 5 nomes em um arquivo txt -> ok
#  Exe.2 = ler os 5  nomes em um arquivo txt -> ok
#  Exe.3 = salvar esses nomes em uma lista  ->

"""
try:
    nomes=open("nomes.txt","+a", encoding="utf-8")
    nomes.close()
except Exception as e:
    print("Não foi possivel criar o arquivo")


try:
    nomes=open("nomes.txt","+a",encoding="utf-8")
    for i in range(5):
        if i !=4:
            nomes.write(f'{input("digite um nome")},')
        else:
            nomes.write(f'{input("digite um nome")}')

except Exception as e:
    print("Não foi possivel criar o arquivo")

finally:
    nomes.close()

"""
try:
    arquivo=open("nomes.txt","r")
    palavras=arquivo.read().split(",")
    for palavra in palavras:
        print(palavra)
except Exception as e:
    print("Não foi possivel ler os nomes Erro:",e)
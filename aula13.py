# Trabalhando com Inputs e outputs IO

try:
    arquivo = open("texto.txt","x")

except FileExistsError as e:
    print("O arquivo já existe")


# Excrevando algo no txt

texto=input("Digite alguma coisa")
try:
    arquivo=open("texto.txt","w")
    arquivo.write(texto)
except Exception as e:
    print("Não foi possivel escrever erro: ", e)
finally:
    arquivo.close()



#Add mais texto no meu txt

newText=input("Digite alguma coisa")
try:
    arquivo=open("texto.txt", "a")
    arquivo.write(newText)
except Exception as e:
    print("Não foi possivel add mais textos")
finally:
    arquivo.close()



try:
    arquivoLer = open("texto.txt","r")
    print(arquivoLer.name)
    print(arquivoLer.read())
except Exception as e:
    print("Não foi possivel ler : ", e)
finally:
    arquivoLer.close()

# Trabalhando com Inputs e outputs IO
"""
try:
    arquivo = open("texto.txt","r+")

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

"""
def criarArquivoPessoa():
    try:
        arquivo=open("pessoas.txt","+r")
        arquivo.close()
        return True
    except Exception as e:
        print("Arquivo já foi criado!")
        return False



def addPessoas(nome,rg, ano_nasc):
    pessoa=f'{nome},{rg},{ano_nasc}'
    try:
        arquivo=open("pessoas.txt","a")
        arquivo.write(pessoa)
        arquivo.close()
    except Exception as e:
        print("Não foi possivel add essa pessoa, Erro:",e)


def listarPessoas():
    pessoas=list()
    try:
        arquivo=open("pessoas.txt","r")

        for linha in arquivo.readlines():
            lista=linha.split(",")

            pessoa={"nome":lista[0],"rg":lista[1],"ano_nasc":lista[2].replace("\n","") }
            pessoas.append(pessoa)

        return pessoas
    except Exception as e:
        print("Não foi possivel ler o arquivo pessoas, Erro:", e)
    finally:
        arquivo.close()
# Criando o meu Sistema


valor=criarArquivoPessoa()


while True:
    if valor:
        print("MENU".center(40,"#"))
        print("""
        Opção 1 -> Cadastrar
        Opção 2 -> Listar
        Opção 3 -> Buscar
        Opção 4 -> Sair do sistema
        """)

        pergunta = input("Qual Opção Deseja: ")

        if pergunta == "1":
            print("Cadastrar".center(40, "#"))
            nome=input("Nome: ")
            rg = input("RG: ")
            try:
                ano = int(input("Ano de nascimento: "))
                addPessoas(nome=nome,rg=rg,ano_nasc=ano)
            except Exception as e:
                print("Erro na digitação do ano de nascimento \nErro: ",e)
        elif pergunta == "2":
            for linha in listarPessoas():
                print(f"Nome: {linha['nome']}")
                print(f"RG:   {linha['rg']}")
                print(f"Ano:  {linha['ano_nasc']}")
                print("#"*20)

        elif pergunta=="3":
            buscarPessoa=input("Quem você deseja buscar: ")
            for linha in listarPessoas():
                if linha['nome'].upper()==buscarPessoa.upper():
                    print("Busca realizada")
                    print(f"Nome: {linha['nome']}")
                    print(f"RG:   {linha['rg']}")
                    print(f"Ano:  {linha['ano_nasc']}")
                    break
                else:
                    print("A pessoa pesquisada não esta no sistema!")


        elif pergunta == "4":
            break
        else:
            print("Valor digitado não é valido !")
    else:
        break
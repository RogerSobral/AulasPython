#Tratamento de Erros
try: # aqui ele vai tentar realizar, se não der vai pegar um erro
    divisao=2/0
    lista=[21,56,44]
    print(lista[2])

    print(divisao)
except ZeroDivisionError as variavel: # aqui ele vai testar se o erro é igual a Divisor por Zero
    print(f"Mensagem de Erro: {variavel}")
except IndexError as e: # Aqui vai testar se esta fora do Index o valor passado
    print(f"Outro Erro: {e}")
else: # caso não seja nenhum dos erros acima ele entra aqui
    print("Sei la")
finally:
    print("Aqui ele sempre entra")



for i in range(10):
    print(i)

#Exe 1
#Criar um sistema que vai cadastrar pessoas:
#Nome
#ano_nasc
#Você deve tratar os possiveis erros em salário caso seja digitado um valor errado

"""pessoas=list()
while True:
    try:
        nome=input("Digite o seu nome: ")
        ano=int(input("Digite a sua Idade"))
        pessoa={"nome": nome, "ano": ano}
        pessoas.append(pessoa)
    except Exception as e:
        print("O campo Idade deve ser numerico com 4 caracteres")

    resp=input("Deseja Continuar cadastrando Sim ou Não ").strip()[0].upper()
    if resp=="N":
        break


print(pessoas)"""
#Exe 2
#Você vai calcular a média de notas de um aluno,
#caso não seje digitado nada e a divisão seja por zero trate esse erro

print("Média".center(30,"#"))
valores=list()
while True:

    try:
        valores.append(float(input("Digite um valor :")))
        media=sum(valores)/len(valores)

    except ZeroDivisionError as e:
        print("O valor deve ser diferente de zero")

    except Exception as e:
        print("Erro", e)
    else:
        print("Não sei que erro é")

#Neste cado apresentado não dara certo a nossa operação de verificação pois para acontecer
#precisamos que a lista seja de tamanho zero, ai sim ela vai lançar o erro esperado
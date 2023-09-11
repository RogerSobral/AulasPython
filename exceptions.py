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
#idade
# Você deve tratar os possiveis erros em  salario caso seja digitado um valor errado

#Exe 2
# Você vai calcular a média de notas de um aluno,
# caso não seje digitado nada e a divisão seja por zero trate esse erro





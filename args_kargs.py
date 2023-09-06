# Função args kargs


# vou entrar com a possibilidade de varios parametros, e não quero limitar minha função com uma
#quantidade de parametros
def calculadora(*args):
    operador:str
    valor1:str
    valor2: str
    for index,parametro in enumerate(args):
        if index==0:
            operador=parametro
        elif index==1:
            valor1=parametro
        elif index==2:
            valor2=parametro
    print(f"Qual operador é = {operador}")
    print(f"Qual  é o valor 1 = {valor1}")
    print(f"Qual  é o valor 2 = {valor2}")

#index        0  1  2   3
calculadora("/",34,5, "seila")

print("#"*40)
def calculadora(*args):
    operador=args[0]
    valor1=args[1]
    valor2=args[2]
    print(f"Qual operador é = {operador}")
    print(f"Qual  é o valor 1 = {valor1}")
    print(f"Qual  é o valor 2 = {valor2}")

#Ele vai respeitar a ordem da entrada dos paramentros
calculadora("-",45,100)

print("#"*40)

def calculadora(*args):
    operador=args[0]
    valor1=args[1]
    valor2=args[2]
    print(f"Qual operador é = {operador}")
    print(f"Qual  é o valor 1 = {valor1}")
    print(f"Qual  é o valor 2 = {valor2}")
    print(f"{valor1}{operador}{valor2}={eval(valor1 + operador + valor2)}")# Estou concatenando as Strings e calculando
# A função eval()
# A função eval() em Python é uma ferramenta poderosa que permite
# Avaliar expressões matemáticas ou trechos de código Python presentes em forma de strings.
# Ela oferece uma maneira flexível de executar cálculos ou operações dinâmicas dentro do seu programa.
# No entanto, lembre-se de que a utilização imprudente da função `eval()` pode representar riscos de segurança,
# especialmente quando usado com entrada de usuário não confiável.


#index       0   1  2
calculadora("/","45","100")

"54+100"
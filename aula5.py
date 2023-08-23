# Aula sobre o "enquanto"
# Realiza o loop enquanto uma condição for atendida, sendo assim ela deve ser true

#i = 0
#while i < 10:# enquando i for menor que 10
 #   print("Valor de i: ", i)
 #   i += 1# o valor de i muda a cada rodada sendo somado a ele um valor


#while True:
    # strip()= aqui vou limpar os espaços em branco
    # [0] pegando somente a primeira letra
    # lower() transformando em letra minuscula
  # resposta=input("Deseja continuar  sim ou não").strip()[0].lower()

   # if resposta=="n": # entro na condição
     #   break  # posso quebrar meu loop


#print("Sai do sistema!")

# Criar um sistema que vai pegar o nome e a idade e só vai parar de pedir para cadastrar quando a idade for maior que 18 anos

#while True:

#    nome = input("Digite o seu nome: ")
#    idade = int(input("Digite a sua Idade: "))

#    if idade > 18:
#        break

#print("Acabou o sistema")


# Criar uma aplicação que pega o nome e a idade do aluno
# faça um loop que force o aluno a cadastrar 4 notas e fazer a média delas
# se a média for maior que 8 ele sai do loop e manda a mensagem "Você foi aprovado"

#nome = input("Digite o seu nome: ")
#idade = int(input("Digite a sua idade"))

#while True:
#    nota1 = float(input("Digite a sua nota 1: "))
#    nota2 = float(input("Digite a sua nota 2: "))
#    nota3 = float(input("Digite a sua nota 3: "))
#    nota4 = float(input("Digite a sua nota 4: "))
#    media = (nota1+nota2+nota3+nota4)/4
#    print(media)
#    if media >= 8:
#        break

#print("Sai do sistema")

# Criar uma aplicação que pega o nome e a idade do aluno => ok
# verificando se a idade é realmente é um int
# varificar se o nome é um str
# faça um loop que force ao aluno cadastrar 4 notas e verifique se
# as notas são do tipo float
# e se for float converte elas para esse tipo, depois faça a média delas
# se a média for maior que 8 ele sai do loop e manda a mensagem "Você foi aprovado"

#Trabalhando a validação Simples usando metodos do objeto String
#n="12"
#print(n.isdigit())

#idade=input("Digite a sua idade: ")

#valores Inteiros
#print(idade.isdigit())

#print(idade.isnumeric())

# verificar se é uma letra
#nome=input("digite o seu nome:")
#print(nome.isalpha())

#Alpha Numeric
#numero_Letra="23a45AÇ"
#print(numero_Letra.isalnum())


# para trocar o valor de um caracter eu posso
# usar o metodo replace([vai procurar o valor que deseja mudar],[qual valor que colocar no local])
#decimal="12.45"
#if str.isdigit(decimal.replace(".","")) or str.isdigit(decimal.replace(",","")) :

#    decimal=float(decimal.replace(",","."))
#    print("depois ",decimal)


# Resolução
nome = input("Digite o seu nome: ") # Alpha
idade = input("Digite a sua idade") # Digito

# se o nome for diferente de "alpha" e a idade diferente de "digital", vai dar uma resposta "false"
# sendo assim eu nego a resposta "false" e converto para verdadeira "True" colocando no començo o not
#Olha na planilha de And
while not (nome.isalpha() and idade.isdigit()):
    print("Você digitou ou o nome ou a idade errado")
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade")



# vou criar um loop que vai ficar verificando ate ele digitar as notas corretamente
while True:

    # bandeira
    b1 = False
    b2 = False
    b3 = False
    b4 = False

    #nota 1
    nota1 = input("Digite a sua nota 1: ") # pegando a primeira nota sendo ela uma String
    # 1) Testar se a nota1 tem um caracter do tipo  "." ou "," se tiver vamos remover usando o replace()
    # 2) vamos verificar se o que restou é um digito
    if str.isdigit(nota1.replace(".", "")) or str.isdigit(nota1.replace(",", "")):

        #3)se ela tiver "," eu retiro a vigula e coloco um ponto "." no lugar usando o replace
        #4) vou pegar o valor que é uma String e converter para um float
        nota1 = float(nota1.replace(",", "."))
        # se tudo deu certo eu converto minha bandeira para verdadeiro
        b1=True
    else:
        # se tudo deu certo eu converto minha bandeira para false
        print(" Voce Digitou a nota 1 errado ")
        b1=False

    print(nota1)
    # nota 2
    nota2 = input("Digite a sua nota 2: ")
    if str.isdigit(nota2.replace(".", "")) or str.isdigit(nota2.replace(",", "")):
        nota2 = float(nota2.replace(",", "."))

        b2 = True
    else:
        print(" Voce Digitou a nota 2 errado ")
        b2 = False

    # Nota 3
    nota3 = input("Digite a sua nota 3: ")
    if str.isdigit(nota3.replace(".", "")) or str.isdigit(nota3.replace(",", "")):
        nota3 = float(nota3.replace(",", "."))

        b3 = True
    else:
        print(" Voce Digitou a nota 3 errado ")
        b3 = False

    # Nota 4
    nota4 = input("Digite a sua nota 4: ")
    if str.isdigit(nota4.replace(".", "")) or str.isdigit(nota4.replace(",", "")):
        nota4 = float(nota4.replace(",", "."))
        b4 = True
    else:
        print(" Voce Digitou a nota 4 errado ")
        b4 = False



    if b1 and b2 and b3 and b4:
        media = (nota1+nota2+nota3+nota4)/4
        print(media)
        break



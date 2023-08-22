# Aula sobre o "enquanto"
# Realiza o loop enquanto uma condição for atendida, sendo assim ela deve ser true

i=0
while i<10: # enquando i for menor que 10
    print("Valor de i: ", i)
    i+=1 # o valor de i muda a cada rodada sendo somado a ele um valor


#while True:
    # strip()= aqui vou limpar os espaços em branco
    # [0] pegando somente a primeira letra
    # lower() transformando em letra minuscula
  # resposta=input("Deseja continuar  sim ou não").strip()[0].lower()

   # if resposta=="n": # entro na condição
     #   break  # posso quebrar meu loop


#print("Sai do sistema!")

# Criar um sistema que vai pegar o nome e a idade e só vai parar de pedir para cadastrar quando a idade for maior que 18 anos

while True:

    nome=input("Digite o seu nome: ")
    idade=int(input("Digite a sua Idade: "))

    if idade>18:
        break

print("Acabou o sistema")


#Criar uma aplicação que pega o nome e a idade do aluno
# faça um loop que force o aluno cadastrar 4 notas e fazer a média delas
# se a média for maior que 8 ele sai do loop e manda a mensagem "Você foi aprovado"
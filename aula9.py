# Set
# não aceita repetição
# Ele organiza os dados de uma maneira que faça ficar rapido a busca

lista=[1,2,3,4,2,3]
tupla=(1,2,3,4,2,3)
dicionario={"um":1,"dois":2,"tres":3}
conjunto={2,2,3,4,2,3,2,3,4,3}

print(f"Lista: {lista[0]}")
print(f"tupla: {tupla[0]}")
print(f'Dicionario: {dicionario["dois"]}')
print(f"conjunto: {conjunto}")

tamanho=len(conjunto)

conjunto.add(4)
if len(conjunto)==tamanho:
    print("Login ja existe!")


print("#"*30)



#Exercicio 1
# Criar um sistema que não permita repetição do login
lognhos={"admin","maria_2022"} # ele já começa com um tamanho 1
print("#"*25,"Tela de Login","#"*25)



while True:
    login=input("Cadastre o seu login: ")
    tamanho=len(lognhos)
    lognhos.add(login)
    if len(lognhos)!=tamanho:
        break
    else:
        print("Esse Login já existe: ")

print(f"Login:{lognhos}")

print("#"*30)

conjunto2={23,45,67,80,80}

for valor in conjunto2:
    print(valor)



#Exercicio 2
#Criar um sistema que salva login e senha,
#O Login não pode ser repetido
#A senha pode ser repetida
#O login deve estar associdado a senha

print("#"*30)
loguinhos = set()

usuarios = list()

while True:
    print("Cadastrando Usuario")
    login = input("Cadastre o seu login: ")
    senha = input("Cadastre sua senha: ")
    usuario = [login,senha] # para ele ser cadastrado na minha lista de usuarios vou primeiro validar

    #validando o login

    if len(usuarios)!=0:
        #verificando todos existentes

        for user in usuarios: # gerar uma variavel local (user)
            #estou pegando cada (usuario) que tem cadastrado na minha lista (Usuarios)
            loguinhos.add(user[0])
        tamanho=len(loguinhos) # verifico o tamanho do meu login

        #tentando add mais um login
        loguinhos.add(login)

        if len(loguinhos)==tamanho:
            print("Login já existe no sistema")
        else:
            usuarios.append(usuario)

    else:
        # vai entrar caso seja o primeiro usuario a ser cadastrado
        usuarios.append(usuario)

#Sair do loop
    resposta=input("Deseja continuar cadastrando : Sim ou Não").strip()[0].upper()

    if resposta=="N":
        print("Saindo do Sistema")
        break



# entre no sistema com os login cadastrados e as senhas lembrando que elas tem vinculo
# caso ele entre mande a mensagem "você esta dentro do sistema"

# -*- coding: latin-1 -*-

import datetime as dt
#Organizar meus dados por estrutura, onde essa estrutura representa um usuario
# FUN��O
# O nome da fun��o tem que ser em minusculo
# Uso dos () � obrigatorio, onde posso ou n�o entrar com paramentros
# tenho que usar: para come�ar uma estrutura
# tenho que colocar os codigos internos da estrutura com 4 espa�os
def visitante(nome_input,cpf_input,email_input,tel_input,data_cad_input, data_nas_input):
####
# Esse valor interno chamado de (nome) � uma variavel local
    nome=nome_input
    cpf=cpf_input
    email=email_input
    telefone=tel_input
    data_cadastro=data_cad_input
    data_nascimento=data_nas_input
    return [nome,cpf,email,telefone,data_cadastro,data_nascimento]


def porteiro(nome_input, senha_input,cpf_input):
# Eu devo entender a logica dos meus testes
    if nome_input.isalpha() and len(nome_input)>=2:
        nome = nome_input
        senha = senha_input
        cpf = cpf_input
        return [nome,senha,cpf]


def visita(rg_usuario,data,hora_entrada,hora_saida,motivo,seguranca):
    rg_user=rg_usuario
    data_visita=data
    h_entrada=hora_entrada
    h_saida=hora_saida
    motivo_visita=motivo
    responsavel=seguranca
    return [rg_user,data_visita,h_entrada,h_saida,motivo_visita,responsavel]

# Aqui � onde vamos simular nossas telas
visitantes=list()
while True:
    print("MENU".center(40,"#"))
    print("""
    Op��es 1-> Cadastrar Visitante
    Op��es 2-> Deletar Visitante
    Op��es 3-> Cadastrar Visita
    Op��es 4-> Cadastrar Seguran�a
    Op��es 5-> Listar visitas
    Op��es 6-> Listar Visitantes
    Op��es 7-> sair do sistema
    """)
    # vou pegar pelo teclado a op��o do usuario
    opcao=input("Digite a op��o desejada")
    if opcao.strip() in ["1","2","3","4","5","6"]:# ele esta verificando se o valor da op��o esta dentro da lista
        # vai come�ar rodar o meu sistema
        if opcao=="1":
            #Cadastro do visitante
            print("Cadastro de visitantes".center(30,"#"))

            #chamando fun��o para gerar um visitante
            lista=visitante(input("Nome:"),input("CPF:"),
                      input("Email"),input("Telefone:"),
                      dt.datetime.today(),input("Data de nascimento"))

            #estou add um visitante dentro da lista de visitantes
            visitantes.append(lista)

        elif opcao=="2":
            print("Deletar Visitante".center(40,"#")) # Titulo da tela
            cpf_deletar=input("Digite o valor do CPF de usuario a que deseja deletar: ") #peguei o cpf da pessoa

            for id,visitante in enumerate(visitantes):
                # Esse for esta fazendo duas coisas:
                # 1) percorrendo a lista Visitantes
                if visitante[1] == cpf_deletar:
                    visitantes.pop(id)


        elif opcao=="6":
            print(visitantes)
        # Op��o de sair do sistema

        if opcao == "7":
            break


    else: # se a pessoa digitar um valor que n�o existe no menu vai vir para ca
        print("n�o existe essa op�ao")








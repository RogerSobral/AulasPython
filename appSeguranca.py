# -*- coding: latin-1 -*-

#Organizar meus dados por estrutura, onde essa estrutura representa um usuario
#função
# O nome da função tem que ser em minusculo
# Uso dos () é obrigatorio, onde posso ou não entrar com paramentros
# tenho que usar : para começar uma estrutura
# tenho que colocar os codigos internos da estrutura com 4 espaços
def usuario(nome_input,cpf_input,email_input,tel_input,data_cad_input, data_nas_input):
####
# Esse valor interno chamado de (nome) é uma variavel local
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





porteiro("Sobral","1234","41.165.78")

# Criar as telas

lista=["Sobral","1234","41.165.78"]
print("Essa é a lista",lista[0])
print("Essa é a minha função",len(porteiro("Sobral","1234","41.165.78")) +10)
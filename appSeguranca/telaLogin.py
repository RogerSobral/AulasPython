#-*- coding: utf-8 -*-
import PySimpleGUI as sg
"""
#Pegar nomes de fontes
from tkinter import Tk, font
root = Tk()

font_tuple = font.families()
#Creates a Empty list to hold font names
FontList=[]
for font in font_tuple:
    FontList.append(font)

print(FontList)
"""

#Padroes
fonteTitulo=("Helvetica ",17,"bold")
fontTexto=("Helvetica",14)
cor_fundo="#2F6073"
def janelaLogin():

    layout=[
        [sg.Push(background_color="#2F6073"),sg.Image("img/fundoApp.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Image("img/dentro.png",background_color="#2F6073"),sg.Text("Login",size=7,background_color="#2F6073",text_color="#FFFFFF",font=fontTexto),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15", key="-LOGIN-")],
        [sg.Image("img/seguro.png",background_color="#2F6073"),sg.Text("Senha",size=7,background_color="#2F6073",text_color="#FFFFFF", font=" roboto 20"),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15",password_char="*",key="-SENHA-" )],
        [sg.Push(background_color="#2F6073"),sg.Button("Entrar",size=10,font="arial 15",pad=25,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#5AADBF",key="-BOTAO-"),sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"),sg.Text("Recuperar Senha!",background_color="#2F6073",text_color="#5AADBF", font=("Helvetica",12), enable_events=True, key="-CREATE_USER-"),sg.Push(background_color="#2F6073")]
    ]
    return sg.Window("Login",layout,background_color="#2F6073")


def janelaRecuperarSenha():
    layout=[
        [sg.Push(background_color="#2F6073"),sg.Image("img/mudarSenha.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Text("Entre com o seu CPF",size=18,text_color="#FFFFFF", font=("Helvetica",12), background_color="#2F6073"), sg.Input(key="-CPF-",size=20,background_color="#FFFFFF",font="Helvetica 15")],
        [sg.Button("Recuperar Senha",size=15,font="arial 15",pad=8,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#5AADBF"), sg.Text("",visible=False,background_color="#2F6073",text_color="#5AADBF")]
    ]
    return sg.Window("Recuperar Senha", layout,background_color="#2F6073")


def janelaCadastrarFuncionario():

    lista=["Gerente", "Supervisor", "Suporte", "Segurança"]

    layout = [
        [sg.Image("img/logoAPP.png",background_color="#2F6073"),sg.Push(background_color="#2F6073"),
         sg.Text("CADASTRAR FUNCIONARIO",background_color="#2F6073",font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Nome",background_color="#2F6073",font=fontTexto,size=10),
         sg.Input(size=(70,50),background_color="#FFFFFF", font=fontTexto),
         sg.Text("Nascimento",background_color="#2F6073",font=fontTexto),
         sg.Input(size=20,background_color="#FFFFFF",font=fontTexto),
         sg.Image("img/calendar.png",background_color="#2F6073")],

        [sg.Text("CPF",background_color="#2F6073",font=fontTexto,size=10),
         sg.Input(size=20,background_color="#FFFFFF",font=fontTexto),
         sg.Text("Cargo",background_color=cor_fundo,font=fontTexto,size=10),
         sg.Combo(lista,size=30, default_value="Escolha o Cargos",font=fontTexto,button_arrow_color="#FFFFFF",button_background_color="#2F6073"),
         sg.Text("Cadastrar Contato",size=15, font=fontTexto,background_color=cor_fundo),sg.Image("img/contato.png",background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Senha",size=10,background_color=cor_fundo, font=fontTexto),
         sg.Input(font=fontTexto, size=15,password_char='*'),
         sg.Text("Nivel", font=fontTexto,background_color=cor_fundo),
         sg.Radio("ADM","radio1", font=fontTexto,  background_color=cor_fundo),
         sg.Radio("COMUM","radio1",default=True, font=fontTexto, background_color=cor_fundo), sg.Push(background_color=cor_fundo),sg.Button("Cadastrar",font=fontTexto, size=20), sg.Push(background_color=cor_fundo)],

        [sg.HSep()],

        [
            [sg.Text("Observações de uso: \nCadastrar o nascimento use o calendario :\nA senha deve ter 6 caracteres:\nPara cadastrar o contato clique no icone:",
            font=fontTexto,background_color=cor_fundo)]
        ,sg.Push(background_color=cor_fundo),sg.Image("img/fundoCadastro.png",background_color=cor_fundo),sg.Push(background_color=cor_fundo)],

        [sg.HSep()],
        [sg.Push(background_color=cor_fundo), sg.Text("By: Rogério Sobral Ribeiro",background_color=cor_fundo),sg.Push(background_color=cor_fundo)]

    ]

    return sg.Window("Cadastro",layout,resizable=True,background_color="#2F6073")


def janelaContato():
    layout=[
        [sg.Image("img/logoAPP.png", background_color="#2F6073"), sg.Push(background_color="#2F6073"),
         sg.Text("Contato", background_color="#2F6073", font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Email", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Telefone", background_color="#2F6073", font=fontTexto,size=10),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto)],

        [sg.HSep()],

#Rua | Numero | CEP
        [sg.Text("Rua", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Numero", background_color="#2F6073", font=fontTexto,size=10),
         sg.Input(size=10, background_color="#FFFFFF", font=fontTexto),
         sg.Text("CEP", background_color="#2F6073", font=fontTexto,size=5),
         sg.Input(size=16, background_color="#FFFFFF", font=fontTexto),
         sg.Button("Buscar",font=fontTexto)
         ],

# Bairro | Cidade | SP
        [sg.Text("Bairro", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Cidade", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=25, background_color="#FFFFFF", font=fontTexto),
         sg.Text("Estado", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=10, background_color="#FFFFFF", font=fontTexto)
         ],

    #Button Cadastrar e o Buscar
        [sg.Push(background_color=cor_fundo),sg.Button("Voltar", font=fontTexto, size=18),sg.Button("Cadastrar", font=fontTexto, size=18), sg.Push(background_color=cor_fundo)]

    ]

    return sg.Window("Contato",layout,background_color="#2F6073")



def janelaListarFuncionario():

    lista=["Gerente", "Supervisor", "Suporte", "Segurança"]

    top_tabela=["Nome", "Nascimento","CPF","Cargo","Telefone","Nivel"]
    valores=[[]]

    layout = [
        [sg.Image("img/logoAPP.png",background_color="#2F6073"),sg.Push(background_color="#2F6073"),
         sg.Text("LISTAR FUNCIONARIO",background_color="#2F6073",font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Nome",background_color="#2F6073",font=fontTexto,size=10),
         sg.Input(size=(70,50),background_color="#FFFFFF", font=fontTexto),
         sg.Text("Nascimento",background_color="#2F6073",font=fontTexto),
         sg.Input(size=20,background_color="#FFFFFF",font=fontTexto),
         sg.Image("img/calendar.png",background_color="#2F6073")],

        [sg.Text("CPF",background_color="#2F6073",font=fontTexto,size=10),
         sg.Input(size=20,background_color="#FFFFFF",font=fontTexto),
         sg.Text("Cargo",background_color=cor_fundo,font=fontTexto,size=10),
         sg.Combo(lista,size=30, default_value="Escolha o Cargos",font=fontTexto,button_arrow_color="#FFFFFF",button_background_color="#2F6073"),
         sg.Text("Cadastrar Contato",size=15, font=fontTexto,background_color=cor_fundo),sg.Image("img/contato.png",background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Senha",size=10,background_color=cor_fundo, font=fontTexto),
         sg.Input(font=fontTexto, size=15,password_char='*'),
         sg.Text("Nivel", font=fontTexto,background_color=cor_fundo),
         sg.Radio("ADM","radio1", font=fontTexto,  background_color=cor_fundo),
         sg.Radio("COMUM","radio1",default=True, font=fontTexto, background_color=cor_fundo), sg.Push(background_color=cor_fundo),sg.Button("Cadastrar",font=fontTexto, size=20), sg.Push(background_color=cor_fundo)],

        [sg.HSep()],

       #Vai entrar uma tabela mostrando os usuarioas

        [sg.Table(headings=top_tabela, values=valores)],

        [sg.HSep()],
        [sg.Push(background_color=cor_fundo), sg.Text("By: Rogério Sobral Ribeiro",background_color=cor_fundo),sg.Push(background_color=cor_fundo)]

    ]

    return sg.Window("Listar",layout,resizable=True,background_color="#2F6073")



janelaListarFuncionario().read()

# destruido o arquivo tk usado para pegar as fontes
#root.destroy()
#-*- coding: utf-8 -*-
import PySimpleGUI as sg

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
        [sg.Push(background_color=cor_fundo),sg.Image("img/fundoCadastro.png",background_color=cor_fundo),sg.Push(background_color=cor_fundo)],

        [sg.HSep()],
        [sg.Push(background_color=cor_fundo), sg.Text("By: Rogério Sobral Ribeiro",background_color=cor_fundo),sg.Push(background_color=cor_fundo)]



    ]

    return sg.Window("Cadastro",layout,resizable=True,background_color="#2F6073")



janelaCadastrarFuncionario().read()

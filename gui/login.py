#-*- coding: latin-1 -*-
import PySimpleGUI as sg

layout=[

    [sg.Push(background_color="#2F6073"),sg.Image("fundo_tratado_novo.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
    [sg.Image("dentro.png",background_color="#2F6073"),sg.Text("Login",size=7,background_color="#2F6073",text_color="#E8BF58",font=" roboto 20" ),sg.Input(size=20,background_color="#2F6073",font=" roboto 15", key="-LOGIN-")],
    [sg.Image("seguro.png",background_color="#2F6073"),sg.Text("Senha",size=7,background_color="#2F6073",text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20,background_color="#2F6073",font=" roboto 15",password_char="*",key="-SENHA-" )],
    [sg.Push(background_color="#2F6073"),sg.Button("Entrar",size=10,font="arial 15",pad=25,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#E8BF58",key="-BOTAO-"),sg.Push(background_color="#2F6073")],
    [sg.Push(background_color="#2F6073"),sg.Text("Recuperar Senha!",background_color="#2F6073",text_color="#E8BF58", font=("Helvetica",12), enable_events=True, key="-CREATE_USER-"),sg.Push(background_color="#2F6073")]

]

window = sg.Window("Tela Login",layout,background_color="#2F6073",finalize=True)

while True:
    events,values = window.read()

    if events == sg.WIN_CLOSED:
        break

    elif events == "-BOTAO-":
        nome= values["-LOGIN-"]
        senha= values["-SENHA-"]
        if nome in ["carlos", "pedro", "maria"] and senha in ["123","222","12345"]:
            print("Você esta dentro do sistema")
    if events=="-CREATE_USER-":
        print("Rodou")
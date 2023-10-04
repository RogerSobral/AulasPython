# -*- coding: utf-8 -*-
import PySimpleGUI as sg
#Tela
# CONTROLE DE CONTA


fonte_texto=("roboto",12)
fonte_titulo=("roboto",14,"bold")

def janelaMenu():
    layout=[
        [sg.Push(background_color="white"), sg.Text("Menu",background_color="white", font=fonte_titulo),sg.Push(background_color="white")],
        [sg.Button(key="-MENU_CADASTRAR-",button_text= "Cadastrar Cliente",font=fonte_titulo)],
        [sg.Button(key="-DEPOSITO-", button_text="Deposito", font=fonte_titulo)],
        [sg.Button(key="-DEPOSITO-", button_text="Saque", font=fonte_titulo)],
    ]

    return sg.Window(title="Menu",layout=layout,finalize=True)




def janelaCadastrarCliente():
    layout=[
        [sg.Push(background_color="white"), sg.Text("Cadastro",background_color="white", font=fonte_titulo),
         sg.Push(background_color="white")],

        [sg.Text("Nome",font=fonte_texto, size=10),sg.Input(key="-NOME-")],

        [sg.Text("Data Nascimento", font=fonte_texto, size=10),
         sg.Image("/img/calendar.gif",background_color="white"),
         sg.Input(font=fonte_texto, size=10)],
        [sg.Button(key="-MENU_CADASTRAR-",button_text="Cadastrar",font=fonte_titulo)]
    ]

    return sg.Window(title="Cadastro",layout=layout,finalize=True)









telaMenu,telaCadastro = janelaMenu(),None


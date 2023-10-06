# -*- coding: utf-8 -*-
import PySimpleGUI as sg
#Tela
# CONTROLE DE CONTA
from revisao import bd_conta

fonte_texto=("roboto",12)
fonte_titulo=("roboto",14,"bold")

def janelaMenu():
    layout=[
        [sg.Push(), sg.Text("Menu", font=fonte_titulo),sg.Push()],
        [sg.Button(key="-MENU_CADASTRAR_CLIENTE-",button_text= "Cadastrar Cliente",font=fonte_titulo, size=20)],
        [sg.Button(key="-CONTROLE_CAIXA-", button_text="Operações", font=fonte_titulo,size=20)],

    ]

    return sg.Window(title="Menu",layout=layout,finalize=True)




def janelaCadastrarCliente():

    tipo=["Corrente", "Poupança"]
    layout=[
        [sg.Push(), sg.Text("Dados Pessoais", font=fonte_titulo),
         sg.Push()],
        [sg.Text("Nome",font=fonte_texto, size=15),sg.Input(key="-NOME-")],
        [sg.Text("Data Nascimento", font=fonte_texto, size=15),
         sg.Image("img/calendar.gif", enable_events=True, key="-DATA_NASC-"),
         sg.Input(font=fonte_texto, size=10, key="-CALENDAR-")],
        [sg.HSep(color="white")],
        [sg.Push(), sg.Text("Dados da Conta", font=fonte_titulo),
         sg.Push()],
        [sg.Text("Tipo de conta",font=fonte_texto, size=15), sg.Combo(values=tipo,default_value="Conta", key="-TIPOS-",font=fonte_texto)],
        [sg.Text("Valor R$",font=fonte_texto, size=15), sg.Input(key="-VALOR-", size=10)],

        [sg.Button(key="-CADASTRAR-",button_text="Cadastrar",font=fonte_titulo,expand_x=True)]
    ]

    return sg.Window(title="Cadastro",layout=layout,finalize=True)


def janelaFluxoCaixa():

    layout=[
        #lINHA TITULO
        [sg.Push(background_color="white"), sg.Text("Conta", background_color="white", font=fonte_titulo),
         sg.Push(background_color="white")],
        #LINHA CONTA
        [sg.Text("Conta",background_color="white", font=fonte_titulo),
         sg.Input(key="-ID_CONTA-"), sg.Button("Conectar", key="-CONECTAR-")],
        #LINHA DEPOSITAR
        [sg.Text("Depositar",background_color="white", font=fonte_titulo),
         sg.Input(key="-DEPOSITAR-"), sg.Button("Depositar", key="-BTN_DEPOSITAR-")],
        # LINHA SACAR
        [sg.Text("Sacar", background_color="white", font=fonte_titulo),
         sg.Input(key="-SACAR-"), sg.Button("Sacar", key="-BTN_SACAR-")],
         #separador
        [sg.HSep(color="black")],
        [sg.Text("Saldo", background_color="white", font=fonte_titulo),
         sg.Input(key="-SALDO-",readonly=True)]
    ]







telaMenu,telaCadastroConta, telaFluxoCaixa = janelaMenu(),None, None

while True:
    window, events, values= sg.read_all_windows()

    if window == telaMenu and events == sg.WINDOW_CLOSED:
        break

    if window == telaMenu and events == "-MENU_CADASTRAR_CLIENTE-":
        telaCadastroConta = janelaCadastrarCliente()
        telaMenu.hide()

    if window == telaMenu and events == "-CONTROLE_CAIXA-":
        telaFluxoCaixa=janelaFluxoCaixa()
        telaMenu.hide()

    if window == telaCadastroConta and events == sg.WINDOW_CLOSED:
        telaMenu.un_hide()
        telaCadastroConta.hide()

    if window == telaCadastroConta and events == "-DATA_NASC-":
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                 'Outubro', 'Novembro', 'Dezembro']
        dias = ['Dom', ' Seg', 'Ter', 'Quar', 'Quin', 'Sex', 'Sáb']

        mes, dia, ano = sg.popup_get_date(month_names=meses, begin_at_sunday_plus=1, day_abbreviations=dias,
                                          close_when_chosen=True)

        telaCadastroConta["-CALENDAR-"].update(value=f"{dia}/{mes}/{ano}")

    if window == telaCadastroConta and events == "-CADASTRAR-":
        nome=values["-NOME-"]
        data_nasc=values["-CALENDAR-"]
        valor=values["-VALOR-"]
        tipo_conta=values["-TIPOS-"]
        bd_conta.addCliente(nome,data_nasc)



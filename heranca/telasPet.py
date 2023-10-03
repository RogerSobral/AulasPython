# -*- coding: utf-8 -*-
import PySimpleGUI as sg
# Criar 3 telas de cadastro de animais
# tela cadastrar o dono
# cadastrar o animal
# menu

# nome do animal
# Nome do dono *
# idade do animal
# raça do animal
# espécies do animal
# telefone do dono *
# cor do animal
# porte do animal
# CPF *

# Tela Menu

def telaMenu():
    layout=[
        [sg.Push(),sg.Text("Menu", font=('arial', 15,"bold")), sg.Push()],
        [sg.Button("Cadastrar Dono", size=15)],
        [sg.Button("Cadastrar PET",size=15)],
    ]

    return sg.Window("Menu",layout,finalize=True)


#tela Dono
def telaCadastrarDono():
    layout = [
        [sg.Push(), sg.Text("Cadastrar Dono"), sg.Push()],
        [sg.Text("Nome", size=10), sg.Input(key="-NOME-")],
        [sg.Text("Telefone", size=10), sg.Input(key="-TELEFONE-")],
        [sg.Text("CPF", size=10), sg.Input(key="-CPF-")],
        [sg.Push(), sg.Button("Cadastrar",size=15), sg.Push()]
    ]

    return sg.Window("Cadastro Dono", layout, finalize=True)

#tela Cadastrar Pet
def telaCadastrarPET():
    layout = [
        [sg.Push(), sg.Text("Cadastrar PET"), sg.Push()],
        [sg.Text("Nome", size=10), sg.Input(key="-NOME-")],
        [sg.Text("Idade", size=10), sg.Input(key="-IDADE-")],
        [sg.Text("Raça", size=10), sg.Input(key="-RACA-")],
        [sg.Text("Espécies",size=10),sg.Input(key="-ESPECIE-")],
        [sg.Text("Cor", size=10), sg.Input(key="-COR-")],
        [sg.Text("Porte", size=10), sg.Input(key="-PORTE-")],
        [sg.Push(), sg.Button("Cadastrar",size=15), sg.Push()]
    ]

    return sg.Window("Cadastro Dono", layout, finalize=True)

janelaMenu, janelaCadastrarDono, janelaCadastrarPet= telaMenu(), None, None

while True:

    window, events,values=sg.read_all_windows()
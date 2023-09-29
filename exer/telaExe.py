#-*- coding: utf-8 -*-
import PySimpleGUI as sg

# Criar uma tela de cadastro, nesta tela vai ter uma tabela
# Deve pegar os dados da tela salvar em um txt
# Depois ler esse txt e mostrar os valores na tabela
def lerTxt():
    with open("dados.txt", "r+") as file:
        lista = list()

        for linha in file:
            arquivo = linha.split(" ")
            lista.append(arquivo)

        lista2 = list()

        for linha in lista:
            pessoa = list()
            for index, elemento in enumerate(linha):

                if index == 0:
                    elemento = elemento
                    pessoa.append(elemento)
                else:
                    elemento = elemento.replace("\n", "")
                    pessoa.append(elemento)
            lista2.append(pessoa)
    return lista2

def tela():
    cabecalho=["nome", "idade"]

    layout=[
        [sg.Text("Nome"), sg.Input(key="-NOME-")],
        [sg.Text("idade"), sg.Input(key="-IDADE-")],
        [sg.Button("Cadastrar", key="-CADASTRAR-")],
        [sg.HSep()],
        [sg.Table(headings=cabecalho, values=lerTxt(), key="-TABELA-")]
    ]

    return sg.Window("Tela", layout,finalize=True)


janela=tela()

while True:
    events,values=janela.read()

    if events == "-CADASTRAR-":

        nome=values["-NOME-"]
        idade=values["-IDADE-"]
        #usando para salvar os dados
        with open("dados.txt", "a+") as file:
            file.write(f"{nome} {idade}\n")
            sg.Popup("Cadastrado com sucesso!")
            janela["-NOME-"].update(value="")
            janela["-IDADE-"].update(value="")

        #ler os dados


        janela["-TABELA-"].update(values=lerTxt())





    if events == sg.WIN_CLOSED:
        break



janela.close()
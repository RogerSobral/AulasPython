#-*- coding: utf-8 -*-
import PySimpleGUI as sg
import os

def deletarTxt():
    path = r"C:\Users\rogerio.sribeiro\PycharmProjects\AulasPython\exer"
    dir = os.listdir(path)
    for file in dir:
        if file == "arquivo.txt":
            os.remove(file)


# Criar uma tela de cadastro, nesta tela vai ter uma tabela
# Deve pegar os dados da tela salvar em um txt
# Depois ler esse txt e mostrar os valores na tabela
def lerTxt():
    with open("dados.txt", "r+") as file:
        lista = list()

        for linha in file:
            linha.replace("\n","")
            arquivo = linha.split(" ")
            lista.append(arquivo)
        return lista


#Terminar a logica de deletar
def deletarLinha(id_linha):
    lista=lerTxt()
    listaNova=list()
    deletarTxt()
    for index,pessoa in enumerate(lista):
        if index != id_linha:
            with open("dados.txt", "a+") as file:

                p=f"{pessoa[0]} {pessoa[1]}\n"

                file.write(p)












def tela():
    cabecalho=["Nome", "Idade"]

    layout=[
        [sg.Push(background_color="white"),sg.Image("img/fundoCadastro.png",background_color="white"), sg.Push(background_color="white")],
        [sg.Text("Nome", size=10,background_color="white", text_color="#4970BF",font=("arial",13,"bold")), sg.Input(key="-NOME-")],
        [sg.Text("Idade",size=10,background_color="white",text_color="#4970BF", font=("arial",13,"bold")), sg.Input(key="-IDADE-")],
        [sg.Button("Cadastrar", key="-CADASTRAR-", button_color="#4970BF",size=(53,1),font=("arial",10,"bold"), mouseover_colors=( "white","#4970BF" ))],
        [sg.Button("Deletar", key="-DELETAR-", button_color="#4970BF", size=(53, 1), font=("arial", 10, "bold"),
                   mouseover_colors=("white", "#4970BF"))],

        [sg.HSep()],
        [sg.Table(headings=cabecalho, values=lerTxt(),
                  key="-TABELA-",auto_size_columns=False,def_col_width=23,header_background_color="#4970BF",
                  header_text_color="white", header_font=("arial",10,"bold"),sbar_background_color="#4970BF",sbar_trough_color="#5E83F2",
                  sbar_frame_color="#B6D0F2",background_color="#B6D0F2",text_color="#4970BF", font=("arial",10,"bold"),justification='lefth'
                  )],
        [sg.Push(background_color="white"), sg.Text("By Rogério Sobral",background_color="white", text_color="#4970BF",font=("arial",15)),sg.Push(background_color="white")]

    ]

    return sg.Window("Tela", layout,finalize=True, background_color="white")

if __name__ == '__main__':

    janela=tela()

    while True:
        events,values=janela.read()

        if events == "-CADASTRAR-":

            nome=values["-NOME-"]
            idade=values["-IDADE-"]

            if len(nome)>=1 and len(idade)>=1 and idade.isdigit():
                #usando para salvar os dados
                with open("dados.txt", "a+") as file:
                    file.write(f"{nome} {idade}\n")
                    sg.Popup("Cadastrado com sucesso!")
                    janela["-NOME-"].update(value="")
                    janela["-IDADE-"].update(value="")
            else:
                sg.Popup("Não foi possível cadastrar, entre com valores!")
            #ler os dados


            janela["-TABELA-"].update(values=lerTxt())

        if events=="-DELETAR-":
            value_id=values["-TABELA-"][0]
            deletarLinha(value_id)
            janela["-TABELA-"].update(values=lerTxt())




        if events == sg.WIN_CLOSED:
            break



    janela.close()
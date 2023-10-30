# -*- coding:utf-8 -*-
from PySimpleGUI import *
import crud.bdDespesas as bd

def telaDespesa():

    lista_despesas=bd.listarDespesas() # é o meu Select, vai retornar todos os elementos no banco de dados
    layout=[
        [Push(),Text("Cadastro de Despesa"),Push()],

        [Text("Descrição", size=10), Input(key="-DESCRICAO-")],

        [Text("Valor", size=10), Input(key="-VALOR-"),Image("img/calendar.png",key='-CALENDAR-',enable_events=True),
         Input(key="-INPUT_CALENDAR-", size=10)],

        [Button("Cadastrar",key='-CADASTRAR-'),Button("Deletar", key="-DELETAR-"),
         Button("Atualizar", key='-ATUALIZAR-'),Button("Pegar",key="-PEGAR-"),
         Button("Buscar", key="-BUSCAR-"), Input(key="-DESCRICAO_BUSCAR-")],
        [HSep()],
        [Table(values=lista_despesas,headings=["ID","Descrição","Valor","Data"], key="-TABLE-", auto_size_columns=False, def_col_width=27, font=("Helvetica",10))]
    ]

    return Window("Cadastrar Despesas",layout=layout,finalize=True)

janelaDespesas=telaDespesa()

while True:
    window, events, values = read_all_windows()

    if window==janelaDespesas and events ==WINDOW_CLOSED:
        break
    if window == janelaDespesas and events == "-CALENDAR-":
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                 'Outubro', 'Novembro', 'Dezembro']
        dias = ['Dom', ' Seg', 'Ter', 'Quar', 'Quin', 'Sex', 'Sáb']

        mes, dia, ano = popup_get_date(month_names=meses, begin_at_sunday_plus=1, day_abbreviations=dias,
                                          close_when_chosen=True)
        janelaDespesas["-INPUT_CALENDAR-"].update(value=f"{dia}/{mes}/{ano}")

    if window == janelaDespesas and events =='-CADASTRAR-':
        descricao=values["-DESCRICAO-"]
        valor=values["-VALOR-"]
        data=values["-INPUT_CALENDAR-"]
        bd.addDespesa(descricao,float(valor),data)
        Popup("Cadastrado com Sucesso!")
        janelaDespesas["-TABLE-"].update(values=bd.listarDespesas())
        janelaDespesas["-DESCRICAO-"].update(value="")
        janelaDespesas["-VALOR-"].update(value="")
        janelaDespesas["-INPUT_CALENDAR-"].update(value="")

    if window == janelaDespesas and events == "-PEGAR-":
        lista=janelaDespesas['-TABLE-'].get() # toda a tabela
        index = values["-TABLE-"][0]
        valor = lista[index]
        id_despesa=lista[index][0]
        janelaDespesas["-DESCRICAO-"].update(value=valor[1])
        janelaDespesas["-VALOR-"].update(value=valor[2])
        janelaDespesas["-INPUT_CALENDAR-"].update(value=valor[3])

        print(valor)
    if window == janelaDespesas and events == "-ATUALIZAR-":
        descricao = values["-DESCRICAO-"]
        valor = values["-VALOR-"]
        data = values["-INPUT_CALENDAR-"]

        bd.atualizar(descricao,data,float(valor),int(id_despesa))
        Popup("Atualizado com Sucesso !")
        janelaDespesas["-TABLE-"].update(values=bd.listarDespesas())

    if window == janelaDespesas and events == "-DELETAR-":
        lista = janelaDespesas['-TABLE-'].get()  # toda a tabela
        index = values["-TABLE-"][0]

        id = lista[index][0]
        bd.deletarDespesa(id)
        Popup("Deletado com Sucesso!")
        janelaDespesas["-TABLE-"].update(values=bd.listarDespesas())

    if window == janelaDespesas and events == "-BUSCAR-":
        valor=values["-DESCRICAO_BUSCAR-"]

        janelaDespesas["-TABLE-"].update(values=bd.buscar(valor))
# -*- coding:utf-8 -*-
import flet as ft

# Vamos criar um contador que vai add valores através de Buttons
def main(page:ft.Page):
    page.title="Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    titulo=ft.Text("Contador")
    # Criar as Funções
    def minus_click(e):
        # Eu estou modificando esse valor
        #1 - primeiro  pego o valor
        #2- converto o valor para INT
        #3 - faço a subtração
        #4- converter ele novamente para STR
        #5- jogo ele para o valor do meu TextField

        txt_number.value = str(int(txt_number.value) - 1)
        page.update()


    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()


    linha1=ft.Row(controls=[titulo], alignment=ft.MainAxisAlignment.CENTER)

    menos=ft.IconButton(ft.icons.REMOVE,on_click=minus_click)
    mais= ft.IconButton(ft.icons.ADD, on_click=plus_click)

    # Row é um elemento de linhas
    linha2=ft.Row(controls=[menos,txt_number,mais],alignment=ft.MainAxisAlignment.CENTER)

    coluna=ft.Column(controls=[linha1,linha2])

    page.add(coluna)

    page.update()

ft.app(target=main)

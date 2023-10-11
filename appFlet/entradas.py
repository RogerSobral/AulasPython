#-*- coding: utf-8 -*-
import flet as ft
import  sys


def main(page: ft.Page):
    page.title="Entradas de Dados"
    titulo=ft.Text("Cadastro de Matérias")
    titulo.color="#7F0DDE"
    titulo.size= 20
    page.window_center()
    page.window_min_width = 450
    page.update()


    linhaMateria = ft.Row()
    def addMateria(e):

        if not materia_input.value:
            materia_input.error_text="Digite uma Matéria"
            materia_input.focus()

        else:
            linhaMateria.controls=[ft.Checkbox(),ft.Text(materia_input.value),
                               ft.IconButton(ft.icons.REMOVE), ft.IconButton(ft.icons.UPDATE)]

            linhaMateria.alignment=ft.MainAxisAlignment.CENTER
            page.add(linhaMateria)
            materia_input.value=""
            materia_input.error_text =""
            materia_input.focus()


        materia_input.update()




    materia_input=ft.TextField(label="Digite a matéria desejada!")



    btn_add= ft.IconButton(ft.icons.ADD, on_click=addMateria)
    linha1=ft.Row([titulo],alignment = ft.MainAxisAlignment.CENTER)
    linha2=ft.Row(controls=[materia_input,btn_add],alignment = ft.MainAxisAlignment.CENTER)

    page.add(
        ft.Column(controls=[linha1,linha2],alignment = ft.MainAxisAlignment.CENTER
        )
    )

    page.update()


sys.exit(ft.app(target=main))
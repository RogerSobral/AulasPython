#-*- coding: utf-8 -*-
import flet as ft
import  sys

def main(page: ft.Page):
    page.title="Entradas de Dados"
    titulo=ft.Text("Drop Down")

    def teclado(e:ft.KeyboardEvent): # pegando o evento do teclado
        if e.key=="Enter":
            modificarCor()



    def modificarCor(*e):
        output_text.value = f"O valor do Drop é:  {color_dropdown.value}"
        page.update()

    output_text=ft.Text()
    btn= ft.ElevatedButton("Modificar", on_click=modificarCor)
    color_dropdown=ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Azul"),
        ],
    )

    page.add(
        ft.Column(controls=[titulo]),
        ft.Column(controls=[btn,color_dropdown]),
        ft.Column(controls=[output_text])
    )
    page.on_keyboard_event=teclado
    page.update()


sys.exit(ft.app(target=main))


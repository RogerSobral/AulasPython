# -*- coding: utf-8 -*-

import flet as ft

def main(page: ft.Page):
    page.title="Contador"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.window_min_width=600
    page.window_min_height=400
    page.window_max_width=600
    page.window_max_height=600
    page.update()



    txt_number= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100 )
    def plus_click(e):
        txt_number.value=  str(int(txt_number.value)+1)
        page.update()

    def minus_click(e):
        txt_number.value=  str(int(txt_number.value)-1)
        page.update()

# Page Add é um controler de widgets
    page.add(
        # Row tambem é um controle de widgets, mas ajuda a organizalas por linhas
        ft.Row([ft.Text("Contagem", size=20)],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
        [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
        txt_number,
        ft.IconButton(ft.icons.ADD,on_click=plus_click)],
        alignment = ft.MainAxisAlignment.CENTER

        )
    )




ft.app(target=main)
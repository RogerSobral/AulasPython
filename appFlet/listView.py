#-*- coding: utf-8 -*-
import flet as ft

def main(page: ft.Page):
    # spacing é o espaço que sera gerando entre os itens
    lista= ft.ListView(spacing=2, expand=True)
 
    # vamos criar varios itens
    for i in range(100):
        lista.controls.append(
            ft.Text(f"Estamos na lina {i}")
        )

    page.add(lista)


ft.app(target=main, view=ft.WEB_BROWSER)
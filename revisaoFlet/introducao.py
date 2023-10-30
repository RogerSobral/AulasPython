# -*- coding:utf-8 -*-
import flet as ft

# anotações
def main(page:ft.Page):
    page.title="Pagina Introdução"
    page.bgcolor="#F2F2F2"
    texto=ft.Text("Essa é a minha primeira pagina")
    btn=ft.ElevatedButton("Sei la")
    page.update()
    page.add(texto)
    page.add(btn)





ft.app(target=main)
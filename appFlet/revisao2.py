# -*- coding: utf-8 -*-
#Nesta Aplicação estamos criando um contador automático

import time

import flet as ft
texto=ft.Text()
def main(page: ft.Page):

    page.title="Testando os Widgets"
    page.add(texto)
    for i in range(10):
        texto.value=f"Foi modificado {i+1}"
        page.update()
        time.sleep(1)



ft.app(target=main)
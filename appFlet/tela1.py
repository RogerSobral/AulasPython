# -*- coding: utf-8 -*-
import flet as ft

def main(page:ft.Page ):
    #Configurações da Pagina
    page.title = "Primeiro Programa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ola= ft.Text(value="Ola Mundo !", size=30, text_align=ft.TextAlign.CENTER)
    page.controls.append(ola) # add um elemento
    page.update() # atualizar a pagina




ft.app(target=main)
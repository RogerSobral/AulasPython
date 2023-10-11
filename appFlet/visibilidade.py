#-*- coding: utf-8 -*-
import flet as ft

def main(page: ft.Page):

    page.title = "Teste"

    btn=ft.ElevatedButton("Botão")
    first_name=ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,last_name
    ])
    c.visible=False
    def disabledTrue(e):
        c.visible = True # tornar visivel
        c.disabled=True # habilitar
        page.update()


    def desabledFalse(e):
        c.visible = False # tornar visivel um elemento ou seus filhos
        c.disabled=False # habilitar para uso  o elemento ou seus filhos
        page.update()

    texto=ft.Text("Testando um Texto")
    btn.on_click=disabledTrue
    btn.on_long_press=desabledFalse
    page.add(btn,c, texto)
    page.update()



ft.app(target=main)

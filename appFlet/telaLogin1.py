# -*- coding: utf-8 -*-

import flet as ft

def main(page: ft.Page):
    page.title="Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width=600
    page.window_min_height=400
    page.window_max_width=650
    page.window_max_height=600


    titulo=ft.Text("Login")
    nome_icon=ft.Icon(ft.icons.BOY)
    senha_icon=ft.Icon(ft.icons.PASSWORD)
    nome_input=ft.TextField(hint_text="Digite o seu nome",label="nome")
    passWord_input=ft.TextField(hint_text=" Digite sua senha", label="Senha")
    btn_entrar=ft.OutlinedButton("Entrar")

    page.add(
        ft.Row(controls=[titulo], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[nome_icon,nome_input], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[senha_icon, passWord_input],  alignment = ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[btn_entrar], alignment = ft.MainAxisAlignment.CENTER)
    )

    page.update()


ft.app(target=main)
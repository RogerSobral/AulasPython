# -*- coding:utf-8 -*-
import flet as ft

# Vamos criar um Login
def main(page:ft.Page):
    page.title="Login"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    def eventoMensagem(e):
        texto=f"Nome: {input_name.value} Senha: {input_pass.value}"
        mensagem.value=texto
        page.update()

    # Elementos
    title=ft.Text("Login")
    icon_user=ft.Icon(ft.icons.BOY)
    icon_password=ft.Icon(ft.icons.PASSWORD)
    input_name= ft.TextField(label="Nome")
    input_pass= ft.TextField(label="Senha")
    btn_enter= ft.ElevatedButton(text="Entrar",on_click=eventoMensagem)
    mensagem=ft.Text(value="")


    line1=ft.Row(controls=[title],alignment=ft.MainAxisAlignment.CENTER)
    line2=ft.Row(controls=[icon_user,input_name],alignment=ft.MainAxisAlignment.CENTER)
    line3=ft.Row(controls=[icon_password,input_pass],alignment=ft.MainAxisAlignment.CENTER)
    line4=ft.Row(controls=[btn_enter],alignment=ft.MainAxisAlignment.CENTER)
    line5=ft.Row(controls=[mensagem],alignment=ft.MainAxisAlignment.CENTER)

    coluna=ft.Column(controls=[line1,line2,line3,line4,line5])
    page.add(coluna)
    page.update()





ft.app(target=main,view=ft.AppView.WEB_BROWSER)
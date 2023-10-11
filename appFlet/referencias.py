#-*- coding: utf-8 -*-
import flet as ft


def main(page):
# Vamos criar referências para usar no posterior
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]() # vai ser a coluna que vamos imprimir as nossas mensagens

    def btn_click(e):
        #vou add os valores capturados pelos TextFields dentro da coluna
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        # limpando as informações
        first_name.current.value = ""
        last_name.current.value = ""
        page.update() # atualizando as paginas
        first_name.current.focus() # trazendo o focu para o primeiro input

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )


ft.app(target=main)
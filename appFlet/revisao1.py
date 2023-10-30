#-*- coding: utf-8 -*-
import os
import pprint

import flet as ft
#pprint.pprint(os.environ['HOMEPATH'])

os.environ["FLET_WS_MAX_MESSAGE_SIZE"]="80000000"
pprint.pprint(dict(os.environ))
#O módulo OS em Python fornece funções para interagir
# com o sistema operacional. OS vem em módulos de utilitário
# padrão do Python. Este módulo fornece uma maneira portátil
# de usar a funcionalidade dependente do sistema operacional.


def main(page:ft.Page):
    page.title="Criando Grids"
    page.window_min_width=200
    #wrap quebra de linha
    #expand permite expandir e ver mais
    #scroll cria uma barra de rolagem
    linha=ft.Row(wrap=True,expand=True,scroll="always")

    titulo=ft.Text("Criando Grids com o click do Botão", size=20)
    btn_criar=ft.FilledButton("Criar")
    def gerarElemento(e):

        linha.controls.append(
            ft.Container(
                ft.Text("Novo texto"),
                width=100, height=100
                , alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(2, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(8)
            )
        )
        page.update()

    btn_criar.on_click = gerarElemento

    page.add(titulo, btn_criar, linha)
    page.update()


ft.app(target=main)

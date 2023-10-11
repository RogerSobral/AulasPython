#-*- coding: utf-8 -*-

import flet as ft

def main(page: ft.Page):

    page.title="To DO List"

    titulo=ft.Text("Lista de Tarefas")

    def addTarefa(e):
        page.add(
            ft.Row(controls=[ft.IconButton(ft.icons.DELETE),ft.Text(value=new_task.value)])
            )
        new_task.value=""
        new_task.focus()
        new_task.update()


    new_task=ft.TextField(hint_text="Add uma nova tarefa",width=300)

    page.add(
        ft.Row(controls=[titulo]),
        ft.Row(
            controls=[ft.ElevatedButton("Add",on_click=addTarefa), new_task],)
    )
    page.update()


ft.app(target=main)

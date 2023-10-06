# -*- coding:utf-8 -*-

import flet as ft
from flet import (
Checkbox,
Column,
FloatingActionButton,
IconButton,
OutlinedButton,
Page,
Row,
Text,
Tab,
Tabs,
TextField,
UserControl,
colors,
icons
)
#Classe de tarefas
class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed =False
        self.task_name=task_name
        self.task_status_change=task_status_change
        self.task_delete=task_delete


#Classe da aplicação toda
class TodoApp(UserControl):
    def build(self):
        self.new_task= TextField(
           hint_text="Descreva a Tarefa",
            expand=True,
            on_submit=self.add_clicked, # um evento dentro do input
        )
        self.tasks=Column()

        self.filter = Tabs(
            selected_index=0,
            on_change= self.tabs_changed,
            tabs=[Tab(text="Todas Tarefas"),
                  Tab(text="Tarefas Ativas"),
                  Tab(text="Tarefas Completadas")]
        )
        return Column(
            width= 600,
            controls=[
                Row([Text(value="Tarefas", style="headlineMedium")
                    ], alignment="center"),

                Row(
                    controls=[ self.new_task]

                )
            ]
        )


    def add_clicked(self):
        pass

#Função Principal
def main(page:ft.Page):
   page.title="Tarefas"
   page.horizontal_alignment= "center"
   page.scroll="adaptive"
   page.update()

# Instanciar a classe principal
   app=TodoApp()
   page.add(app) # adicionando a aplicação principal

ft.app(target=main)
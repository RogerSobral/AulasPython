# *- ecoding: UTF-8 -*
from flet import *

class App(UserControl):

    def __init__(self, pg:Page):
        super().__init__()
        self.pg=pg
        self.init_helper()

    def switch_page(self,e,):
        self.indicator.offset.y = e.control.data
        self.indicator.update()



    def change_page(self,e):
        pass

    def init_helper(self):
        self.indicator = Container(
            bgcolor="red",
            width=3,
            height=40,
            offset= transform.Offset(0,0),
            animate_offset=animation.Animation(500, AnimationCurve.DECELERATE)
        )

        self.pg.add(
            Container(
                expand=True,
                bgcolor="blue",
                content=Row(
                    spacing=0,
                    controls=[
                        Container(
                            padding= padding.only(top=50),
                            bgcolor="white",
                            width=80,
                            content= Row(
                                        spacing=0,
                                        controls=[
                                        Column(
                                            spacing=0,
                                            expand=True,
                                            controls=[


                                                Row( #Botão 1
                                                    controls=[
                                                        Container(
                                                            on_click=self.switch_page,
                                                            expand=True,
                                                            height=40,
                                                            content=Icon(icons.CHAT_BUBBLE,
                                                            color="blue"
                                                            ),
                                                            data = 0,
                                                        ),
                                                    ]
                                                ),

                                                Row( #Botão 2
                                                    controls=[
                                                        Container(
                                                            on_click=self.switch_page,
                                                            expand=True,
                                                            height=40,
                                                            content=Icon(icons.DASHBOARD,
                                                                         color="blue"
                                                            ),
                                                            data = 1,
                                                        )
                                                    ]
                                                ),

                                            ]
                                        ),
                                        Column(
                                            controls=[
                                               self.indicator,
                                            ]

                                        ),
                                        ]
                                    )
                        ), # End of sideBar

                        Container(
                            expand=True,
                            content=Container(
                                expand=True,
                                bgcolor="yellow"
                            )
                        ), #mainScreen
                    ])

            )
        )


app(target=App)

# -*- coding:utf-8 -*-
import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"
    page.background_image_url="assets/fundo.jpg"
    img=ft.Image("")
    page.background_image_url="assets/fundo.jpg"

    coluna=ft.Column(controls=[
        ft.Text("Sei la"),
        ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store"))]
    )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Container(content=coluna,bgcolor=ft.colors.SURFACE_VARIANT,height=350,width=375,alignment=ft.alignment.center
                                 ,opacity=0.5)

                ],vertical_alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
import flet as ft


def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.add(ft.Text("Rudimar"))


ft.app(main)

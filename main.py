import flet as ft
import os

#supabase8836#
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
print(os.environ)

api = os.getenv("API") or os.environ.get("API") or "no API set"


def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.Text("Rudimar Althof's Site - dev"))
    print("API: ", api)
    page.add(ft.Text("API: " + api))


ft.app(main)

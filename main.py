import flet as ft
import os
from CloudFlare import CloudFlare

#supabase8836#
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
print(os.environ)

cf = CloudFlare.CloudFlare()
print(cf)

client = CloudFlare(
    # This is the default and can be omitted
    api_email=os.environ.get("CLOUDFLARE_EMAIL"),
    # This is the default and can be omitted
    api_key=os.environ.get("CLOUDFLARE_API_KEY"),
)

print(client)

api = os.getenv("API") or os.environ.get("API") or "no API set"


def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.Text("Rudimar Althof's Site - dev"))
    print("API: ", api)
    page.add(ft.Text("API: " + api))


ft.app(main)

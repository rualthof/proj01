from dotenv import load_dotenv
load_dotenv()

import flet as ft
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

print (supabase)

api = os.getenv("API") or os.environ.get("API") or "no API set"

def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.Text("Rudimar Althof's Site - dev test push"))
    print("API: ", api)
    page.add(ft.Text("API: " + api))


#supabase8836#
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
print(os.environ)




ft.app(main)
 
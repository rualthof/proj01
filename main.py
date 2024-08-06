from dotenv import load_dotenv
load_dotenv()

import requests

import flet as ft
import os

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

headers = {
    'apikey': supabase_key,
    'Authorization': f'Bearer {supabase_key}',
    'Content-Type': 'application/json'
}

def get_users():
    url = f"{supabase_url}/rest/v1/ToDos"
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
users = get_users()
print(users)

api = os.getenv("API") or os.environ.get("API") or "no API set"

def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.Text("Rudimar Althof's Site - dev test push"))
    print("API: ", api)
    page.add(ft.Text("API: " + api))


#supabase8836#
print("")
print("---------")
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
print(os.environ)




ft.app(main)
 
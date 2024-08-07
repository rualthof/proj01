from dotenv import load_dotenv
load_dotenv()
import requests
import time
import asyncio
import flet as ft
import os

SUPABASE_URL="https://psggxlflowkfoyszdxdc.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBzZ2d4bGZsb3drZm95c3pkeGRjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI4OTk1MTcsImV4cCI6MjAzODQ3NTUxN30.XJwVSC98bHz8yxhkZxR4DEi7WxEbvboCSNbIfxobvOw"

supabase_url =  SUPABASE_URL#os.environ.get("SUPABASE_URL")
supabase_key = SUPABASE_KEY #os.environ.get("SUPABASE_KEY")

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

    def handler(e):
      time.sleep(3)
      page.add(ft.Text("Handler clicked"))

    async def handler_async(e):
      await asyncio.sleep(3)
      page.add(ft.Text("Async handler clicked"))

    page.add(
        ft.ElevatedButton("Call handler", on_click=handler),
        ft.ElevatedButton("Call async handler", on_click=handler_async)
    )


#supabase8836#
print("")
print("---------")
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
#print(os.environ)


#/Users/rudimar/.fly/bin/flyctl launch

ft.app(main, view=ft.AppView.WEB_BROWSER)
 
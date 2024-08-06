import flet as ft
import os

async def on_fetch(request, env):
    data = request.cf if request.cf is not None else None
    print("on fetch")
    print(request)
    print(data)
    bar = await env.FOO.get("bar")
    print(env)
    print(bar)
    #headers = Headers.new({"content-type":"application/json"}.items())
    #return Response.new(JSON.stringify(data, None, 2), headers=headers)

api = os.getenv("API") or os.environ.get("API") or "no API set"

def main(page: ft.Page):
    page.title = "Rudimar's App"
    page.add(ft.Text("Rudimar Althof's Site - dev"))
    print("API: ", api)
    page.add(ft.Text("API: " + api))


#supabase8836#
print(os.getenv("VIRTUAL_ENV"))
print(os.environ.get("VIRTUAL_ENV"))
print(os.getenv("API"))
print(os.environ.get("API"))
#print(os.environ)

#ft.app(main)

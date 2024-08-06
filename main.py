import flet as ft
import os
from cfkv import KVStore

#store = KVStore(namespace_id="1b73c708fab441abad9ca199aca6c5db", account_id="66e8de2e2d9662d21afea4ea9389a0f2", api_key="fKICUL8p6XvAqxcH3XXeWAjszZxDkDJQAoAjsdzw")
store = KVStore(namespace_id="1b73c708fab441abad9ca199aca6c5db", account_id="66e8de2e2d9662d21afea4ea9389a0f2", api_key="v1.0-dcd760b9a724ce811e593663-d2476aada983ec9c94883a34cfeee139706d6cd4b1226fe46600dfe040e3e9648c792759309ed9b05cdf2ebb972505b34c344f946047b3b10d22e93bd9ca3b7d3576a87c1eef721ecf")
print(store)
key = "API"
get = store.get(key)
print("KV value: ", get)

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

ft.app(main)

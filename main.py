import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Weather"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Enter city name', width=300)
    weather_data = ft.Text()

    def get_info(e):
        if len (user_data.value) < 2:
            page.add(ft.Text("Please enter a valid city name"))
            return

        API = 'ef21bb0db0010ff1706664256f58ae93'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = 'Weather: ' + str(temp) + '°C'
        page.update()

    def change_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.SUNNY, on_click=change_theme),
                ft.Text("Weather app")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Get info", on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )







    
    

ft.app(target=main)
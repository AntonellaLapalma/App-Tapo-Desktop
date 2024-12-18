import flet as ft
from funciones import Funciones

# Funciones del control
f = Funciones()

def main(page: ft.Page):
    def animacion_power(e):
        f.power()
        e.control.selected = not e.control.selected
        e.control.update()

    page.title = "Tapo"
    page.window_width = 400
    page.window_height = 710
    page.padding = 0
    page.window_resizable = False
    page.window_top = 370
    page.window_left = 1520
    page.theme = ft.Theme(
        color_scheme = ft.ColorScheme(
            primary = ft.colors.GREY_100,
        ),
    )
    page.add(
        ft.Container(
            content = ft.Column(
                [   
                    ft.Card( # Tarjeta POWER
                        content = ft.Container(
                            content = ft.Row(
                                [
                                    ft.Text(value = str("Alimentación")),
                                    ft.IconButton(
                                        icon = ft.icons.POWER_SETTINGS_NEW_ROUNDED,
                                        selected_icon = ft.icons.POWER_SETTINGS_NEW_ROUNDED,
                                        on_click = animacion_power,
                                        selected = f.estado_luz(),
                                        style=ft.ButtonStyle(color={"selected": '#ffffff', "": '#3C3C3C'})
                                        ),
                                ],
                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            width = 400,
                            padding = 20,
                            bgcolor = '#111111',
                            border_radius = 10,
                        ),
                    ),
                    ft.Card( # Tarjeta BRILLO
                        content = ft.Container(
                            content = ft.Column(
                                [
                                    ft.Text(value = str("Brillo")),
                                    ft.Slider(
                                        min = 1, 
                                        max = 100, 
                                        divisions = 100,
                                        value = f.estado_brillo(), 
                                        label = "{value}%", 
                                        on_change = f.brillo, 
                                        thumb_color = '#ffffff', 
                                        active_color = '#ffffff',
                                        inactive_color = '#1B1B1B'),
                                ],
                            ),
                            width = 400,
                            padding = 20,
                            bgcolor = '#111111',
                            border_radius = 10,
                        ),
                    ),
                    ft.Card( # Tarjeta COLORES GOOGLE
                        content = ft.Container(
                            content = ft.Column(
                                [
                                    ft.Text(
                                        value = str("Colores Google Home")
                                        ),
                                    ft.Container(
                                        content = ft.Dropdown(
                                            hint_text = "Ninguno",
                                            options = [
                                                ft.dropdown.Option('AliceBlue'),
                                                ft.dropdown.Option('LightGoldenrod'),
                                                ft.dropdown.Option('LemonChiffon'),
                                                ft.dropdown.Option('Gold'),
                                                ft.dropdown.Option('Peru'),
                                                ft.dropdown.Option('Chocolate'),
                                                ft.dropdown.Option('SandyBrown'),
                                                ft.dropdown.Option('Coral'),
                                                ft.dropdown.Option('Pumpkin'),
                                                ft.dropdown.Option('Tomato'),
                                                ft.dropdown.Option('Vermilion'),
                                                ft.dropdown.Option('OrangeRed'),
                                                ft.dropdown.Option('Pink'),
                                                ft.dropdown.Option('Crimson'),
                                                ft.dropdown.Option('HotPink'),
                                                ft.dropdown.Option('Smitten'),
                                                ft.dropdown.Option('MediumPurple'),
                                                ft.dropdown.Option('BlueViolet'),
                                                ft.dropdown.Option('Indigo'),
                                                ft.dropdown.Option('LightSkyBlue'),
                                                ft.dropdown.Option('CornflowerBlue'),
                                                ft.dropdown.Option('Ultramarine'),
                                                ft.dropdown.Option('DeepSkyBlue'),
                                                ft.dropdown.Option('Azure'),
                                                ft.dropdown.Option('NavyBlue'),
                                                ft.dropdown.Option('LightTurquoise'),
                                                ft.dropdown.Option('Aquamarine'),
                                                ft.dropdown.Option('Turquoise'),
                                                ft.dropdown.Option('LightGreen'),
                                                ft.dropdown.Option('Lime'),
                                                ft.dropdown.Option('ForestGreen')
                                            ],
                                            autofocus=True,
                                            border=ft.InputBorder.NONE,
                                            on_change=f.colores_google,
                                            color="#FFFFFF",
                                            bgcolor="#000000",
                                        ),
                                    ),
                                ],
                            ),
                            width = 400,
                            padding = 20,
                            bgcolor = '#111111',
                            border_radius = 10,
                        ),
                    ),
                    ft.Card( # Tarjeta HUE
                        content = ft.Container(
                            content = ft.Column(
                                [
                                    ft.Text(value = str("Color")),
                                    ft.Slider(
                                        min = 1, 
                                        max = 360, 
                                        divisions = 360,
                                        value = f.obetener_hue(), 
                                        label = "{value}%", 
                                        on_change = f.cambiar_hue, 
                                        thumb_color = '#ffffff', 
                                        active_color = '#ffffff',
                                        inactive_color = '#1B1B1B'),
                                ],
                            ),
                            width = 400,
                            padding = 20,
                            bgcolor = '#111111',
                            border_radius = 10,
                        ),
                    ),
                    ft.Card( # Tarjeta SATURATION
                        content = ft.Container(
                            content = ft.Column(
                                [
                                    ft.Text(value = str("Saturación")),
                                    ft.Slider(
                                        min = 1, 
                                        max = 100, 
                                        divisions = 100,
                                        value = f.obetener_saturacion(), 
                                        label = "{value}%", 
                                        on_change = f.cambiar_saturacion, 
                                        thumb_color = '#ffffff', 
                                        active_color = '#ffffff',
                                        inactive_color = '#1B1B1B'),
                                ],
                            ),
                            width = 400,
                            padding = 20,
                            bgcolor = '#111111',
                            border_radius = 10,
                        ),
                    ),
                ],
            ),
            width = 400,
            height = 670,
            padding = 20,
            bgcolor = '#1B1B1B',
        ),
    ),
ft.app(main)
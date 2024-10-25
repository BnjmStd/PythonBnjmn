import random
import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.bgcolor = ft.colors.BLACK
    page.title = "Juego de adivinanzas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    title = ft.Text(
        "cards, divider y verticaldivider en flet", size=30, weight=ft.FontWeight.BOLD
    )

    number_secret = random.randint(1, 10)
    intentos = 0

    def verificar_intento(e):
        nonlocal intentos

        intento = int(input_numero.value)
        intentos += 1
        if intento == number_secret:
            resultado.value = f"Correcto, lo adivinaste en {intentos} intentos"
            resultado.color = ft.colors.GREEB
            verificar_btn.disable = True


    input_numero = ft.TextField(
        label="Tu intento!", 
        width=100
    )

    verificar_btn =  ft.ElevatedButton('verificar', on_click=verificar_btn)
    resultado = ft.Text("adivina el número entre 1 y 10")

    card_simple = ft.Card(
        content = ft.Container(
            content=ft.Column(
                [
                    input_numero,
                    verificar_btn,
                    resultado
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            padding=10,
        ),
        width=200,
        height=100,
    )

        
    card_2 = ft.Card(
        content = ft.Container(
            content = ft.Text("c2"),
            padding=10
        ),
        width=200,
        height=100,
    )

    divider_simple = ft.Divider(height=1, 
    color=ft.colors.BLUE_200)

    layout = ft.Row(
        [
            card_simple,
            divider_simple,
            card_2

        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        title,
        layout
    )

ft.app(target=main)
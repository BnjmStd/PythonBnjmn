import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.AMBER_200
    page.title = "app filas y columnas"
    text1 = ft.Text("texto 1", size=24, color=ft.colors.WHITE)
    texto2 = ft.Text("texto 2", size=18, color=ft.colors.RED_ACCENT_100)

    fila_textos = ft.Row(
        controls=[text1, texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_textos)

    boton1 = ft.FilledButton(text="boton 1")
    boton2 = ft.FilledButton(text="boton 2")
    boton3 = ft.FilledButton(text="boton 3")

    fila_botones = ft.Row(
        controls=[boton1, boton2, boton3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_botones)

    textColumnas = [
        ft.Text("columna 1 - Fila 1", size=18, color=ft.colors.WHITE),
        ft.Text("columna 1 - Fila 2", size=18, color=ft.colors.WHITE),
        ft.Text("columna 1 - Fila 3", size=18, color=ft.colors.WHITE)
    ]

    columna_text1 = ft.Column(
        controls=textColumnas
    )

    textColumnas2 = [
        ft.Text("columna 2 - Fila 1", size=18, color=ft.colors.WHITE),
        ft.Text("columna 2 - Fila 2", size=18, color=ft.colors.WHITE),
        ft.Text("columna 2 - Fila 3", size=18, color=ft.colors.WHITE)
    ]

    columna_text2 = ft.Column(
        controls=textColumnas2
    )

    filaColumnas = ft.Row(
        controls=[columna_text1, columna_text2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(filaColumnas)

ft.app(target=main)  
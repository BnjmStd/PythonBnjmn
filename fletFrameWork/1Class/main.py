"""
Este módulo utiliza la biblioteca Flet para crear una interfaz de usuario.
Flet es un framework que permite construir aplicaciones web, móviles y de escritorio usando 
Python.
"""

import flet as ft

def main(page: ft.Page):
    """
    Función principal que configura y maneja la interfaz de usuario usando Flet.

    Args:
        page (ft.Page): Página principal de la aplicación donde se añaden los controles y 
        componentes de UI.
    """

    page.bgcolor = ft.colors.AMBER_400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Mi app"
    text = ft.Text("Hola mundo!")


    def cambiarTexto(e):
        text.value = "Suscribete!"
        page.update()


    buton = ft.FilledButton(text="Cambiar texto", on_click=cambiarTexto)
    page.add(text, buton)


ft.app(target=main)

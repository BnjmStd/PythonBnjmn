import flet as ft
import random


import flet as ft
import random

def generar_tareas():
    tareas = [
        "hacer la compra", "llamar al médico", "estudiar", "hacer ejercicio", "leer un libro", "preparar la cena"
    ]
    return random.sample(tareas, k=4)

def main(page: ft.Page):

    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Tabs en flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("Ejemplo de tabs en flet", size=24, color=ft.colors.WHITE)

    # Definir lista_tareas antes de actualizar_tareas
    lista_tareas = ft.ListView(
        spacing=10,
        padding=20
    )
    
    def actualizar_tareas():
        lista_tareas.controls.clear()  # Ahora lista_tareas ya está definida
        for tarea in generar_tareas():
            lista_tareas.controls.append(
                ft.Text(
                    tarea, color=ft.colors.WHITE
                )
            )
        page.update()

    actualizar_tareas()

    boton_actualizar = ft.ElevatedButton(
        "Actualizar tareas",
        on_click=lambda _: actualizar_tareas()
    )

    contenido_tareas = ft.Column(
        [
            lista_tareas, boton_actualizar
        ]
    )

    # contenido para la pestaña de Perfil

    campo_nombre = ft.TextField(label="nombre", bgcolor=ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField(label="email", bgcolor=ft.colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton("Guardar perfil")
    contenido_perfil = ft.Column([campo_nombre, campo_email, boton_guardar])


    # content settings

    switch_notificaciones = ft.Switch(label="notificaciones", value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label="volumen")
    contenido_config = ft.Column([switch_notificaciones, slider_volumen])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Perfil", icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(text="Configuraciones", icon=ft.icons.SETTINGS, content=contenido_config),
        ],
        expand=1
    )

    page.add(tabs)

ft.app(target=main)

import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.AMBER_400
    page.title = "Mi list to task"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    title = ft.Text("Mi lista de tareas con flet", size=30, weight=ft.FontWeight.BOLD)

    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title= ft.Text(campo_tarea.value), leading=ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()
    
    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ".join(seleccionadas)
        page.update()

    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()

    campo_tarea = ft.TextField(hint_text="Escribe una nueva tarea! ...")
    boton_agregar = ft.FilledButton(text="Add tarea", on_click=agregar_tarea)

    lista_tareas = ft.ListView(expand=1, spacing=5)

    tareas = []

    tareas_seleccionadas = ft.Text("", size=20, weight=ft.FontWeight.BOLD)

    page.add(title, campo_tarea, tareas_seleccionadas, boton_agregar, lista_tareas)


ft.app(target=main)
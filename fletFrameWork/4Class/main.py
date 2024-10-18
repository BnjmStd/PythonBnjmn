"""
Programa de notas con gridView
"""

import flet as ft


def main(page: ft.Page):
    """
     
    cosas
    
    """

    def add_note(e):
        new_note = create_note("nueva Nota")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):

        note_content = ft.TextField(
            value=text, multiline=True,
            bgcolor=ft.colors.BLUE
        )

        note = ft.Container(
            content=ft.Column([
                    note_content,
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda _: delete_note(note)
                    )
                ]),
            width=200,
            height=200,
            bgcolor=ft.colors.BLACK,
            border_radius=10,
            padding=10
        )

        return note

    page.title = "Tablero de notas"
    page.bgcolor = ft.colors.AMBER_300
    page.theme_mode = "dark"

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        horizontal=False,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=10
    )

    notes = [
       "Comprar leche",
        "Llamar al médico",
        "reunión a las 3 pm"
    ]


    for note in notes:
        grid.controls.append(create_note(note))


    page.add(ft.Row([
            ft.Text("Mis notas", size=24, weight='bold', 
                color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )


    page.add(grid)


ft.app(target=main)

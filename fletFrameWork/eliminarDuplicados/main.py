import flet as ft

def main(page: ft.Page):
    # conf basic windows

    page.title = "Rapidín Python"
    page.window.width = 1000
    page.window.height
    page.padding = 0
    page.bgcolor = ft.colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK

    # add theme perso
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE,
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.ORANGE,
            background=ft.colors.GREEN_900,
            surface=ft.colors.GREY_800,
        )
    )

    def change_view(e):
        selected = e.control.selected_index

        if selected == 0:
            content_area.content = duplicate_files_view
        elif selected == 1:
            content_area.content = ft.Text("Próximamente ...", size=24)

        content_area.update()
        
    # variable de estado

    selected_dir_text = ft.Text(
        "No se ha seleccionado ninguna carpeta",
        size=14,
        color=ft.colors.BLUE_200
    )

    def handle_folder(e: ft.FilePickerResultEvent):
        if e.path:
            selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
            selected_dir_text.update()

    # conf view folder

    folder_picker = ft.FilePicker(on_result=handle_folder)
    page.overlay.append(folder_picker)

    # vista de archivos duplicados
    duplicate_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Eliminar Archivo duplicado",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_200,
                ),
                margin=ft.margin.only(bottom=20),
            ),
            ft.ElevatedButton(
                "seleccionar folder",
                icon=ft.icons.FOLDER_OPEN,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_900,
                on_click=lambda _: folder_picker.get_directory_path(),
            ),
            ft.Container(
                content=selected_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
            )
        ]),
        padding=30,
        expand=True
    )

    content_area = ft.Container (
        content=ft.Text("vista de duplicados", size=24),
        expand=True,
        padding=30
    )

    # Menú lateral

    rail  = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DELETE_FOREVER,
                selected_icon=ft.icons.DELETE_FOREVER,
                label="Dupli"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                label="Proxi ... "
            )
        ],
        on_change=change_view,
        bgcolor=ft.colors.GREEN_900
    )

    page.add(ft.Row(
        [
           rail,
           ft.VerticalDivider(width=1),
           content_area
        ],
        expand=True
    ))


if __name__ == "__main__":
    ft.app(target=main)

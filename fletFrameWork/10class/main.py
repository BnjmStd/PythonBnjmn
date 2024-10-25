import flet as ft
import time

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_600
    page.title = "Simulador de Descarga"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("simulador de descarga de archivos", size=24, color=ft.colors.BLACK)
    files = ft.Text("Selecciona archivos para descargar", size=16, color=ft.colors.BLACK)

    file_list = ft.Column([
        ft.Checkbox(label="document.pdf (2.5 mb)",value=False),
        ft.Checkbox(label="document.pdf (2.5 mb)",value=False),
        ft.Checkbox(label="document.pdf (2.5 mb)",value=False),
        ft.Checkbox(label="document.pdf (2.5 mb)",value=False),
    ])

    def simular_descarga(e):
        select_files = [checkbox for checkbox in file_list.controls if checkbox.value]
        
        if not select_files:
            status_text.value = "Por favor, selecciona al menos un archivo."
            page.update()
            return 
        
        progress_bar.value = 0
        progress_ring.value = 0
        page.update()


        total_size = sum([float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in select_files])

        downloaded = 0

        for archivo in file_list:
            file_size = float(archivo.label.split("(")[1].split(" MB")[0])
            status_text.value = f"Descargando { archivo.label }"
        
            for _ in range(10):
                time.sleep(0.3)
                downloaded += file_size/10
                progress = min(downloaded / total_size, 1)
                progress_bar = progress
                progress_ring = progress

                page.update()

    containt = ft.Container(content=file_list, padding=24)


    progress_bar = ft.ProgressBar(
        width=400, 
        color="amber", 
        bgcolor="#263238",
        value=0
    )

    progress_ring = ft.ProgressRing(stroke_width=5, color="amber", value=0)

    row = ft.Row([
        progress_bar, 
        progress_ring
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    status_text = ft.Text("", color=ft.colors.BLACK)

    download_btn = ft.ElevatedButton("Iniciar descarga", 
                                     on_click=simular_descarga, bgcolor=ft.colors.AMBER_100, color=ft.colors.BLACK)

    page.add(title, files, containt, row, status_text, download_btn)

ft.app(target=main)
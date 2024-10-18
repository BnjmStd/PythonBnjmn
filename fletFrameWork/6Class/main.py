import flet as ft
from openpyxl import Workbook
from datetime import datetime

#  pip install openpyxl

def main(page: ft.Page):
    page.bgcolor = ft.colors.AMBER_700
    page.title = "datatable en flet con excel"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("datatable", size=24, color=ft.colors.WHITE)

    data_table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_700,
        border=ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, ft.colors.BLUE_GREY_200),
        columns= [
            ft.DataColumn(ft.Text("ID", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Nombre", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("edad", color=ft.colors.BLUE_200))
        ],
        rows=[]
    )

    def agregar_fila(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows) + 1), color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.WHITE))
            ]
        )

        data_table.rows.append(nueva_fila)

        nombre_input.value = ""
        edad_input.value = ""

        page.update()

    def guardar_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title = "Datos de la tabla"
        ws.append(["ID", "NOMBRE", "EDAD"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"{fecha_hora}_datos.xlsx"
            wb.save(nombre_archivo)

            snack_bar = ft.SnackBar(content=ft.Text(f"Datos guardados en {nombre_archivo}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True 

            page.update()

    nombre_input = ft.TextField(label="Nombre", bgcolor=ft.colors.BLUE_GREY_700, color=ft.colors.WHITE)
    edad_input = ft.TextField(label="edad", bgcolor=ft.colors.BLUE_GREY_700, color=ft.colors.WHITE)

    add_boton = ft.ElevatedButton(
        "Agregar", on_click=agregar_fila, color=ft.colors.WHITE, bgcolor=ft.colors.BLUE
    )

    guardar_boton = ft.ElevatedButton("guardar en excel", on_click=guardar_excel, color=ft.colors.WHITE, bgcolor=ft.colors.GREEN)

    input_container = ft.Row(
        controls=[nombre_input, edad_input, add_boton, guardar_boton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(title, data_table, input_container)

ft.app(target=main)

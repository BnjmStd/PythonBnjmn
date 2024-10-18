import flet as ft
import os
import base64

def crear_producto(nombre, precio, color, name_image):
    image_path = os.path.join(os.path.dirname(__file__), "assets", name_image)

    try:
        with open(image_path, "rb") as image_file:
            imagen_bytes = base64.b16encode(image_file.read()).decode()
    except FileNotFoundError:
        print(f"Warning!: la imagen {name_image} no existe")
        imagen_bytes = None

    return ft.Container(
        content=ft.Column([
            ft.Image(
                src_base64=imagen_bytes,
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Image not found") if imagen_bytes else ft.Text("image no encontraaada")
            ),
            ft.Text('producto1', size=16, weight=ft.FontWeight.BOLD),
            ft.Text("$19.9", size=14),
            ft.ElevatedButton("Add to cart", color=ft.colors.WHITE)
        ]),
        bgcolor=ft.colors.BLUE_500,
        border_radius=10,
        padding=10,
        alignment=ft.alignment.center
    )

def main(page: ft.Page):
    page.title = "Galeria de productos"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.AMBER_500

    productos = [
        crear_producto("Producto 1", 19.99, ft.colors.BLUE_500, "1.png"),
        crear_producto("Producto 2", 19.99, ft.colors.GREEN_500, "2.png"),
        crear_producto("Producto 2", 19.99, ft.colors.ORANGE_500, "3.png"),
        crear_producto("Producto 3", 19.99, ft.colors.WHITE24, "4.png"),
    ]
    
    galary = ft.ResponsiveRow(
        [
            ft.Container(producto, col={
                "sm": 12,
                "md": 6,
                "lg": 3
            }) for producto in productos
        ],
        run_spacing=20,
        spacing=20
    )

    content = ft.Column([
        ft.Text("Galery of Products", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.WHITE24),
        galary
    ], scroll=ft.ScrollMode.AUTO, expand=True)

    page.add(content)

ft.app(target=main)

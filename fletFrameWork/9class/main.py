import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.AMBER_400
    page.title = "demostracion de stack, Image y circleavatar en flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"

    text_title = ft.Text(
        "demostración  de stack, Image, y circle", size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD
    )

    def create_example(title, description, content):
        return ft.Container(
            content=ft.Column([
            ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            ft.Text(description, color=ft.colors.GREY_500),
            ft.Container(
                content=content, padding=10, 
                border=ft.border.all(1, ft.colors.GREY_400)
            )
        ]), margin=ft.margin.only(bottom=20)
        )
    
    stack_example = ft.Stack(
        [
            ft.Container(
                width=200, height=200, bgcolor=ft.colors.BLUE_900
            ),
            ft.Container(
                width=150, height=150, bgcolor=ft.colors.BLUE_700,
                left=25, top=25
            ),
            ft.Container(
                width=100, height=100, bgcolor=ft.colors.BLUE_500,
                left=50, top=50
            ),
            ft.Text("stack demo", color=ft.colors.WHITE, size=12, left=70, top=90)
        ],
        width=200,
        height=200
    )

    stack_ = create_example(
        "stack", "stack un mejor lugar",
        stack_example
    )



    image_internet = ft.Image(
        src="https://picsum.photos/200/200", width=200
    )

    image_local = ft.Image(src="assets/image.png", width=200)

    column_imge = ft.Column([
        image_internet,
        ft.Text("Img desde Url", size=14, color=ft.colors.GREEN_700),
        image_local,
        ft.Text("Imagen local", size=14, color=ft.colors.BLUE_900)
    ])

    image_example = create_example(
        "Image",
        "description img", column_imge
    )

    img_avatar = ft.CircleAvatar(
        foreground_image_url="https://avatars.githubusercontent.com/u/5479691",
        radius=50
    )


    page.add(text_title, stack_, image_example)

ft.app(target=main)
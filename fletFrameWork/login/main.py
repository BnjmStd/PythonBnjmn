import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()


        c1 = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column([
                            ft.Text(
                                "Iniciar Sesión",
                                width=360,
                                size=30,
                                weight='w900',
                                text_align="center"
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='correo electronico',
                                    border='underline',
                                    color='black',
                                    prefix_icon= ft.icons.EMAIL,                                    
                                ),
                                padding=ft.padding.only(20,30)
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='contraseña',
                                    border='underline',
                                    color='black',
                                    prefix_icon=ft.icons.LOCK,
                                    password=True,
                                ),
                                padding= ft.padding.only(20,10)
                            ),
                            ft.Container(
                                ft.Checkbox(
                                    label='recordar contraseña',
                                    check_color='black'
                                ),
                                padding=ft.padding.only(40),
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content = ft.Text(
                                        'iniciar',
                                        color='white',
                                        weight='w500',
                                    ),
                                    width=200,
                                    bgcolor='black'
                                ),
                                padding=ft.padding.only(25, 10)
                            ),
                            ft.Container(
                                ft.Row([
                                    ft.Text(
                                        '¿No tiene una cuenta?'
                                    ),
                                    ft.TextButton(
                                        'crear cuenta',
                                        on_click=animate
                                    ),
                                    
                                ], spacing=8),
                                padding=ft.padding.only(40)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.PURPLE,
                        expand=True,
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text(
                                    'Bienvenido!',
                                    size=40,
                                    font_family="Georgia",

                                ),
                                ft.Container(
                                    ft.Image(
                                        src='1.png',
                                        width=200,
                                    ),
                                    padding=ft.padding.only(20, 20),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.CYAN,
                        expand=True,
                        border_radius=ft.BorderRadius(
                            top_left=100,
                            top_right=0,
                            bottom_left=100,
                            bottom_right=0,
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),

            alignment=ft.alignment.center,
            width=700,
            height=400,
            bgcolor=ft.colors.PURPLE,
            border_radius=40
        )

        c2 = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text(
                                    "Bienvenido!",
                                    size=40,
                                    font_family="Georgia"
                                ),
                                ft.Container(
                                    ft.Image(
                                        src="logo2.png",
                                        width=200,
                                    ),
                                    padding=ft.padding.only(20,20),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.PURPLE,
                        expand=True,
                        border_radius=ft.BorderRadius(
                            top_left=0,
                            top_right=100,
                            bottom_left=0,
                            bottom_right=100,
                        )
                    ),

                    ft.Container(
                        ft.Column([
                            ft.Text(
                                'crear cuenta',
                                width=360,
                                size=30,
                                weight='w900',
                                text_align='center',
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text="nombre",
                                    border='underline',
                                    color='black',
                                    prefix_icon=ft.icons.PERM_CONTACT_CAL
                                ),
                                padding=ft.padding.only(20, 10)
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='correo electronico',
                                    border='underline',
                                    color='black',
                                    prefix_icon=ft.icons.EMAIL,
                                    password=True,
                                ),
                                padding= ft.padding.only(20,10)
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='contraseña',
                                    border='underline',
                                    color='black',
                                    prefix_icon=ft.icons.LOCK,
                                    password=True,
                                ),
                                padding=ft.padding.only(20,10)
                            ),

                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        'registrarse',
                                        color='white',
                                        width='w500',
                                    ),
                                    width=280,
                                    bgcolor='black',
                                ),
                                padding=ft.padding.only(25,10)
                            ),
                            ft.Container(
                                ft.Row([
                                    ft.Text(
                                        'Ya tiene una cuenta'
                                    ),
                                    ft.TextButton(
                                        'iniciar sesion',
                                        on_click=animate
                                    ),
                                ], spacing=8),
                                padding=ft.padding.only(40)
                            ),   
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.CYAN,
                        expand=True,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
                        alignment=ft.alignment.center,
            width=700,
            height=400,
            bgcolor=ft.colors.PURPLE,
            border_radius=40
        )

        c= ft.AnimatedSwitcher(
            c1,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.DECELERATE,
            switch_out_curve=ft.AnimationCurve.EASE
        )

        page.add(c)

ft.app(target=main)
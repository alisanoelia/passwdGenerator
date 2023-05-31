import flet
from flet import *
import random
import pyperclip

def main(page:Page):
    page.title = 'Generador de password :v'
    page.theme_mode = ThemeMode.DARK
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = '#F4BDC9'

    divider = Divider(height=50)


    minus = "abcdefghijklmnopñqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    nums = "0123456789"
    symbols = " !@#$%^&*()-_+=<>{}[]|/?.,;:~' "

    def generate(e):
        if check_num.value == False and check_symbols.value == False:
            longitud = int(num_caracteres.value)
            passw = random.sample(minus, longitud)
            password1 = "".join(passw)
            password.value = password1
            page.update()
        elif check_num.value == True and check_symbols.value == True:
            longitud = int(num_caracteres.value)
            passwd = minus + nums + symbols
            passwd = random.sample(passwd, longitud)
            password4 = "".join(passwd)
            password.value = password4
            print(password.value)
            page.update()
        elif check_num.value == True:
            longitud = int(num_caracteres.value)
            passwd_nums = minus + nums
            passwd_nums = random.sample(passwd_nums, longitud)
            password2 = "".join(passwd_nums)
            password.value = password2
            page.update()
        elif check_symbols.value == True:
            longitud = int(num_caracteres.value)
            passwd_symbols = minus + symbols
            passwd_symbols = random.sample(passwd_symbols, longitud)
            password3 = "".join(passwd_symbols)
            password.value = password3
            print(password)
            page.update()

    def minus_caracter(e):
        if num_caracteres.value == "1":
            print('error')
        else:
            num_caracteres.value = str(int(num_caracteres.value) - 1)
            page.update()

    def max_caracter(e):
        num_caracteres.value = str(int(num_caracteres.value) + 1)
        page.update()



    def copy(e):
        pyperclip.copy(password.value)
        print("Texto guardado en el portapapeles.")


    titulo = Container(
            width=250,
            height=60,
            bgcolor='#333333',
            border_radius=25,
            content=Text(
                value='Password',
                text_align=TextAlign.CENTER,
                size=40,
                )
            )

    num_caracteres = TextField(
            value="8",
            width=50,
            text_align=TextAlign.CENTER,
            bgcolor='#333333',
            )

    btm_min = IconButton(
            icons.REMOVE,
            on_click=minus_caracter
            )

    btm_max = IconButton(
            icons.ADD,
            on_click=max_caracter
            )

    check_num = Checkbox(
            label='Include numbers',
            value=False
            )

    check_symbols = Checkbox(
            label='Include simbols',
            value=False
            )

    btm_generated = ElevatedButton(
            text='Generated Password',
            on_click=generate,
            height=50,
            )

    password = Text(
            value='',
            size=40,
            text_align=TextAlign.CENTER,
            selectable=True,
            )

    btn_copy = IconButton(
            icons.COPY,
            on_click=copy
            )

    password_generate = Container(
            width=400,
            border_radius=25,
            bgcolor='#333333',
            content=Column([
                Row([
                    password,
                    Row([
                        btn_copy,
                        ], alignment=MainAxisAlignment.END),
                    ], alignment=MainAxisAlignment.CENTER),
                ])
            )



    container_main = Container(
            width=500,
            height=500,
            bgcolor="#0b0f10",
            border_radius=25,
            expand=True,
            alignment=alignment.center,
            content=
                Column([
                    Row([titulo], alignment=MainAxisAlignment.CENTER),
                    divider,
                    Row([btm_min, num_caracteres, btm_max], alignment=MainAxisAlignment.CENTER),
                    Row([check_num, check_symbols], alignment=MainAxisAlignment.CENTER),
                    divider,
                    Row([btm_generated], alignment= MainAxisAlignment.CENTER),
                    Row([password_generate], alignment=MainAxisAlignment.CENTER)
                    ], alignment=MainAxisAlignment.CENTER)
                )



    page.add(
            container_main
            )

flet.app(target=main, port=8080, view=WEB_BROWSER)

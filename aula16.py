import flet as ft 


def main(page: ft.Page):
   page.fonts={
        'Kanit-Black':'fonts\Kanit-Black.ttf'
   }
   t1 = ft.Text(
       value='Bem vindo ao curso de Flet',
       style=ft.TextThemeStyle.DISPLAY_LARGE,
       bgcolor=ft.colors.WHITE54,
       color=ft.colors.BLACK,
       #font_family='Kanit-Black',
       #definir o numero maximo de linha
       max_lines=2,
       # se o texto não caber na 2 linhas o flet coloca ...
       overflow=ft.TextOverflow.ELLIPSIS,
       
       
       )
   page.add(t1)
   
ft.app(target=main, assets_dir='assets')
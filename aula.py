import flet as ft


#
#  Aula 11
#
# definição da caracteristicas e funções da pagina e sistema operacional
#
#def main(page: ft.Page):
#    pass


# chama a função definida na main
#ft.app(target=main)


# chmando na forma de classes

class App:
    def __init__(self, page: ft.Page):
        mensagem = ft.Text(value='Olá mundo')
        page.add(mensagem)


ft.app(target=App)

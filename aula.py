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
        #
        # formas de atribuir cores
        #
        #page.bgcolor = 'Green'
        #page.bgcolor = '#B12B12'
        page.bgcolor = ft.colors.AMBER        
        page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        #page.padding = ft.padding.all(10)
        #page.padding = ft.padding.symmetric(vertical=10, horizontal=100) 
        page.padding = ft.padding.only(top=10, left=20, right=20, bottom=200)
        page.spacing = 100
        # titulo na barra do celular no topo da tela
        page.title = 'Flet - aula'
        page.add(
            ft.Text(value='Ola mundo'),
            ft.Container(ft.Text(value='Ola mundo 2'), bgcolor='RED'),
            ft.Container(ft.Text(value='Ola mundo 2'), bgcolor='RED')
        )     
        page.update()

#

ft.app(target=App)

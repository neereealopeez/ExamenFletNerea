import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6

    #Fin --- Ejercicio 6


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250

    #Ejercicio 2
    img = ft.Image(src="Logo.png",width=150,height=150)
    #Fin --- Ejercicio 2


    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4
    tfpassword = ft.TextField(label="Contraseña")
    #Fin --- Ejercicio 4


    #Ejercicio 5

    #Fin-- Ejercicio 5


    page.add(img,tfnombre,tfpassword)
    


ft.app(target=main,assets_dir="imagenes")
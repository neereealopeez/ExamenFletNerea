import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6

    #Fin --- Ejercicio 6


    #Ejercicio 2
    
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250



    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4
    

    #Fin --- Ejercicio 4


    #Ejercicio 5

    #Fin-- Ejercicio 5


    page.add(img,tfnombre,tfpassword,btnEntrar)
    


ft.app(target=main,assets_dir="imagenes")
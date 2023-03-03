import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"
    #Ejercicio 6
    

    def entrar(e):
        if tfnombre.value == tfpassword.value:
            dlg = ft.AlertDialog(title=ft.Text("La contraseña es correcta."), on_dismiss=lambda e: print("Dialog dismissed!"))
            page.dialog = dlg
            dlg.open = True
        
            page.update()
    

    #Fin --- Ejercicio 6


    #Ejercicio 2

    img=ft.Image(src=f"esto no se ve",width=100,height=100)
    img.src="Logo.png"

    #Fin --- Ejercicio 2


    #Ejercicio 3
    
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250
    tnombre = ft.Text()
    tfnombre = ft.TextField(label="Nombre")

    #Ejercicio 4
    tpassword = ft.Text()
    tfpassword= ft.TextField(label="Password", password=True, can_reveal_password=True)

    #Fin --- Ejercicio 4


    #Ejercicio 5

    btnEntrar= ft.ElevatedButton("Entrar",icon="SETTINGS_ACCESSIBILITY",icon_color="#62C5C8", on_click=entrar)

    #Fin-- Ejercicio 5

    page.add(img,tfnombre,tfpassword, btnEntrar, tnombre, tpassword)
    
ft.app(target=main,assets_dir="fotos")
# https://www.youtube.com/watch?v=Ih18LFBOhZc&list=PL441cQBT_dHUJOL-6ZC6BsglGgxePGt4f&index=9
# Crear barra de Menú // TKINTER DESDE 0 | 8 Crear Menu

from tkinter import *

class Menu_pricipal(Tk):
    def __init__(self):
        super().__init__()
        self.barra_menu = Menu() # creamos una variable y le asignamos la función Menu
        self.config(menu=self.barra_menu)

        #Menu Servicio              
        serviciosMenu = Menu(self.barra_menu, tearoff=0)

        serviciosMenu.add_command(label="Nuevo")
        serviciosMenu.add_command(label="Abrir")
        serviciosMenu.add_command(label="Modificar")
        serviciosMenu.add_command(label="Eliminar")
        serviciosMenu.add_separator()                # separador __________
        serviciosMenu.add_command(label="Salir", command=self.quit) # le agregamos la funcion "quit" para salir de la ventana

        #Menu Clientes
        clientesMenu = Menu(self.barra_menu, tearoff=0)

        clientesMenu.add_command(label="Abrir")
        clientesMenu.add_command(label="Agregar Nuevo")
        clientesMenu.add_command(label="Modificar")
        clientesMenu.add_command(label="Cambiar Estado")

        #Menu Ventas
        ventasMenu = Menu(self.barra_menu,tearoff=0)

        ventasMenu.add_command(label="Ver Ventas",command=self.prueba1)
        ventasMenu.add_command(label="Cobrar")

        #Cascada/linita barra de tareas
        self.barra_menu.add_cascade(label="Servicios", menu=serviciosMenu)
        self.barra_menu.add_cascade(label="Clientes", menu=clientesMenu)
        self.barra_menu.add_cascade(label="Ventas", menu=ventasMenu)

    def prueba1(self):
        #root.destroy()
        self.ventana2 = Toplevel()
        self.ventana2.title("jajja")
        prueba_label = Label(self.ventana2,text="Lo estamos haciendo bien")
        prueba_label.pack()


if __name__ == "__main__":
    menu_p = Menu_pricipal()
    menu_p.mainloop()
#class Login
#Menu_principal -- opciones 3 -serv,clientes,ventas
#Menu_serv --- 
#menu_cliente
#menu_ventas --- ver_ventas-cobrar
import tkinter as tk
from tkinter import messagebox

# Crear una ventana emergente sin prefijo
#ventana_registro = Toplevel()
from login import *

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Salon de Belleza")
        self.geometry("600x400")

        bienv = tk.Label(self,text="Bienvenido")
        bienv.pack(pady=10)
        bienv2 = tk.Label(self,text= "Ingrese a la Aplicación")
        bienv2.pack(pady=10.5)

        #VENTANA PRINCIPAL
        #Usuario
        usuario_l = tk.Label(self,text= "Usuario")
        usuario_l.pack(pady= 12)
        self.usuario_e = tk.Entry(self)
        self.usuario_e.pack(pady=12.5)

        #Contraseña
        contra_l = tk.Label(self,text="Password")
        contra_l.pack(pady= 18)
        self.contra_e = tk.Entry(self,show="*")
        self.contra_e.pack(pady = 18.5)

        #botonInicio
        boton_inic = tk.Button(self,text="Iniciar Sesion",command= self.iniciar_sesion)
        boton_inic.pack(padx=30,pady=25)
        

        #registrarse

        #botonRegistrarse
        boton_regi = tk.Button(self,text="Registrarse",command= self.abrir_registro)
        boton_regi.pack()

    #Abre ventana nueva al presionar #Registrarse
    def abrir_registro(self):
        self.ventana_registro = tk.Toplevel(self) #crea nueva ventana
        self.ventana_registro.title("Registro")
        nombre_l = tk.Label(self.ventana_registro,text="Nombre")
        nombre_l.pack()
        self.nombre_e = tk.Entry(self.ventana_registro)
        self.nombre_e.pack()

        apellido_l = tk.Label(self.ventana_registro,text="Apellido")
        apellido_l.pack()
        self.apellido_e = tk.Entry(self.ventana_registro)
        self.apellido_e.pack()

        dni_l = tk.Label(self.ventana_registro,text="Dni")
        dni_l.pack()
        self.dni_e = tk.Entry(self.ventana_registro)
        self.dni_e.pack()

        tel_l = tk.Label(self.ventana_registro,text="Tel")
        tel_l.pack()
        self.tel_e = tk.Entry(self.ventana_registro)
        self.tel_e.pack()
        
        rol_l = tk.Label(self.ventana_registro,text="Rol")
        rol_l.pack()
        #self.rol_e = tk.Entry(self.ventana_registro)
        #self.rol_e.pack()
        
        self.opcion_seleccionada = tk.StringVar(self.ventana_registro) #menu desplegable
        self.opcion_seleccionada.set("cajero")  # Opción por defecto

        # Lista de opciones
        opciones = ["cajero", "admin"]

        # Crear el OptionMenu
        self.rol_e = tk.OptionMenu(self.ventana_registro, self.opcion_seleccionada, *opciones)
        self.rol_e.pack()


        clave_l = tk.Label(self.ventana_registro,text="Clave")
        clave_l.pack()
        self.clave_e = tk.Entry(self.ventana_registro)
        self.clave_e.pack()

        boton_cr= tk.Button(self.ventana_registro, text="Crear nuevo usuario", command=self.registrarse)
        boton_cr.pack()
        
    def iniciar_sesion(self):
        usuario = self.usuario_e.get()
        contra = self.contra_e.get()

        if login(usuario,contra) == True:
            messagebox.showinfo("Inicio Sesion","Acceso Concedido")
            self.destroy()
            #if acceso == true:

            #llamar otra clase (encerrar clase nueva en un varible)
            #mainlopp de la nueva clase
        else:
            messagebox.showerror("Error","Acceso denegado")

    def registrarse(self):
        nombre = self.nombre_e.get()
        apellido = self.apellido_e.get()
        dni = self.dni_e.get()
        tel = self.tel_e.get()
        rol = self.opcion_seleccionada.get()
        clave = self.clave_e.get()
       
    
        if not nombre or not apellido or not dni or not tel or not rol or not clave: 
            messagebox.showerror("Error","Debe completar todos los campos")
            return
        if not nombre.isalpha() or not apellido.isalpha():
            messagebox.showerror("Error","Debe ingresar caracteres alfabeticos")       
            return
        if not dni.isdigit() or len(dni)!= 8:
            messagebox.showerror("Error","Debe ingresar un DNI de 8 digitos")
            return
        if not tel.isdigit():
            messagebox.showerror("Error","Debe ingresar solo")  
            return  
        
        registrar(nombre,apellido,dni,tel,rol,clave) #funcion de modulo login ficheros
        messagebox.showinfo("Éxito", "Usuario registrado con éxito")
        self.ventana_registro.destroy() 
        

    #def acceso(self):

    #match con rol , == admin True , else False


if __name__ == "__main__":
    login_app = Login()
    login_app.mainloop()


git remote add origin https://github.com/sabrina-arganaraz/Tecnicasdeprogramacion.git
git branch -M main
git push -u origin main





from clientes import *
import datetime as dt

def ventas():
    with open("Transacciones.txt","r") as archivo:
        print(archivo.readlines())
        
def cobrar(dni,serv):
    fecha = dt.datetime.now()
    fecha1 = fecha.strftime("%d-%m-%Y %H:%M")
    with open("Clientes.txt","r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            a = i.strip().split(",")
            if buscar_cliente(dni) == True:
                b = a[2] # dni
                n_c = a[0]
                a_c = a[1]
    with open("Servicios.txt","r") as archivo_s:
        lineas_s = archivo_s.readlines()   
        for j in lineas_s:
            s = j.strip().split(",")   
            if serv == s[0]:
                n_s = s[0]
                p_s = s[1]
    with open("Transacciones.txt","a") as archivo_t:
        archivo_t.write(fecha1)
        archivo_t.write(",")
        archivo_t.write(n_c)
        archivo_t.write(",")
        archivo_t.write(a_c)
        archivo_t.write(",")
        archivo_t.write(b)
        archivo_t.write(",")
        archivo_t.write(n_s)
        archivo_t.write(",")
        archivo_t.write(p_s)
        archivo_t.write("\n")
        
cobrar("39909651","Peinado")
    
        
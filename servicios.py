#servicios
def ver_precios():
    with open("Servicios.txt","r") as archivo:
       print(archivo.read())
    
def agregar_serv(nombre,precio):
    with open("Servicios.txt","a") as archivo:
        archivo.write(nombre)
        archivo.write(",")
        archivo.write(precio)
        archivo.write("\n")

def modif_precio(servicio, precio):
    with open("Servicios.txt", "r") as archivo:
        lineas = archivo.readlines() #Lee el txt

    with open("Servicios.txt", "w") as archivo: #modo escritura
        for i in lineas: #itera cada registro/linea del txt.
            #print("iteracion",i) -- Imprime cada registro tal cual el txt
            a = i.strip().split(",") #cada linea va a eliminar espacios y separarlos por comas- convierte cada registro en lista y asi poder ubicar index
            #print(a) -- Conviete los registros en listas separados por las comas.
            if a[0] == servicio: #condicional
                a[1] = precio #replace
            archivo.write(",".join(a) + "\n") #reescribe el registro, manteniendo los registros existentes
            
def eliminar_serv(servicio):
    reg = []
    with open("Servicios.txt","r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            e = i.strip().split(",")
            if e[0] != servicio:
                reg.append(i)
    with open("Servicios.txt","w") as archivo:
        archivo.writelines(reg)
                
  
eliminar_serv("Secado")  


#modif_precio("Peinado","9000")
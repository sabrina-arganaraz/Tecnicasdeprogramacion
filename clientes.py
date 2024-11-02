#clientes
def alta_cliente(nom,ape,dni,tel,dire):
    if buscar_cliente(dni) == False:
        with open("Clientes.txt","a") as archivo:
            archivo.write(nom)
            archivo.write(",")
            archivo.write(ape)
            archivo.write(",")
            archivo.write(dni)
            archivo.write(",")
            archivo.write(tel)
            archivo.write(",")
            archivo.write(dire)
            archivo.write("\n")
    else:
        print("El cliente ya existe en la bbdd")


def ver_clientes():
    with open("Clientes.txt","r") as archivo:
       print(archivo.read())

def modif_datos(dni,opcion,new_dato): # 1 para telefono , 
    with open("Clientes.txt","r") as archivo:
        lineas = archivo.readlines()

    with open("Clientes.txt","w") as archivo:
        for i in lineas:
            a = i.strip().split(",") #separado por coma, convertido en lista
            if dni == a[2]:
                 if opcion == 1: #modifica telefono
                     a[3] = new_dato
                 elif opcion == 2: #modifica direccion
                     a[4] = new_dato
            archivo.write(",".join(a) + "\n")

def buscar_cliente(dni):
    with open("Clientes.txt", "r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            a = i.strip().split(",")
            if dni == a[2]:
                #print(a)
                return True
    return False

def modif_estado(dni):
    with open("Clientes.txt","r") as archivo:
        lineas = archivo.readlines()
    with open("Clientes.txt","w") as archivo:
        for i in lineas:
            a = i.strip().split(",")
            if dni == a[2]:
                if a[5] == 'A':
                    a[5] = 'B'
                else:
                    a[5] = 'A'
            archivo.write(",".join(a) + "\n")    
        
modif_estado("39909651")               


#buscar_cliente("454545")
#alta_cliente("Rosa","Casco","77777777","4564545","45d45asd4s5a")


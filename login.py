
def login(dni,contra):
    with open ("Usuarios.txt","r") as archivo:
        lineas = archivo.readlines()
        cont = 0
        for i in lineas:
            a = i.strip().split(",")
            if dni == a[2] and contra == a[5]:
                cont = cont +1
        if cont == 1:
            return True 
        else:
            return False
        
def registrar(nom,ape,dni,tel,rol,pasw):
    with open("Usuarios.txt","r") as archivo:
        lineas = archivo.readlines()
        cont = 0
        for i in lineas:
            a = i.strip().split(",")
            if a[2] != dni:
                cont = cont + 1
        if cont >= 1:
            with open("Usuarios.txt","a") as archivo:
                archivo.write(nom)
                archivo.write(",")
                archivo.write(ape)
                archivo.write(",")
                archivo.write(dni)
                archivo.write(",")
                archivo.write(tel)
                archivo.write(",")
                archivo.write(rol)
                archivo.write(",")
                archivo.write(pasw)
                archivo.write("\n")
        else:        
            return False

def acceso(dni):
    with open("Usuarios.txt","r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            a = i.strip().split(",")
            if login(dni) == True:
                if a[4] == 'admin':
                    return True
    return False
                




        
                

                
        
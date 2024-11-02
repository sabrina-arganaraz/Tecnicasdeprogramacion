"""contenido_usuarios : nombre,apellido,dni,tel,rol,pass
Contendio_serivicios : servicio,precio
Contenido_cliente : nombre,apellido,dni,tel,domicilio
contenido_transacciones : codigo,fecha,cliente,servicio,precio
"""
cont_usuarios = "Susana,Gimenez,04236985,1135897458,admin,1234\nRoman,Gutierrez,36569856,1125369851,cajero,6789\n"
cont_servicios = "Corte de pelo,4500\nTintura,3000\nPlanchita,6000\nSecado,5000\nPeinado,15000\n"
cont_cliente = "Sabrina,Arganaraz,35971776,1149896145,Cordoba 1468,A\nCarlos,Estigarribia,24676997,1165733934,Directorio 596,A\nJulieta,Casco,39909651,1136241814,Ramon Falcon 4658,A\n"

def crear_archivo(txt):
    with open (txt , "x") as archivo:
        archivo.read

crear_archivo("Usuarios.txt")
crear_archivo("Servicios.txt")
crear_archivo("Clientes.txt")
crear_archivo("Transacciones.txt")

def escribir(nombre,contenido):
    with open(nombre,"w") as archivo:
        archivo.write(contenido)

escribir("Usuarios.txt",cont_usuarios)
escribir("Servicios.txt",cont_servicios)
escribir("Clientes.txt",cont_cliente)






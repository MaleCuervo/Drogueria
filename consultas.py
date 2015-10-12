#encoding: latin1

import csv
import sys

def obtener_indice(headers, nombre_indice):
    """ funcion de obtener indice para evitar tener que hacerlo cada vez que se necesita saber un header especifico,
        recibe lista a iterear y nombre buscado, devuelve numero de posicion""" 
    indice = 0

    for idx, row in enumerate(headers):
        if row == nombre_indice:
            indice = idx
            break

    return indice

def obtener_reader(archivo):
    """ funcion que resetea el puntero interno del reader a la posicion inicial y lee el archivo indicado """
    archivo.seek(0)
    return csv.reader(archivo)

#función hecha por M.Alejandra y Eliana
def cargar_archivo(nombre_archivo):
    ''' Recibe el nombre de un archivo y:
        •Chequea que el archivo exista,
        •Que sea de extensión csv,
        •Que algún registro tenga una cantidad inválida de campos,
        •Que algún campo de CODIGO no sea vacío,
        •Que algún campo de CANTIDAD no contenga un número entero, 
        •Que algún campo de PRECIO no contenga un valor decimal FALTA
    '''
    
    #chequea que el archivo exista,trata de abrir el archivo, si no puede devuelve error y sale del programa 
    try:
        archivo = open(nombre_archivo)

    except IOError:
        print ("No se pudo leer el archivo", nombre_archivo,", chequee que el mismo exista")
        sys.exit()

    #de existir el archivo ...
    if nombre_archivo.lower().endswith('.csv'):
        archivo_csv = obtener_reader(archivo)
        headers = next(archivo_csv)

        #encuentro los indices de los headers que voy a tener que validar
        campo_codigo = obtener_indice(headers, "CODIGO")
        campo_cantidad = obtener_indice(headers, "CANTIDAD")
        campo_precio = obtener_indice(headers, "PRECIO")

        #por cada fila de la lista
        for row in archivo_csv:
            #Si la cantidad de valoren en una fila es menor o mayor a la cantidad de headers pasados
            if len(row) < len(headers):
                raise ValueError ("Falta un registro en la fila:", row)
            elif len(row) > len(headers):
                raise ValueError ("Sobran valores en la fila:", row)

            #chequea que el campo codigo no sea vacio
            if not row[campo_codigo]:
                raise ValueError ("Falta valor para la columna codigo en la fila", row)

            #chequea que el campo cantidad sea un entero 
            try:
                row[campo_cantidad] = int(row[campo_cantidad])
            except:
                raise ValueError ("La cantidad no puede ser decimal ni un texto", row)

            #chequea que el campo precio pueda ser un numero decimal
            try:
                row[campo_precio] = float(row[campo_precio])
            except:
                raise ValueError ("El precio no puede ser una cadena de texto", row)

        return archivo

    #sino devuelve error de extension   
    else:
        raise RunnableException ("Debe cargar un archivo con extension csv")

def obtener_clientes_con_nombre_incompleto(archivo, nombre_cliente_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de cliente 
    incompleto, devuelve una lista con todos los nombres de clientes sin 
    repetir (obtenidos de la columna CLIENTE del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''
    #lee el archivo dado
    archivo_csv = obtener_reader(archivo)

    headers = next(archivo_csv)
    campo_cliente = obtener_indice(headers, "CLIENTE")
    nombre_cliente_buscado = []

    #recorre los datos 
    for row in archivo_csv:

        #si el nombre incompleto se encuentra en el valor de la columna cliente
        if nombre_cliente_incompleto in row[campo_cliente]:
            
            #Si ese nombre no fue incluido en la lista lo agregega, sino no
            if row[campo_cliente] not in nombre_cliente_buscado:
                nombre_cliente_buscado.append(row[campo_cliente])

    if len(nombre_cliente_buscado) == 0:
        raise ValueError("No se encontro ningun registro con ese nombre")

    else:
        #devuelve lista final con todos los posibles nombres
        return nombre_cliente_buscado


def obtener_productos_con_nombre_incompleto(archivo, nombre_producto_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de producto 
    incompleto, devuelve una lista con todos los nombres de productos sin 
    repetir (obtenidos de la columna PRODUCTO del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''                            
    #lee el archivo dado
    archivo_csv = obtener_reader(archivo)

    headers = next(archivo_csv)
    campo_producto = obtener_indice(headers, "PRODUCTO")
    nombre_producto_buscado = []

    #recorre los datos 
    for row in archivo_csv:

        #si el nombre incompleto se encuentra en el valor de la columna producto
        if nombre_producto_incompleto in row[campo_producto]:
            
            #Si ese nombre no fue incluido en la lista lo agregega, sino no
            if row[campo_producto] not in nombre_producto_buscado:
                nombre_producto_buscado.append(row[campo_producto])

    if len(nombre_producto_buscado) == 0:
        raise ValueError("No se encontro ningun registro con ese nombre")

    else:
        #devuelve lista final con todos los posibles nombres
        return nombre_producto_buscado
    
    
def obtener_productos_comprados_por_cliente(archivo, nombre_cliente):
    ''' Dado el contenido del archivo de datos y el nombre de un cliente, 
    devuelve una lista de todos los nombres de productos comprados por
    el cliente, sin repetir.
    '''
    raise NotImplementedError
   
     

def obtener_clientes_de_producto(archivo, nombre_producto):
    ''' Dado el contenido del archivo de datos y el nombre de un producto, 
    devuelve una lista de todos los compradores del producto, sin repetir.
    '''
  
    
    raise NotImplementedError
    
    
    
def obtener_productos_mas_vendidos(archivo, cantidad_maxima_productos):
    ''' Devuelve una lista de tuplas de tamaño pasado por parámetro que 
    representan los productos más vendidos, conteniendo como primer elemento 
    el nombre del producto y como segundo elemento la cantidad de ventas. 
    '''
    
    
    
    raise NotImplementedError
    

def obtener_clientes_mas_gastadores(archivo, cantidad_maxima_clientes):
    ''' Devuelve una lista de tuplas de tamaño pasado por parámetro que 
    representan los clientes que más gastaron, conteniendo como primer 
    elemento el nombre del cliente y como segundo elemento el monto gastado.   
    '''
   
    
    raise NotImplementedError 


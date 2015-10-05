#encoding: latin1

import csv
import sys

#función hecha por M.Alejandra y Eliana
def cargar_archivo(nombre_archivo):
    ''' Recibe el nombre de un archivo, chequea que exista y que sea un csv y devuelve un diccionario 
    con su contenido. 
        En caso de error levanta una RunnableException con un mensaje 
    descriptivo.'''
    
    #chequea que el archivo exista,trata de abrir el archivo, si no puede devuelve error y sale del programa 
    try:
        archivo = open(nombre_archivo)

    except IOError:
        print ("No se pudo leer el archivo", nombre_archivo,", chequee que el mismo exista")
        sys.exit()

    #de existir el archivo ...
    with archivo:
        #chequea que sea una extensión válida y abre y lee el archivo, devuelve un diccionario
        if nombre_archivo.lower().endswith('.csv'):
            archivo = open(nombre_archivo)  
            archivo_csv = csv.DictReader(archivo) 
            #for row in archivo_csv:
            #    print(row)
            return archivo_csv

        #sino devuelve error de extension   
        else:
            raise RunnableException ("Debe cargar un archivo con extension csv")
        
 

def obtener_clientes_con_nombre_incompleto(archivo, nombre_cliente_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de cliente 
    incompleto, devuelve una lista con todos los nombres de clientes sin 
    repetir (obtenidos de la columna CLIENTE del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''
    nombre_cliente_buscado = []
    #recorre el diccionario por fila
    for row in archivo:
        #si el nombre incompleto se encuentra en el valor de la columna cliente
        if nombre_cliente_incompleto in row["CLIENTE"]:
            #Si ese nombre no fue incluido en la lista lo agregega, sino no
            if row["CLIENTE"] not in nombre_cliente_buscado:
                nombre_cliente_buscado.append(row["CLIENTE"])

    if len(nombre_cliente_buscado) == 0:
        #falta hacer el error
        raise ValueError("No se encontró ningún registro con ese nombre")

    else:
        #devuelve lista final con todos los posibles nombres
        #print(nombre_cliente_buscado)
        return nombre_cliente_buscado
    



def obtener_productos_con_nombre_incompleto(archivo, nombre_producto_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de producto 
    incompleto, devuelve una lista con todos los nombres de productos sin 
    repetir (obtenidos de la columna PRODUCTO del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''                            
                        # si no esta el elemento me devuelve un mensaje
            
    raise NotImplementedError
    
     
    
    
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
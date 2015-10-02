#encoding: latin1

import csv
import sys

def cargar_archivo(nombre_archivo):
    ''' Recibe el nombre de un archivo, chequea que exista y que sea un csv y devuelve un diccionario 
    con su contenido. 
        En caso de error levanta una RunnableException con un mensaje 
    descriptivo.'''
    
    #chequea que el archivo exista,trata de abrir el archivo, si no puede devuelve error y sale del programa 
    try:
        archivo = open(nombre_archivo)

    except IOError:
        print "No se pudo leer el archivo", nombre_archivo,", chequee que el mismo exista"
        sys.exit()

    #de existir el archivo ...
    with archivo:
        #chequea que sea una extensión válida y abre y lee el archivo, devuelve un diccionario
        if nombre_archivo.lower().endswith('.csv'):
            archivo = open(nombre_archivo)  
            archivo_csv = csv.DictReader(archivo) 
            return (archivo_csv)

        #sino devuelve error de extension   
        else:
            raise RunnableException ("Debe cargar un archivo con extension csv")
        
 

def obtener_clientes_con_nombre_incompleto(archivo, nombre_cliente_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de cliente 
    incompleto, devuelve una lista con todos los nombres de clientes sin 
    repetir (obtenidos de la columna CLIENTE del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''
    #esta buscando en la lista por nombre incompleto
    for row in archivo: 
        #regresa lista con el indice del nombre
        #return ("CLIENTE") 

     # si no esta el elemento me devuelve un mensaje                                    
    else:                                                  
        return ("no esta su nombre")
    
    raise NotImplementedError
    



def obtener_productos_con_nombre_incompleto(archivo, nombre_producto_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de producto 
    incompleto, devuelve una lista con todos los nombres de productos sin 
    repetir (obtenidos de la columna PRODUCTO del archivo) cuyo nombre 
    contenga la cadena incompleta pasada por parámetro.
    '''                            
                             
    nombre_producto_incompleto = raw_input()
    
    for nombre_producto_incompleto in archivo:                  #esta buscando en la lista por nombre imcompleto
        return ("PRODUCTO")                                      #regresa lista con el indice del nombre 
    else:                                                    
        return ("no existe el producto")                         # si no esta el elemento me devuelve un mensaje
            
    raise NotImplementedError
    
     
    
    
def obtener_productos_comprados_por_cliente(archivo, nombre_cliente):
    ''' Dado el contenido del archivo de datos y el nombre de un cliente, 
    devuelve una lista de todos los nombres de productos comprados por
    el cliente, sin repetir.
    '''
    archivo =  open("./archivos_prueba/archivo_valido_1.csv") 
    archivo1 =  open("./archivos_prueba/archivo_valido_2.csv") 
 
    
    nombre_cliente = raw_input() 
    
    
    for nombre_cliente in archivo,archivo1:                                       #busca en lista
        return ("PRODUCTO")    #regresa lista
         
    
    raise NotImplementedError
   
     

def obtener_clientes_de_producto(archivo, nombre_producto):
    ''' Dado el contenido del archivo de datos y el nombre de un producto, 
    devuelve una lista de todos los compradores del producto, sin repetir.
    '''
  
    nombre_producto =  raw_input()
    
    for nombre_producto in archivo,archivo1:                                       #busca en lista
        return ("CLIENTE")                                                  #regresa lista
    
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
    

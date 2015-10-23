#encoding: latin1

import time
import os

def obtener_nombre_archivo():
    ''' Devuelve una cadena con el nombre de archivo de salida con el 
    formato resultados_MMDD_HHSSMM.txt, correspondiente a la fecha y hora
    actual del sistema.
    '''
    
    return "resultados_" + time.strftime("%m%d_%H%M%S") + ".txt"
        
        
def exportar_resultados(resultados, cabecera, descripcion):
    ''' Graba en un archivo una descripción de la consulta realizada y los 
    resultados en forma tabulada, agregando la cabecera correspondiente.
        Descripción debe ser una cadena descriptiva de la consulta 
    realizada. Cabecera debe ser una tupla con el contenido de cada columna
    que va a tener la tabla de salida. Resultados debe ser una lista de 
    tuplas.
        Devuelve el nombre del archivo que se grabó.   
    '''
    archivo_nuevo = open(obtener_nombre_archivo(), 'a')
    #archivo_nuevo.write(descripcion)
    #for t in cabecera:
    #    archivo_nuevo.write(t + '\n')
    #archivo_nuevo.writelines(cabecera) 
    #archivo_nuevo.writelines(resultados)  
    archivo_nuevo.close()

    return obtener_nombre_archivo()
    #raise NotImplementedError
        

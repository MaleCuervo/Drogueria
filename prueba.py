#!/usr/bin/env python
# encoding: utf-8

import consultas

archivo = "prueba.csv"

archivo_abierto = consultas.cargar_archivo(archivo)

res_1 = consultas.obtener_clientes_con_nombre_incompleto(archivo_abierto,"C") #C0, C2,C9
print(res_1)

res_2 = consultas.obtener_productos_con_nombre_incompleto(archivo_abierto,"P") #P1,P2, p3
print(res_2)

res_3 = consultas.obtener_productos_comprados_por_cliente(archivo_abierto,"C0") #P1, P3
print(res_3)

res_4 = consultas.obtener_clientes_de_producto(archivo_abierto,"P2") #C2, C9
print(res_4)

res_5 = consultas.obtener_productos_mas_vendidos(archivo_abierto, 4) #p1,P2,P3,23
print(res_5)

res_6 = consultas.obtener_clientes_mas_gastadores(archivo_abierto, 4)#C0,C9,C2
print(res_6)

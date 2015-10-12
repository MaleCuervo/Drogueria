#!/usr/bin/env python
# encoding: utf-8

import consultas

archivo = "prueba.csv"

archivo_abierto = consultas.cargar_archivo(archivo)

consultas.obtener_clientes_con_nombre_incompleto(archivo_abierto,"P4")

consultas.obtener_productos_con_nombre_incompleto(archivo_abierto,"P4")


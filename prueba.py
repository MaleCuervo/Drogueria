#!/usr/bin/env python
# encoding: utf-8

import consultas

archivo = "prueba.csv"

consultas.cargar_archivo(archivo)

consultas.obtener_clientes_con_nombre_incompleto(archivo,"C1")
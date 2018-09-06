#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Monitor de Recursos
#
# Simple monitor de recursos escrito en Python
#
# Humberto Alcocer <humbertowoody@gmail.com>

# Librerías de uso para acceder a los datos del sistema.
import platform, psutil, multiprocessing, time

# Esta función proporciona los datos básicos de la instalación del
# Sistema Operativo
def datos_so():
	print '·Sistema Operativo'
	print "\t-Tag del Sistema: %s" % platform.platform()
	pass

# Esta función deberá proporcionar los datos básicos del procesador
# como modelo, velocidad y número de cores (entre otros)
def datos_procesador():
	print '·Procesador'
	print "\t-Arquitectura del Procesador: %s" % platform.processor()
	print "\t-Uso del procesador: %d%%" % psutil.cpu_percent()
	print "\t-Número de Cores: %s" % multiprocessing.cpu_count()
	pass

# Esta función provee la información básica acerca del Disco Duro
def datos_hdd():
	print '·Disco Duro'
	print "\t-Porcentaje de uso: %d%%" % psutil.disk_usage('/')[3]
	pass

# Esta función proporciona la información básica del estado actual
# de la memoria de acceso aleatorio
def datos_ram():
	print '·RAM (Memoria de Acceso Aleatorio)'
	print "\t-Porcentaje de uso: %d%%" % psutil.virtual_memory()[2]
	pass

# Función principal
def main():
	print '\t##################################'
	print '\t# Información básica del sistema #'
	print '\t#--------------------------------#'
	print '\t#   Presione Ctrl+C para salir   #'
	print '\t##################################'
	print '--------------------------------------------------------------'
	try:
		while 1:
			datos_so() # Muestra datos del Sistema Operativo.
			datos_procesador() # Muestra datos del Procesador.
			datos_ram() # Muestra datos de la memoria RAM.
			datos_hdd() # Muestra datos del Disco Duro.
			# Pausa de 2 segundos
			time.sleep(2)
			print '--------------------------------------------------------------'
			pass
	except:
		print '\n\t####################'
		print '\t# Fin del Programa #'
		print '\t####################'
	pass

# Redirección a la función principal
if __name__ == '__main__':
	main()

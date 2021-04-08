import os

prosat1 = {}
prosat2 = {}

while True:
	print ()
	print ("1.- Wireless Pro SAT 1")
	print ("2.- Wireless Pro SAT 2")
	print ("3.- Resultados para CLI")
	print ("4.- Salir")
	print ()
	try:
		opcion = int (input("Selecciona una opción: "))
		print ()

		if opcion == 1:
			name = input ("Nombre del Proveedor: ")
			mac = input ("mac address: ")
			ip = input ("ip: ")
			prosat1 [mac,name,ip] = ip
			os.system("clear")
			print ("(Ok ...)")

		elif opcion == 2:
			name = input ("Nombre del Proveedor: ")
			mac = input ("mac address: ")
			ip = input ("ip: ")
			prosat2 [mac,name,ip] = ip
			print ()
			os.system("clear")
			print ("(Ok ...)")

		elif opcion == 3:
			os.system("clear")
			print ("\nOutput para WLC:\n")
			print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
			for mac,name,ip in prosat1:
				print (f"config macfilter delete {mac.lower()}")
				print (f'config macfilter add {mac.lower()} 7 sso3_cpn "{name.title()}" {ip}')
			for mac,name,ip in prosat2:
				print (f"config macfilter delete {mac.lower()}")
				print (f'config macfilter add {mac.lower()} 18 sat_509 "{name.title()}" {ip}')
			print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

		elif opcion == 4:
			os.system("clear")
			break

		else:
			os.system("clear")
			print ("\nOpcion no válida")

	except ValueError:
			os.system("clear")
			print ("\nOpcion no válida")


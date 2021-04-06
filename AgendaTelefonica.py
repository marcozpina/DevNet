agenda_telefonica = {}

while True:
    print ()
    print ("-------- .: Menu :. --------\n")
    print ("1.- Ingresar nuevo contacto\n")
    print ("2.- Eliminar contacto\n")
    print ("3.- Consultar contactos\n")
    print ("4.- Salir del programa\n")

    select = int (input("Selecciona una opcion: "))
    print ()
   

    if select == 1:
        name = str  (input("Nombre: "))
        #last = str (input("Apellido: "))
        phone = input ("Telefono: ")
        print ()

        if name not in agenda_telefonica:
            agenda_telefonica [name] = phone
            print (" -- Contacto agregado correctamente --\n")

    elif select == 2:
        name = input ("Selecciona el nombre que quieres eliminar: ")
        if name in agenda_telefonica:
            del (agenda_telefonica [name])
            print ("Contacto eliminado correctamente\n")
        else:
            print ("Este contacto no existe")
    
    elif select == 3:
        if name in agenda_telefonica:
            for name,phone in agenda_telefonica.items():
                print ("Estos son todos los contactos: \n")
                print (f"Nombre: {name}, Telefono: {phone}")
        else:
            print ("No hay contactos aún")
    
    elif select == 4:
        print (" .: Hasta pronto :. \n")
        break
    
    else:
        print ("Opcion inválida")
    


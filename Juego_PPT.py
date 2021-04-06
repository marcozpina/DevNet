print ()
print (".: Juego de 'Piedra' 'Papel' o 'Tijera' :.")
print ()

print ("(1) Piedra (2) Papel (3) Tijera")
print ()

while True:

    p1 = int (input("Jugador 1: Selecciona una opcion: "))
    p2 = int (input("Jugador 2: Selecciona una opcion: "))

    if p1 == p2:
        print ("Hay un empate")
    elif p1 == 1 and p2 == 2:
        print ("Juagador 2 Gana!")
        print ()
    elif p1 == 1 and p2 == 3:
        print ("Jugador 1 Gana!")
        print ()
    elif p1 == 2 and p2 == 1:
        print ("Jugador 1 Gana!")
        print ()
    elif p1 == 2 and p2 == 3:
        print ("Jugador 2 Gana!")
        print ()
    print ()

    ask = input ("¿Deseas seguir Jugando? SI = 1 / NO = 2: ")
    if ask == 1:
        break 

print ()
print (".: Hasta Pronto :.")


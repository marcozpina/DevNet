cadena = input("Ingresa una serie de numeros de solo un digíto para saber si es un Palíndromo:  ")
cadena2 = cadena [::-1] # [::-1] Es un mecanismo que permite hacer una reversa.
if cadena == cadena2:
    print ("La serie numerica SI es un Palíndromo")
else:
    print ("La sereie numerica NO es un Palíndromo")
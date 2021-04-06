from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
page = requests.get (url)
soup = BeautifulSoup (page.content, "html.parser")

# Equipos 

eq = soup.find_all  ("span", class_="nombre-equipo")

# print (eq) # Imprime todo lo que tiene en esa clase

equipos = list ()

count = 0

for i in eq:
    if count < 20: # Sin esto, se mostrarian todos los nombres de la pagina. Esto lo limita a 20
        equipos.append(i.text) # Con el Metodo append, se le agrega un elemento a la lista
    else:                      # Con el .text selecciona solo el "texto" de las etiquetas
        break
    count += 1 # El contador inicia en "0" y con este va incrementando en "1" la lista

# Puntos

pt = soup.find_all  ("td", class_="destacado")

puntos = list ()

count = 0

for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1

# Creacion de un "Data Frame"

df = pd.DataFrame ({"Nombre" : equipos, "  Puntos" : puntos}, index = list (range(1,21)))
print (df)
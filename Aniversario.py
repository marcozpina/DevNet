print ()
fechas = {"Marcos / Adriana" : "13/Sep/2016",
          "Edgar / Angelica" : "09/Dic/2019",
          "Mario / Ely" : "12/Dic/2017"
          }
for i in fechas:
    print (i)
print ()
ask = input (".:Fechas de Aniversario de Bodas. Escribe una opción: ")
print ()
if ask in fechas:
    print ("El aniversario de bodas de {} es:".format(ask))
    print (fechas[ask])
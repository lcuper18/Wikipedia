from Consulta_wikipedia import buscar_informacion
from Consulta_google import buscar_Bibliografia
print("A continuacion una app para buscar en wikipedia")
consulta = input("Ingresa el tema que deseas buscar: \n")
buscar_informacion(consulta)
print("")
print("Bibliografia:\n")
buscar_Bibliografia(consulta)
#que quede en formato APA
#y que todo quede en un pdf

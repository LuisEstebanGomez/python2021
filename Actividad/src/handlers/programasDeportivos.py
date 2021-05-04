import csv
from src.handlers import guardarDeportes 

def deportesEnPlazas():
        archivo = open ("src/programas-deportivos.csv", "r")
        csvreader=csv.reader(archivo, delimiter=',')

        encabezado=next(csvreader)


        texto=""

        for linea in csvreader:
            print(linea[4])
            if linea[4] == "Actividades deportivas en Plazas":
                texto = texto + linea[5] + "\n"
                guardarDeportes.guardarDeportes(linea[5])
        return texto        
      

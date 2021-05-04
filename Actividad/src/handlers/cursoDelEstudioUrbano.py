import csv
from src.handlers import guardarEstudio
def estudioUrbano():
        archivo = open ("src/cursos-del-estudio-urbano.csv", "r")
        csvreader=csv.reader(archivo, delimiter=';')

        encabezado=next(csvreader)


        texto=""

        for linea in csvreader:
            
            if linea[8] == "MARTES" or linea[8] == "MIERCOLES" or linea[8] == "JUEVES" :
                texto = texto + linea[4] + "\n"
                guardarEstudio.guardarEstudios(linea[4])
        return texto        
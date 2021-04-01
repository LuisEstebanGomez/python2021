nombres="""'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'"""

eval1= """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""
eval2="""30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""


#ACA SACO LOS CARACTERES Y SALTOS DE LINEA QUE NO HABIA ECHO POR QUE HABIA COPIADO MAL EL STRING DE LOS NOMBRES 
nombres = nombres.replace("'", '')
nombres = nombres.replace("\n",'')
#Creo las listas
lista_nombres=nombres.split(",")
lista_eval1=eval1.split(",")
lista_eval2=eval2.split(",")

#Creo la estructura con nombre y la suma de sus dos notas 
i=0
estructura=[]
for n in lista_nombres:
    estructura.append([n,int(lista_eval1[i])+int(lista_eval2[i])])
    i+=1

#Calculo la nota promedio
sum=0
for dato in estructura:
    sum += dato[1]

print(f"Nota promedio : {sum/len(estructura)}")   

#Imprimo nombre de alumnos que su nota esta por debajo del promedio
for dato in estructura:
    if dato[1] < sum/len(estructura):
        print(f" -El alumno: {dato[0]} con nota: {dato[1]} esta por debajo del promedio")

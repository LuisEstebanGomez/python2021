nombre = input("Ingrese Nombre Alumno (<fin> para finalizar)")
notas=[]
suma=0
while nombre != "fin":
    nota = int(input("Ingrese una nota: "))
    suma = suma + nota
    notas.append([nombre, nota])
    nombre = input("Ingrese Nombre Alumno (<fin> para finalizar)")
    


promedio=suma/len(notas)
print(promedio)
cant=0
for x in notas:
    if(x[1] < promedio):
        print(f"{x[0]} tiene nota menor al promedio")

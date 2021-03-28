nota = int(input("Ingrese una nota (-1 para finalizar)"))
notas=[]
suma=0
while nota != -1:
    suma = suma + nota
    notas.append(nota)
    nota = int(input("Ingrese una nota (-1 para finalizar)"))

promedio=suma/len(notas)

cant=0
for x in notas:
    if(nota < promedio):
        cant += 1

print(f"El promedio es: {promedio}")        
print(f"La cantidad de notas bajo el primedio es: {cant}")
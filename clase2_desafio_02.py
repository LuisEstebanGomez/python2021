cadena=input("Ingrese una palabra: <Para salir ingrese fin>")
while (cadena != "fin" ):
    if cadena[len(cadena)-1] == cadena[0]:
        print(f"PALABRA CAPICUA: {cadena}")
    cadena=input("Ingrese una palabra: <Para salir ingrese fin>")

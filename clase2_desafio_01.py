'''for i in range(4):
    cadena=input("Ingresá una palabra")
    if "r" in cadena:
        print(f"{cadena} tiene una letra r")
    else:
        print(f"{cadena} no tiene una letra r")  
'''
for i in range(4):
    cadena=input("Ingresa una palabra: ")
    mensaje = "TIENE R" if "r" in cadena else "NO TIENE R"
    print(mensaje)          
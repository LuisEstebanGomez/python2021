import PySimpleGUI as sg
from src.windows import ventana1
from src.handlers import programasDeportivos

def start():
    #Ejecuta la ventana principal

    ventana1_window=loop()

    ventana1_window.close()

def loop():
        #loop de la pantalla principal
        texto = programasDeportivos.deportesEnPlazas()

        ventana1_window = ventana1.build(texto)

        while True: 
                event, _values= ventana1_window.read()
               
                if event in (sg.WIN_CLOSED, 'Exit','-EXIT-'):
                        break
                if event == '-LOGOUT-':
                        break    
        
        return ventana1_window  
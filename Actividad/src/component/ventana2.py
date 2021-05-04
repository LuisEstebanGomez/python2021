import PySimpleGUI as sg
from src.windows import ventana2
from src.handlers import cursoDelEstudioUrbano

def start():
    #Ejecuta la ventana principal

    ventana2_window=loop()

    ventana2_window.close()

def loop():
        #loop de la pantalla principal
        texto = cursoDelEstudioUrbano.estudioUrbano()
        ventana2_window = ventana2.build(texto)

        while True: 
                event, _values= ventana2_window.read()
               
                if event in (sg.WIN_CLOSED, 'Exit','-EXIT-'):
                        break
                if event == '-LOGOUT-':
                        break    
        
        return ventana2_window  
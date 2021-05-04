import PySimpleGUI as sg
from src.windows import principal
from src.component import ventana1
from src.component import ventana2
from src.handlers import programasDeportivos
from src.handlers import cursoDelEstudioUrbano

def start():
    #Ejecuta la ventana principal

    principal_window=loop()

    principal_window.close()

def loop():

        principal_window=principal.build()

        #loop de la pantalla principal
        while True: 
                event, _values= principal_window.read()
                if event == "-DATA1-":
                        principal_window.hide()
                        ventana1.start()
                        principal_window.un_hide()
                if event == "-DATA2-":
                        principal_window.hide()
                        ventana2.start()
                        principal_window.un_hide()
                if event in (sg.WIN_CLOSED, 'Exit','-EXIT-'):
                        break
                if event == '-LOGOUT-':
                        break    
        return principal_window                    
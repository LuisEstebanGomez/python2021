import PySimpleGUI as sg

def build(texto):

    layout=[[sg.Text(texto)],
        [sg.Button("SALIR",size=(50,2),key='-LOGOUT-')]    ]  

    ventana2_window = sg.Window('Curso del estudio Urbano CABA').layout(layout)

    return ventana2_window  
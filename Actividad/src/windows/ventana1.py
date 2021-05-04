import PySimpleGUI as sg

def build(texto):

    layout=[[sg.Text(texto)],
        [sg.Button("SALIR",size=(50,2),key='-LOGOUT-')]    ]  

    ventana1_window = sg.Window('Cursos Estudio Urbano CABA').layout(layout)

    return ventana1_window  
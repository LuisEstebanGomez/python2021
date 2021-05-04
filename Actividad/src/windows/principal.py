import PySimpleGUI as sg

def build():

    layout=[[sg.Button("Actividades deportivas en Plazas CABA",size=(50,2),key='-DATA1-')],
             [sg.Button("Cursos de estudio Urbano CABA ",size=(50,2),key='-DATA2-')],
             [sg.Button("SALIR",size=(50,2),key='-LOGOUT-')],   
    
    ]  
    
    principal_window = sg.Window('Actividad').layout(layout)
    return principal_window  
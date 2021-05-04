import json

def guardarEstudios(values):
    users_data = {'Estudios': values}
    user = [users_data]
    try:
        with open('src/EstudiosCaba.json', 'r') as archivo:
            users_json = json.load(archivo)
        user.extend(users_json)
    except FileNotFoundError:
        print('Archivo no encontrado.')
    with open('src/EstudiosCaba.json', 'w') as archivo:
        json.dump(user, archivo)
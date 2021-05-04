import json

def guardarDeportes(values):
    users_data = {'sport': values}
    user = [users_data]
    try:
        with open('src/deportesCaba.json', 'r') as archivo:
            users_json = json.load(archivo)
        user.extend(users_json)
    except FileNotFoundError:
        print('Archivo no encontrado.')
    with open('src/deportesCaba.json', 'w') as archivo:
        json.dump(user, archivo)
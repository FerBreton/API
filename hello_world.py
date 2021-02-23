from flask import Flask, jsonify
import requests

app = Flask(__name__)

alumnos = [
    {
        'id': 1,
        'nombre': 'Maria Fernanda',
        'ap_p': 'Breton',
        'ap_m': 'Quintero',
        'asistencia': True
    },
    {
        'id': 2,
        'nombre': 'Diego',
        'ap_p': 'Vega',
        'ap_m': 'De Ita',
        'asistencia': True
    },
    {
        'id': 3,
        'nombre': 'Luis Alejandro',
        'ap_p': 'Pinot',
        'ap_m': 'Campos',
        'asistencia': False
    }
]

@app.route('/')
def hello_world():
    return "Hola clase"

@app.route('/api/alumnos', methods = ['GET'])
def get_alumnos():
    return jsonify({'alumnos': alumnos})

@app.route('/api/pokemon', methods = ['GET'])
def get_pokemon():
    poke = 'https://pokeapi.co/api/v2/type'
    response = requests.get(poke)
    json_response = response.json()
    return json_response


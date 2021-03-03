from flask import Flask, jsonify, abort, request
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("firebase-adminsdk.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-api-6566f-default-rtdb.firebaseio.com/'
})

print(default_app)

ref = db.reference('/')

ref.set({
    'tasks': {
        '1':{
            'name': 'Ir a bañarse',
            'check': False
        },
        '2':{
            'name': 'Estudiar para los parciales',
            'check': False
        }
    }
})

task_ref = ref.child('tasks/1')
task_ref.update({
    'check': True
})

task_ref.delete()
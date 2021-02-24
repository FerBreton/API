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

tasks = [
    {
        'id': 1,
        'name': 'Ir a bañarse',
        'check': False
    },
    {
        'id': 2,
        'name': 'Estudiar para los parciales',
        'check': False
    }
]

ref.set(tasks)

@app.route('/')
def hello_world():
    return "API de un TO-DO List"

@app.route('/api/tasks', methods = ['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/api/tasks/<int:id>', methods = ['GET'])
def get_task(id):
    '''this_task = 0
    for task in tasks:
        if task['id'] == id:
            this_task = task'''

    this_task = [task for task in tasks if task['id'] == id]

    if len(this_task) == 0:
        abort(404)

    return jsonify({'task':this_task[0]})

@app.route('/api/tasks', methods = ['POST'])
def create_task():
    if not request.json:
        abort(404)
    
    task = {
        'id': len(tasks) + 1,
        'name': request.json['name'],
        'check': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    this_task = [task for task in tasks if task['id'] == task_id]
    if len(this_task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'check' in request.json and type(request.json['check']) is not bool:
        abort(400)
    
    this_task[0]['name'] = request.json.get('name', this_task[0]['name'])
    this_task[0]['check'] = request.json.get('check', this_task[0]['check'])

    return jsonify({'task': this_task[0]})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    
    task.remove(task[0])

    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
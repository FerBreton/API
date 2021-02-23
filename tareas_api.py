from flask import Flask, jsonify, abort, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
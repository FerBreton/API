import os
from flask import Flask, request, jsonify, abort
from firebase_admin import credentials, db, initialize_app


app = Flask(__name__)

cred = credentials.Certificate('firebase-adminsdk.json')
default_app = initialize_app(cred, {
    'databaseURL': 'https://test-api-6566f-default-rtdb.firebaseio.com/'
})

ref = db.reference('tasks')
#READ
@app.route('/tasks', methods=['GET'])
def read():
    try:
        task_id = request.args.get('id')
        if task_id:
            task = ref.child(task_id)
            return jsonify(task.get()), 200
        else:
            tasks = ref.get()
            return jsonify(tasks), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

#CREATE
@app.route('/add', methods=['POST'])
def create():
    if not request.json:
        abort(404)
    
    try:
        id = request.json['id']
        task = {
            'id': id,
            'name': request.json['name'],
            'check': False
        }
        ref.child(id).set(task)
        return jsonify({"sucess": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

#UPDATE
@app.route('/update', methods=['PUT'])
def update():
    try:
        id = request.json['id']
        if ref.child(id).get()==None:
            abort(404)
        if not request.json:
            abort(400)
        ref.child(id).update(request.json)
        return jsonify({"sucess": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

#DELETE
@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        task_id = request.args.get('id')
        if ref.child(task_id).get()==None:
            abort(404)
        ref.child(task_id).delete()
        return jsonify({"sucess": True}), 200
    except Exception as e:
        return f"Ocurrio el siguiente error: {e}"

port = int(os.environ.get('PORT', 8000))

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
    app.run(debug=True)
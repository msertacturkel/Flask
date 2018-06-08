from flask import Flask, jsonify, make_response, request, url_for, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
'''
GET 
'''


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


''' Create New Connection Service Template'''


@app.route('/datameer/gateway/create/connection', methods=['POST'])
def create_new_connection():
    return jsonify({'task_': ' new connection created ...'}), 201


''' Get view or Table due con_str'''


@app.route('/datameer/gateway/get/viewortable/<string:con_str>', methods=['GET'])
def get_table_or_view(con_str):
    return jsonify({'task_ get due con_str...': con_str})


''' Get Related fields due con_name'''


@app.route('/datameer/gateway/get/relatedfields/<string:con_name>', methods=['GET'])
def get_related_fields(con_name):
    return jsonify({'task_ get related fields due con_str...': con_name})


''' Get Selected fields due con_name'''


@app.route('/datameer/gateway/get/selectedfields/<string:con_name>', methods=['GET'])
def get_selected_fields(con_name):
    return jsonify({'task_ get selected fields due con_str...': con_name})


''' Run Job with con_name '''


@app.route('/datameer/gateway/run/job/<string:con_name>', methods=['GET'])
def run_job(con_name):
    return jsonify({'task_ get run job with con_str...': con_name})


''' List Connections'''


@app.route('/datameer/gateway/get/connections', methods=['GET'])
def get_connections():
    return jsonify({'task_ get run job with con_str.. ': ' get connections called'})


''' Get Columns for selected tables, Selected tables passed with Request Body '''


@app.route('/database/gateway/get/columns', methods=['POST'])
def get_connections():
    return jsonify({'task_ get run job with con_str.. ': ' get columns called'})


''' Get Updated table or view data from Datatable Updated tables passed with Request Body '''


@app.route('/datameer/gateway/get/updatedtableorview', methods=['POST'])
def get_connections():
    return jsonify({'task_ get run job with con_str.. ': ' get updatedtableorview called'})


''' Update new Cron expression with Request Body'''


@app.route('/datameer/gateway/get/updatedcronexp', methods=['POST'])
def get_connections():
    return jsonify({'task_ get run job with con_str.. ': ' get updatedtableorview called'})


''' Get Connection String with database name  '''


@app.route('/datameer/gateway/get/constr/<string:db_name>', methods=['GET'])
def get_table_or_view(db_name):
    return jsonify({'task_ get due db_name...': db_name})


if __name__ == '__main__':
    app.run(debug=True)

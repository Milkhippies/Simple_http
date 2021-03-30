import random

from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

tutorials = [
    {
        "id": 0,
        "title": 'Video #1. Intro',
        "description": 'Get, POST routes'
    },
    {
        "id": 1,
        "title": 'Video #2. More features',
        "description": 'PUT, DELETE routes'
    },
    {
        "id": 2,
        "title": 'Video #3. Id 2',
        "description": 'Hehe, its 3'
    },
    {
        "id": 3,
        "title": 'Video #4. Id 3',
        "description": 'Blink your diode here'
    },
    {
        "id": 4,
        "title": 'Video #5. Id 4',
        "description": 'Hello, world!'
    },
    {
        "id": 5,
        "title": 'Video #6. Id 5',
        "description": 'Simple text'
    }
]


@app.route('/tutorials/' or '/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['GET'])
def get_id_tutorials(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    return jsonify(tutorials[tutorial_id])


@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorials(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)
    return item


@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorials(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials)
                   if x[1]['id'] == tutorial_id), (None, None))

    tutorials.pop(idx)
    return "", 204


if __name__ == '__main__':
    app.run()

import os
from flask import Flask, request
from people import get_people, add_people, edit_people, delete_people


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/api')
def api_base():
    return request.args


methods = ['GET', 'POST', 'PUT', 'DELETE']
@app.route('/api/people/', methods=methods)
@app.route('/api/people/<id>', methods=methods)
def api_people(id=None):

    if request.method == "POST":
        data = request.get_json()
        return add_people(data)

    elif request.method == "PUT":
        data = request.get_json()
        return edit_people(data)

    elif request.method == "DELETE":
        data = request.get_json()
        return delete_people(data)
    else:
        return get_people(id)


@app.route('/api/systems')
def api_systems():
    return 'system results here'


@app.route('/api/planets')
def api_planets():
    return 'planets results here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

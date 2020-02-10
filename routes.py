import os
import json
from flask import Flask, request, current_app
from queries import getPeople


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/api')
def apiBase():
    return request.args


methods = ['GET', 'POST', 'PUT', 'DELETE']
@app.route('/api/people', methods=methods)
@app.route('/api/people/<id>', methods=methods)
def apiPeople(id="all"):

    if request.method == "POST":
        return "post"
    elif request.method == "PUT":
        return "put"
    elif request.method == "DELETE":
        return "delete"
    else:
        print("GET")

        people = getPeople()

        if people == 'failed':
            return 'Connection to DB failed'
        else:

            """
            https://stackoverflow.com/questions/16908943/display-json-returned-from-flask-in-a-neat-way
            https://www.programiz.com/python-programming/json
            https://stackoverflow.com/questions/37255313/what-is-a-right-way-for-rest-api-response """
            return current_app.response_class(
                    json.dumps(
                                {
                                    'Status': 'Success',
                                    'Count': len(people),
                                    'Data': people
                                },
                                indent=4,
                                sort_keys=False,
                                ensure_ascii=False
                                ), mimetype="application/json")


@app.route('/api/systems')
def apiSystems():
    return 'system results here'


@app.route('/api/planets')
def apiPlanets():
    return 'planets results here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

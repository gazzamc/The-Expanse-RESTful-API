import os
from flask import Flask, request, json, current_app
from queries import getPeople


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/api')
def apiBase():
    return request.args


@app.route('/api/people')
def apiPeople():
    people = getPeople()

    if people == 'failed':
        return 'Connection to DB failed'
    else:
        return current_app.response_class(
                                        json.dumps(
                                                    people,
                                                    indent=4,
                                                    sort_keys=False
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

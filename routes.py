import os
import json
from flask import Flask, request, current_app
from queries import getPeople, addPeople


app = Flask(__name__)


def responseCode(code, message):
    response = {
        'status': code,
        'message': message
    }
    return json.dumps(
                    response,
                    indent=4,
                    sort_keys=False)


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
        data = request.get_json()

        if data is None:
            return responseCode(
                400,
                'Bad Request. Data must be in JSON format'
            )

        else:
            try:
                name = data['name']
                gender = data['gender']
                status = data['status']
                desc = ""

            except KeyError:
                return responseCode(
                    400,
                    'Bad Request. One or more fields not supplied or invalid'
                )

            if (type(name) is str and type(gender) is str
                    and type(status) is str and type(desc) is str):
                if len(name) == 0 or len(gender) == 0 or len(status) == 0:
                    return responseCode(
                        400,
                        'Bad Request. One or more fields not supplied or invalid'
                    )
                else:
                    isAdded = addPeople(name, status, gender, desc)

                    if isAdded != "failed":
                        return responseCode(
                            201,
                            'Record created in database'
                        )
                    else:
                        return responseCode(
                            403,
                            'Record was not created in database'
                        )
            else:
                return responseCode(
                    400,
                    'Bad Request. One or more fields not supplied or invalid'
                )

    elif request.method == "PUT":
        return "put"
    elif request.method == "DELETE":
        return "delete"
    else:

        people = getPeople()

        if people == 'failed':
            return responseCode(
                503,
                'Cannot connect to database'
            )
        else:

            """
            https://stackoverflow.com/questions/16908943/display-json-returned-from-flask-in-a-neat-way
            https://www.programiz.com/python-programming/json
            https://stackoverflow.com/questions/37255313/what-is-a-right-way-for-rest-api-response """
            return current_app.response_class(
                    json.dumps(
                                {
                                    'status': 200,
                                    'count': len(people),
                                    'data': people
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

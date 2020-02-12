import os
import json
from flask import Flask, request, current_app
from queries import get_people, add_people, delete_people


app = Flask(__name__)


def response_code(code, message):
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
def api_base():
    return request.args


methods = ['GET', 'POST', 'PUT', 'DELETE']
@app.route('/api/people', methods=methods)
@app.route('/api/people/<id>', methods=methods)
def api_people(id="all"):

    if request.method == "POST":
        data = request.get_json()

        if data is None:
            return response_code(
                400,
                'Bad Request. Data must be in JSON format'
            )

        else:
            try:
                name = data['name']
                gender = data['gender']
                status = data['status']
                desc = data['desc']

            except KeyError:
                return response_code(
                    400,
                    'Bad Request. One or more fields not supplied or invalid keyerror'
                )

            if (type(name) is str and type(gender) is str
                    and type(status) is str and type(desc) is str):
                if len(name) == 0 or len(gender) == 0 or len(status) == 0:
                    return response_code(
                        400,
                        'Bad Request. One or more fields not supplied or invalid'
                    )
                else:
                    is_added = add_people(name, status, gender, desc)

                    if is_added != "failed":
                        return response_code(
                            201,
                            'Record created in database'
                        )
                    else:
                        return response_code(
                            403,
                            'Record was not created in database'
                        )
            else:
                return response_code(
                    400,
                    'Bad Request. One or more fields not supplied or invalid not str'
                )

    elif request.method == "PUT":
        return "put"
    elif request.method == "DELETE":
        data = request.get_json()

        try:
            id = data['id']
            if type(id) is int:
                delete_rec = delete_people(id)

                if delete_rec != "failed":
                    return response_code(
                        200,
                        'Record successfully deleted'
                    )
                else:
                    return response_code(
                        204,
                        'Cannot delete record as it does not exist'
                    )
            else:
                return response_code(
                    400,
                    'Bad Request. One or more fields not supplied or invalid'
                )
        except KeyError:
            return response_code(
                400,
                'Bad Request. One or more fields not supplied or invalid'
            )
    else:

        people = get_people()

        if people == 'failed':
            return response_code(
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
def api_systems():
    return 'system results here'


@app.route('/api/planets')
def api_planets():
    return 'planets results here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

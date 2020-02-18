import os
import json
from flask import Flask, request, current_app
from queries import get_people, add_people, delete_people, edit_people


app = Flask(__name__)


def response_code(code=400, message=None):

    if code == 400 and message is None:
        message = 'Bad Request. One or more fields not supplied or invalid'

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
def api_people(id=None):

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
                return response_code()

            if (type(name) is str and type(gender) is str
                    and type(status) is str and type(desc) is str):
                if len(name) == 0 or len(gender) == 0 or len(status) == 0:
                    return response_code()
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
                return response_code()

    elif request.method == "PUT":
        data = request.get_json()
        try:
            id = data['id']
            name = data['name']
            status = data['status']
            gender = data['gender']
            desc = data['desc']

            if id is not None:
                if (status is not None and name is not None
                        and gender is not None and desc is not None):
                    edited = edit_people(id, name, status, gender, desc)

                    if edited != "failed":
                        return response_code(
                            200,
                            'Record was successfully altered'
                        )
                    else:
                        return response_code(
                            403,
                            'Record was not altered'
                        )
                else:
                    return response_code()
            else:
                return response_code()
        except KeyError:
            return response_code()

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
                return response_code()
        except KeyError:
            return response_code()
    else:

        people = get_people(id)

        if people == 'failed':
            return response_code(
                503,
                'Cannot connect to database'
            )
        if people == 'not found':
            return response_code(
                404,
                'Record does not exist'
            )
        else:

            if id is None:
                count = len(people)
            else:
                count = 1

            """
            https://stackoverflow.com/questions/16908943/display-json-returned-from-flask-in-a-neat-way
            https://www.programiz.com/python-programming/json
            https://stackoverflow.com/questions/37255313/what-is-a-right-way-for-rest-api-response """
            return current_app.response_class(
                    json.dumps(
                                {
                                    'status': 200,
                                    'count': count,
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

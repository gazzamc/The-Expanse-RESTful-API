import json
from flask import current_app
from queries import (get_people_query, add_people_query,
                     delete_people_query, edit_people_query)


def response_code(code=400, message=None):

    if code == 400 and message is None:
        message = 'Bad Request. One or more fields not supplied or invalid'

    response = {
        'status': code,
        'message': message
    }
    return current_app.response_class(
                json.dumps(
                    response,
                    indent=4,
                    sort_keys=False
                    ), mimetype="application/json")


def get_people(id=None):
    try:
        if id is not None:
            id = int(id)

        people = get_people_query(id)

        if people == 'no connection':
            return response_code(
                503,
                'Cannot connect to database'
            )
        elif people == 'failed':
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
    except ValueError:
        return response_code(
            400,
            'Bad Request. ID must be an integer'
        )


def add_people(data):
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
                added = add_people_query(name, status, gender, desc)

                if added == 'no connection':
                    return response_code(
                        503,
                        'Cannot connect to database'
                    )
                elif added == "duplicate":
                    return response_code(
                        403,
                        'Duplicate, Record was not created in database'
                    )
                else:
                    return response_code(
                        201,
                        'Record created in database'
                    )
        else:
            return response_code()


def edit_people(data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )

    try:
        id = data['id']
        name = data['name']
        status = data['status']
        gender = data['gender']
        desc = data['desc']

        if id is not None:
            if (status is not None and name is not None
                    and gender is not None and desc is not None):
                if status == "" and name == "" and gender == "" and desc == "":
                    return response_code()
                else:
                    edited = edit_people_query(id, name, status, gender, desc)

                    if edited == 'no connection':
                        return response_code(
                            503,
                            'Cannot connect to database'
                        )
                    elif edited == "no record":
                        return response_code(
                            404,
                            'Record does not exist'
                        )
                    elif edited == "failed":
                        return response_code(
                            403,
                            'Record was not altered'
                        )
                    else:
                        return response_code(
                            200,
                            'Record was successfully altered'
                        )
            else:
                return response_code()
        else:
            return response_code()
    except KeyError:
        return response_code()


def delete_people(data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )
    try:
        id = data['id']
        if type(id) is int:
            delete_rec = delete_people_query(id)

            print(delete_rec, flush=False)

            if delete_rec == 'no connection':
                return response_code(
                    503,
                    'Cannot connect to database'
                )
            elif delete_rec == 'no record':
                return response_code(
                    204,
                    'Cannot delete record as it does not exist'
                )
            else:
                return response_code(
                    200,
                    'Record successfully deleted'
                )
        else:
            return response_code()
    except KeyError:
        return response_code()

import json
from flask import current_app
from systems_queries import (get_systems_query, add_system_query,
                             edit_system_query, delete_system_query)
from people import response_code


def get_systems(id):
    try:
        if id is not None:
            id = int(id)

        systems = get_systems_query(id)

        if systems == 'no connection':
            return response_code(
                503,
                'Cannot connect to database'
            )
        elif systems == 'failed':
            return response_code(
                404,
                'Record does not exist'
            )
        else:
            if id is None:
                count = len(systems)
            else:
                count = 1

            return current_app.response_class(
                    json.dumps(
                                {
                                    'code': 200,
                                    'results': count,
                                    'data': systems
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


def add_system(data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )

    else:
        try:
            name = data['name']
            planets = data['planets']
            desc = data['desc']

        except KeyError:
            return response_code()

        if (type(name) is str and type(planets) is int
                and type(desc) is str):
            if len(name) == 0 or planets is None:
                return response_code()
            else:
                added = add_system_query(name, planets, desc)

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


def edit_system(data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )

    try:
        id = data['id']
        name = data['name']
        planets = data['planets']
        desc = data['desc']

        if id is not None:
            if (name is not None and planets is not None
                    and desc is not None):
                if planets == "" and name == "" and desc == "":
                    return response_code()
                else:
                    edited = edit_system_query(id, name, planets, desc)

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


def delete_system(data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )
    try:
        id = data['id']
        if type(id) is int:
            delete_rec = delete_system_query(id)

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

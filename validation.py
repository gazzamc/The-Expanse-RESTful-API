import json
from flask import current_app
from people_queries import (get_people_query, add_people_query,
                            delete_people_query, edit_people_query,
                            get_people_query_filtered)
from system_queries import (get_systems_query, add_system_query,
                            edit_system_query, delete_system_query,
                            get_system_query_filtered)
from location_queries import (get_locations_query, add_location_query,
                              edit_location_query, delete_location_query,
                              get_location_query_filtered)


def response_code(code=400, message=None):

    if code == 400 and message is None:
        message = 'Bad Request. One or more fields not supplied or invalid'

    response = {
        'code': code,
        'message': message
    }
    return current_app.response_class(
                json.dumps(
                    response,
                    indent=4,
                    sort_keys=False
                    ), mimetype="application/json")


def get_data(table, id=None, offset=0):

    try:
        if id is not None:
            id = int(id)

        if table == "people":
            results = get_people_query(id, offset)
        elif table == "systems":
            results = get_systems_query(id, offset)
        elif table == "locations":
            results = get_locations_query(id, offset)

        if results == 'no connection':
            return response_code(
                503,
                'Cannot connect to database'
            )
        elif results == 'failed':
            return response_code(
                404,
                'Record does not exist'
            )
        else:
            if int(offset) >= int(results[1]):
                return response_code(
                    404,
                    'Page does not exist'
                )
            elif results[1] > 25:
                page = round(int(offset) / 25) + 1
                pages = round(results[1] / 25) + 1
            else:
                page = 1
                pages = 1

            """
            https://stackoverflow.com/questions/16908943/display-json-returned-from-flask-in-a-neat-way
            https://www.programiz.com/python-programming/json
            https://stackoverflow.com/questions/37255313/what-is-a-right-way-for-rest-api-response """
            return current_app.response_class(
                    json.dumps(
                                {
                                    'code': 200,
                                    'results': results[1],
                                    'pages': '{} of {}'.format(page, pages),
                                    'data': results[0]
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


def get_data_filtered(table, filter):

    for key in filter:
        if key == 'offset':
            if table == "people":
                return get_data("people", None, filter[key])
            elif table == "systems":
                return get_data("systems", None, filter[key])
            elif table == "locations":
                return get_data("locations", None, filter[key])

        elif key == 'name':
            if table == "people":
                query = get_people_query_filtered("name", filter[key])
            elif table == "systems":
                query = get_system_query_filtered("name", filter[key])
            elif table == "locations":
                query = get_location_query_filtered("name", filter[key])

        elif key == 'status':
            if (filter[key] == "alive" or filter[key] == "deceased" or
               filter[key] == "unknown"):

                query = get_people_query_filtered("status", filter[key])
            else:
                return response_code(
                    400,
                    'Bad Request. Status must be alive, deceased or unknown'
                )
        elif key == 'gender':

            if (filter[key] == "male" or filter[key] == "female" or
                    filter[key] == "unknown"):

                query = get_people_query_filtered("gender", filter[key])
            else:
                return response_code(
                    400,
                    'Bad Request. Gender must be male, female or unknown'
                )
        else:
            return response_code(
                400,
                'Bad Request. Query string unrecognised'
            )

        if len(query) > 0:
            count = len(query)
        else:
            return response_code(
                404,
                'No records found for query \'' + filter[key] + '\''
            )

        if query != "failed":
            return current_app.response_class(
                                json.dumps(
                                            {
                                                'code': 200,
                                                'count': count,
                                                'data': query
                                            },
                                            indent=4,
                                            sort_keys=False,
                                            ensure_ascii=False
                                            ), mimetype="application/json")
        elif query == "no connection":
            return response_code(
                503,
                'Cannot connect to database'
            )
        else:
            return response_code()


def is_add_valid(table, value1="",
                 value2="", value3="", value4=""):
    valid = False

    if table == "people":
        name = value1
        desc = value2
        gender = value3
        status = value4

        if (type(name) is str and type(desc) is str
                and type(gender) is str and type(status) is str):
            if len(name) != 0 or len(gender) != 0 or len(status) != 0:
                if (gender == "male" or gender == "female" or
                   gender == "unknown"):
                    if (status == "alive" or status == "deceased" or
                       status == "unknown"):
                        valid = True

    return valid


def is_edit_valid(table, id, value1=None,
                  value2=None, value3=None, value4=None):
    valid = False
    name = value1
    desc = value2

    if table == "people":
        gender = value3
        status = value4

        if id is not None and type(id) is int:
            if (status is not None and name is not None
                    and gender is not None and desc is not None):
                if status != "" or name != "" or gender != "" or desc != "":
                    if (status == "alive" or status == "deceased" or
                       status == "unknown" or status == ""):
                        if (gender == "male" or gender == "female" or
                           gender == "unknown" or gender == ""):
                            valid = True

    if table == "systems":
        planets = value3

        if id is not None and type(id) is int:
            if (planets is not None and name is not None
                    and desc is not None):
                if name != "" or desc != "" or (planets != "" and type(planets) is int):
                    valid = True

    return valid


def add_data(table, data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )

    else:
        try:
            name = data['name']
            desc = data['desc']

            if table == "people":
                gender = data['gender']
                status = data['status']

                is_valid = is_add_valid(
                        "people",
                        name,
                        desc,
                        gender,
                        status)

            if not is_valid:
                return response_code()
            else:
                if table == "people":
                    added = add_people_query(name, status, gender, desc)
                elif table == "locations":
                    added = add_location_query(name, status, gender, desc)
                elif table == "systems":
                    added = add_system_query(name, status, gender, desc)

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

        except KeyError:
            return response_code()


def edit_data(table, data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )
    else:
        try:
            id = data['id']
            name = data['name']
            desc = data['desc']

            if table == "people":
                gender = data['gender']
                status = data['status']

                is_valid = is_edit_valid(
                        "people",
                        id,
                        name,
                        desc,
                        gender,
                        status)

            elif table == "systems":
                planets = data['planets']

                is_valid = is_edit_valid(
                        "systems",
                        id,
                        name,
                        desc,
                        planets)

            if not is_valid:
                return response_code()
            else:
                if table == "people":
                    edited = edit_people_query(id, name, status, gender, desc)
                if table == "systems":
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

        except KeyError:
            return response_code()


def delete_data(table, data):
    if data is None:
        return response_code(
            400,
            'Bad Request. Data must be in JSON format'
        )
    try:
        id = data['id']
        if type(id) is int:
            if table == "people":
                delete_rec = delete_people_query(id)
            elif table == "systems":
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

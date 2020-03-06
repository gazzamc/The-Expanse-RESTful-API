import json
from flask import current_app
from validation import response_code
from database.people import get_people_query, get_people_query_filtered
from database.system import get_systems_query, get_system_query_filtered
from database.location import get_locations_query, get_location_query_filtered


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
        elif key == 'system':
            query = get_location_query_filtered("system", filter[key])
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

        if query == 'no connection':
            return response_code(
                503,
                'Cannot connect to database'
            )
        else:
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

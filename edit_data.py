from validation import is_edit_valid, response_code
from people_queries import edit_people_query
from system_queries import edit_system_query
from location_queries import edit_location_query


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

            elif table == "locations":
                population = data['population']
                system = data['system']

                is_valid = is_edit_valid(
                        "locations",
                        id,
                        name,
                        desc,
                        population,
                        system)

            if not is_valid:
                return response_code()
            else:
                if table == "people":
                    edited = edit_people_query(id, name, status, gender, desc)
                elif table == "systems":
                    edited = edit_system_query(id, name, planets, desc)
                elif table == "locations":
                    edited = edit_location_query(id, name, population, system, desc)

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

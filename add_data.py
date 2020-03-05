from validation import is_add_valid, response_code
from people_queries import add_people_query
from system_queries import add_system_query
from location_queries import add_location_query


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

            elif table == "systems":
                planets = data['planets']

                is_valid = is_add_valid(
                        "systems",
                        name,
                        desc,
                        planets)

            elif table == "locations":
                population = data['population']
                system = data['system']

                is_valid = is_add_valid(
                        "locations",
                        name,
                        desc,
                        population,
                        system)

            if not is_valid:
                return response_code()
            else:
                if table == "people":
                    added = add_people_query(name, status, gender, desc)
                elif table == "systems":
                    added = add_system_query(name, planets, desc)
                elif table == "locations":
                    added = add_location_query(name, population, system, desc)

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
                elif added == "system incorrect":
                    return response_code()
                else:
                    return response_code(
                        201,
                        'Record created in database'
                    )

        except KeyError:
            return response_code()

from validation import response_code
from people import delete_people_query
from system import delete_system_query
from location import delete_location_query


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
            elif table == "locations":
                delete_rec = delete_location_query(id)

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

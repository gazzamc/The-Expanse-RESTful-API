from validation import response_code
from database.people import delete_people_query
from database.system import delete_system_query
from database.location import delete_location_query


def delete_data(table, data):
    '''
    Takes in endpoint/table name, JSON data and
    returns JSON response.

            Parameters:
                    table (str): endpoint/table
                    data (JSON Object): JSON data

            Returns:
                    JSON Object: JSON response
    '''
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

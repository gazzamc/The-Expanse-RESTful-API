import json
from flask import current_app


def response_code(code=400, message=None):
    '''
    Takes in code, message and returns it as JSON Object.

            Parameters:
                    code (int, Optional): Integer of error code
                    message (str, Optional): Error message

            Returns:
                    JSON Object: JSON object of error code and message
    '''
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


def is_add_valid(table, value1="",
                 value2="", value3="", value4=""):
    '''
    This function takes in endpoint/table name and
    up to four optional values. Returns a Boolean.

            Parameters:
                    table (str): endpoint/table name
                    value1 (str, Optional): name
                    value2 (str, Optional): desc
                    value3 (str, Optional): gender/planets/population
                    value4 (str, Optional): status/system

            Returns:
                    Boolean: True or False depending if valid data.
    '''
    valid = False

    if table == "people":
        name = value1
        desc = value2
        gender = value3
        status = value4

        # Check to see if all input values are strings
        if (type(name) is str and type(desc) is str and
                type(gender) is str and type(status) is str):
            # Check if at least one variable is not an empty string
            if len(name) != 0 or len(gender) != 0 or len(status) != 0:
                # Verify the string matches the options provided
                if (gender == "male" or gender == "female" or
                   gender == "unknown"):
                    if (status == "alive" or status == "deceased" or
                       status == "unknown"):
                        valid = True

    if table == "systems":
        name = value1
        desc = value2
        planets = value3

        # Check to see name, desc are strings and planet is an int
        if (type(name) is str and type(desc) is str and
                type(planets) is int):
            # Check if at least one variable is not an empty string
            if len(name) != 0 or len(planets) != 0:
                valid = True

    if table == "locations":
        name = value1
        desc = value2
        population = value3
        system = value4

        if (type(name) is str and type(desc) is str and
                type(system) is str and type(population) is str):
            if len(name) != 0 or len(system) != 0:
                if population.isdigit() or population[1:]:
                    valid = True

    return valid


def is_edit_valid(table, id, value1=None,
                  value2=None, value3=None, value4=None):
    '''
    This function takes in endpoint/table name and
    up to four optional values. Returns a Boolean.

            Parameters:
                    table (str): endpoint/table name
                    id (int): id of record to edit
                    value1 (str, Optional): name
                    value2 (str, Optional): desc
                    value3 (str, Optional): gender/planets/population
                    value4 (str, Optional): status/system

            Returns:
                    Boolean: True or False depending if valid data.
    '''
    valid = False
    name = value1
    desc = value2

    if table == "people":
        gender = value3
        status = value4

        # Checking if id is not null and is type int
        if id is not None and type(id) is int:
            # Checking that all variables are provided
            if (status is not None and name is not None and
                    gender is not None and desc is not None):
                # Check if at least one variable is not an empty string
                if status != "" or name != "" or gender != "" or desc != "":
                    # Verify the string matches the options provided
                    if (status == "alive" or status == "deceased" or
                       status == "unknown" or status == ""):
                        if (gender == "male" or gender == "female" or
                           gender == "unknown" or gender == ""):
                            valid = True

    if table == "systems":
        planets = value3

        if id is not None and type(id) is int:
            if (planets is not None and name is not None and
                    desc is not None):
                if (name != "" or desc != "" or
                   (planets != "" and type(planets) is int)):
                    valid = True

    if table == "locations":
        population = value3
        system = value4

        # Checking if id is not null and is type int
        if id is not None and type(id) is int:
            # Checking that all variables are provided
            if (population is not None and name is not None and
                    desc is not None and system is not None):
                # Check if at least one variable is not an empty string
                if (name != "" or desc != "" or
                   population != "" or system != ""):
                    # Check if pop is digit and ignore
                    # first index incase < or > sign
                    if population.isdigit() or population[1:]:
                        valid = True

    return valid

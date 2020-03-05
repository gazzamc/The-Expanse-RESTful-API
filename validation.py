import json
from flask import current_app


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

    if table == "systems":
        name = value1
        desc = value2
        planets = value3

        if (type(name) is str and type(desc) is str
                and type(planets) is int):
            if len(name) != 0 or len(planets) != 0:
                valid = True

    if table == "locations":
        name = value1
        desc = value2
        population = value3
        system = value4

        if (type(name) is str and type(desc) is str
                and type(system) is str
                and type(population) is str):
            if len(name) != 0 or len(system) != 0:
                if population.isdigit() or population[1:]:
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
                if (name != "" or desc != "" or
                   (planets != "" and type(planets) is int)):
                    valid = True

    if table == "locations":
        population = value3
        system = value4

        if id is not None and type(id) is int:
            if (population is not None and name is not None
                    and desc is not None and system is not None):
                if (name != "" or desc != "" or
                   population != "" or system != ""):
                    # Check if pop is digit and ignore
                    # first index incase < or > sign
                    if population.isdigit() or population[1:]:
                        valid = True

    return valid

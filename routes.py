import os
import json
from add import add_data
from edit import edit_data
from get import get_data, get_data_filtered
from delete import delete_data
from flask import Flask, request, render_template, current_app
from validation import response_code


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/documentation')
def docs():
    return render_template("docs.html")


@app.route('/api')
def api_base():
    response = {
        "base_url": request.base_url,
        "endpoints": [
            {
                "people": [
                    request.base_url + "/people",
                    request.base_url + "/people?offset=<offset>",
                    request.base_url + "/people/<id>",
                    {
                        "filter": [
                            request.base_url + "/people?name=<name>",
                            request.base_url + "/people?status=<status>",
                            request.base_url + "/people?gender=<gender>"
                        ]
                    }
                ],
                "systems":[
                    request.base_url + "/systems",
                ],
                "locations":[
                    request.base_url + "/locations",
                ]
            }
        ]
    }

    return current_app.response_class(
                json.dumps(
                    response,
                    indent=4,
                    sort_keys=False
                    ), mimetype="application/json")


methods = ['GET', 'POST', 'PUT', 'DELETE']
@app.route('/api/people', methods=methods)
@app.route('/api/people/<id>', methods=['GET'])
def api_people(id=None):

    if request.method == "POST":
        data = request.get_json()
        return add_data("people", data)

    elif request.method == "PUT":
        data = request.get_json()
        return edit_data("people", data)

    elif request.method == "DELETE":
        data = request.get_json()
        return delete_data("people", data)
    else:
        requests = len(request.args)

        if requests > 0:
            return get_data_filtered("people", request.args)
        else:
            return get_data("people", id)


@app.route('/api/systems', methods=methods)
@app.route('/api/systems/<id>', methods=['GET'])
def api_systems(id=None):
    if request.method == "POST":
        data = request.get_json()
        return add_data("systems", data)

    elif request.method == "PUT":
        data = request.get_json()
        return edit_data("systems", data)

    elif request.method == "DELETE":
        data = request.get_json()
        return delete_data("systems", data)
    else:
        requests = len(request.args)

        if requests > 0:
            return get_data_filtered("systems", request.args)
        else:
            return get_data("systems", id)


@app.route('/api/locations', methods=methods)
@app.route('/api/locations/<id>', methods=['GET'])
def api_locations(id=None):
    if request.method == "POST":
        data = request.get_json()
        return add_data("locations", data)

    elif request.method == "PUT":
        data = request.get_json()
        return edit_data("locations", data)

    elif request.method == "DELETE":
        data = request.get_json()
        return delete_data("locations", data)
    else:
        requests = len(request.args)

        if requests > 0:
            return get_data_filtered("locations", request.args)
        else:
            return get_data("locations", id)


@app.errorhandler(404)
def invalid_route(e):
    """ https://codehandbook.org/handle-404-error-python-flask/ """
    if "api/" in request.url:
        return response_code(
            "404",
            "Invalid EndPoint"
            )
    else:
        return render_template("404.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

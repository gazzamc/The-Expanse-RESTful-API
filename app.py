"""
    Main application file,
    consists of the endpoints and starts the
    application.
"""

import os
from utils.add import add_data
from utils.edit import edit_data
from utils.get import get_data, get_data_filtered
from utils.delete import delete_data
from flask import Flask, request, render_template
from utils.validation import response_code
from utils.endpoints import endpoint_dir
METHODS = ['GET', 'POST', 'PUT', 'DELETE']

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/documentation')
def docs():
    return render_template("docs.html")


@app.route('/api')
def api_base():
    return endpoint_dir()


@app.route('/api/people', methods=METHODS)
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


@app.route('/api/systems', methods=METHODS)
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


@app.route('/api/locations', methods=METHODS)
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
            debug=bool(int(os.environ.get("DEVELOPMENT"))))

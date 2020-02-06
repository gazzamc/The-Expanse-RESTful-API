import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/api')
def apiBase():
    return 'api endpoints here'


@app.route('/api/people')
def apiPeople():
    return 'people results here'


@app.route('/api/systems')
def apiSystems():
    return 'system results here'


@app.route('/api/planets')
def apiPlanets():
    return 'planets results here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# The Expanse - RESTful API
Data Centric Development Milestone Project - Code Institute

## Table Of Contents:

## Demo
You can try the live version of the API [Here](https://expanse-api.herokuapp.com/)<br><br>


## UX

#### User Stories

#### Strategy
I wanted to create a RESTful API using python3, flask and mySQL. To showcase this I also
wanted to created a simple website that would allow you to test the endpoints and add,
edit or delete records.

#### Scope

#### Structure

#### Skeleton

#### Surface
I went with very neutral colours to make it look easy on the eye, as this is a simple
testing site for the API i didnt think it needed a lot to standout. The buttons are coloured
appropriatly for what they do. Edit being yellow as a warning, delete being red etc. As
bootstrap had these built-in styles I didn't do anything custom in the CSS.

## Features
- Users can filter the data using *query strings*, such as by *name*, status, *gender* etc.
- Users can retrieve single records using the ID of said record in the URI.
- Users can Add, Edit and Delete records from the database.
- The API has input validation to prevent users from entering the wrong type of data.
- If there is an error processing the request the API will display an error code with an appropiate error message.
- Users can interact with the API via the website or directly using **Curl**, **Postman** or a language of their choosing.
- The website allows the user to enter new data directly into the *JSON* result instead of a traditional form.


### Features left to Implement
- In the current version of the API there is little to no security, 
I would like to add a key/token to verify users for data manipulation and
limit queries.
- I would like to add more query string filters to search for more specific records.
- I would like to add more endpoints such as organisations and ships.

## Technologies Used

- [Python3]()
    - **Python3** was used for validation and querying the database as well as parsing the data from the wiki.

- [MySQL/ClearDB]()
    - **MySQL/ClearDB** was used to store the tables and columes of data for the API.

- [Flask]()
    - **Flask** was used to create the endpoints, handle 404 pages and output the API data.

- [Javascript]()
    - **Javascript** was used to retrieve and send data to the API and hide/show elements.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - **CSS3** was used to add custom styles and positioning of the HTML elements.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** was used to layout the basic structure of the website.


## Testing
The website was tested in chrome, firefox and edge for responsiveness. 
The majority of my testing consisted of using the developer tools in chrome while working on the website design. 
As for testing the API endpoints I used the [**Postman Chrome Extension**](https://www.postman.com/), 
this allowed me to test all the different methods (GET, PUT, POST, DELETE) 
and check that i got the appropriate response back.

### Manual Testing

### Automated Testing
I did do some basic unit testing using pythons *unittest* and *nose* modules.
These tests can be found in the `api_test.py` file. In order to run these tests 
you will need to connect to a working database to get the appropiate response that
I've set, otherwise it will return `No database connected` and fail.

To run these tests with an appropriate database connected use the following command:
```
nosetests -v
```

The nose module will auto discover the file with `_test.py` in the name.

Expected Result:
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/apiTest.png" alt="API Tests">
</p>

I only tested the API enpoints using the **GET** method. As i was connected to my live
database i didnt want to automate tests that would alter or delete records. Unfortunately I couldn't find a way to setup a temporary database for testing my **CRUD** functionality. The
closest thing i found for database testing was a **Mock** module which didn't suit my needs. 
It only mocked the database connection, 
and this wouldn't return the appropriate response the unit tests were expecting.
## Deployment

#### Heroku Dashboard

1. In the dropdown on the right, click **Create New App**.
2. On the next screen, enter app name and select server, then click **Create App**.
3. In the **Overview** page go to the **Deploy** tab.
4. Scroll down to **Deployment method** and choose **Heroku** (You can also deploy via **Github** here).
5. Using the git commands below, commit your code/project to **Heroku**:
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
6. To keep the Heroku branch up to date connect your **Github** repo for auto-deployment.
7. You can do this by clicking the Github icon and searching for the repo.
8. Once the repo is connected you should have an option below it called **Automatic deploys**.
9. To enable this click **Enable Automatic Deploys**.

Once the project is deployed you need to set the **config variables**, 
you can do this by following the instructions below:

1. In the **Heroku Dashboard** go to **Settings**.
2. Click **Reveal Config Vars**.
3. Enter in the variable names and their values
    - **CLEARDB_DATABASE_URL** (DATABASE URL HERE)
    - **IP** (0.0.0.0)
    - **Port** (5000)

#### Locally
To run the website from your local machine you can clone the project using the below command. 
You will need to install python3 and all its dependencies found in the requirements.txt file. 
You will also need a database with the same schema as shown in this readme.

1. Clone the git repository.
```
    git clone https://github.com/gazzamc/Milestone-Project-Three.git
```
2. Set the database URI in global variables, example of it here:
```
export CLEARDB_DATABASE_URL=mysql://username:password@hostname/databaseName
```
3. Navigate to the cloned folder via the terminal and enter:
```
python3 routes.py
```

## Credits

### Content
- The majority of data was sourced from the Fan Wiki of the show [here](https://expanse.fandom.com/wiki/The_Expanse_Wiki)

### Media
- The hero image of the earth in the jumbotron was sourced from [unsplash.com](https://unsplash.com/photos/Q1p7bh3SHj8).

### Acknowledgements
- Using [this](https://clubmate.fi/javascript-adding-and-removing-class-names-from-elements/) example I was able to add/remove classes in Javascript with less hassle.
- [This](https://clubmate.fi/javascript-adding-and-removing-class-names-from-elements/) article about filtering for restful APIs was very informative and helped me implement a form of filtering in this project.
- Using the example from [this](https://codehandbook.org/handle-404-error-python-flask/) article I was able to implement the 404 page in my flask application when a user visited an invalid endpoint.
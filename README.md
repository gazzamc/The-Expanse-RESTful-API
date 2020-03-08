# The Expanse - RESTful API
Data Centric Development Milestone Project - Code Institute

## Table Of Contents:

## Demo
You can try the live version of the API [Here](https://expanse-api.herokuapp.com/)<br><br>


## UX

#### User Stories
- As a user I should be able test the API from the website.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/testApi.gif" alt="Test API" width="80%">
</p>

- As a user I should be able to view a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/viewResource.png" alt="View Resource" width="80%">
</p>

- As a user I should be warned before altering or deleting a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/addModal.png" alt="Add Resource Warning">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/editModal.png" alt="Edit Resource Warning">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/deleteModal.png" alt="Delete Resource Warning">
</p>

- As a user I should be able to edit a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/editResource.gif" alt="Edit Resource" width="80%">
</p>

- As a user I should be able to delete a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/deleteResource.gif" alt="Delete Resource" width="80%">
</p>

- As a user I should be able to add a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/addResource.gif" alt="Add Resource" width="80%">
</p>

- As a user I should be able to filter a resource.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/filter.png" alt="Filter Resource" width="80%">
</p>

- As a user I should get appropriate error/response messages.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/404.png" alt="404 error"><br />
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/404_2.png" alt="another 404 error">
</p>

- As a user I should have easy access to the API endpoints/filters.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/endpoints.png" alt="API endpoints" width="60%">
</p>

- As a user I should have relevent information available to me about the API.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/docs.png" alt="Documents Page" width="60%">
</p>

#### Strategy
I wanted to create a RESTful API using python3, flask and mySQL. To showcase this I also
wanted to created a simple website that would allow you to test the endpoints and add,
edit or delete records.

#### Scope

#### Structure
- ##### Website
    For the index page of the website i wanted to keep it simple and straight to the point.

    At the top of the page is the navigation bar with the two pages linked, this changes into a hamburger
    button on smaller screens. Then have a hero image with a jumbotron containing the sites name.

    The user is then presented with a search bar under the hero image. Right below that is the results 
    box which is pre-filled on the first load with the API's base url's resource. This is a directory
    of endpoints and their corresponding filters.

    Under the results is a short about section that gives a brief description of the API and it's resources.
    This is followed by "How to use" section which points the user the sites documentation for further information
    on the API and how to use it.

    On the documentation pages, the User is presented with a menu on the left and the main content on the right.
    The User can select any of the menu items and the page will scroll to the corresponding section.

    Finally in the footer we have social links to Github, Linkedin and the github branch of this project.

- ##### API

    On a GET request of any of the endpoints resources the user will be presented a JSON object, like the one below:
    ```
    {
        "code": 200,
        "results": 1,
        "pages": "1 of 1",
        "data": {
            "id": 1,
            "name": "Captain McDowell",
            "status": "alive",
            "gender": "Male",
            "desc": "Captain McDowell has been commissioned by the 
            Pur'n'Kleen Water Company as the commanding officer of the Canterbury"
        }
    }
    ```

    The people resource will consist of the resource `id`, `name`, `status`, `gender` and `desc`.<br />
    The locations resource will consist of the resource `id`, `name`, `population`, `system` and `desc`.<br />
    The systems resource will consist of the resource `id`, `name`, `planets` and `desc`.<br />

    Each endpoint has certain filters than the user can use to query specific resources.

    ##### Filters:
    ###### people:
    - offset:<br />
        As the default amount of results returned is 25, this allows users to get results beyond this point.<br /><br />
    - name:<br />
        Searches resources by its `name`, if blank will return all. If no match is found error message is returned.<br /><br />
    - status:<br />
        Searches resources by `status`, if input is not `alive`, `deceased` or `unknown` and error message will be returned.<br /><br />
    - gender:<br />
        Searches resources by `gender`, if input is not `male`, `female` or `unknown` and error message will be returned.<br />
    
    ###### locations:
    - offset:<br /><br />
    - name:<br /><br />
    - systems:<br />
        Searches resources by `gender`, if input is not `male`, `female` or `unknown` and error message will be returned.<br />

    ###### systems:
    - offset:<br /><br />
    - name:<br /><br />

    For more information on these filters you can view the documentation on the website [here](https://expanse-api.herokuapp.com/documentation#filters).

    #### CRUD Functionality:
    ##### Website
    There is two ways to manipulate the data in the API, you can do directly by sending HTTP requests to the API or
    you can use the website as an interface. On the website when the user goes to add or edit a resource they will be 
    provided with a form within the JSON result. I find this to be the easiest way for the user to understand what data
    needs to go where. To delete a resource the user simply has to search for the resource using the `id` and click delete.

    ##### Directly
    When a user wants to Add, Edit or Delete a resource using a direct path to the API. They simply need to send the keys/values
    in JSON format with the appropiate request method. Below I will give examples of what the request would look like for each
    method.

    - GET 
    <br /><br />
        ```
        No JSON needed, sending a GET request with a valid endpoint will return a JSON object.
        ```
    <br /><br />
    - POST
    <br /><br />
        ```
            {
                "name": string,
                "status": string,
                "gender": string,
                "desc": string
            }
        ```
        These keys will vary, please check the corresponding documentation for each endpoint [here](https://expanse-api.herokuapp.com/documentation#resource)
    <br /><br />
    - PUT
    <br /><br />
        ```
            {
                "id": integer,
                "name": string,
                "status": string,
                "gender": string,
                "desc": string
            }
        ```
        These keys will vary, please check the corresponding documentation for each endpoint [here](https://expanse-api.herokuapp.com/documentation#resource)
    <br /><br />
    - DELETE
    <br /><br />
        ```

            {
                "id": integer,
            }
        ```
        These keys will vary, please check the corresponding documentation for each endpoint [here](https://expanse-api.herokuapp.com/documentation#resource)
    <br /><br />

    If these requests are successful you will recieve a JSON response back with a code and message. 
    Otherwise an error message will be send back with details of what went wrong.

#### Skeleton

#### Surface
I went with very neutral colours to make it look easy on the eye, as this is a simple
testing site for the API i didnt think it needed a lot to standout. The buttons are coloured
appropriately for what they do. Edit being yellow as a warning, delete being red etc. As
bootstrap had these built-in styles I didn't do anything custom in the CSS.

## Features
- Users can filter the data using *query strings*, such as by *name*, *status*, *gender* etc.
- Users can retrieve single records using the ID of said record in the URI.
- Users can Add, Edit and Delete records from the database.
- The API has input validation to prevent users from entering the wrong type of data.
- If there is an error processing the request the API will display an error code with an appropiate error message.
- Users can interact with the API via the website or directly using **Curl**, **Postman** or a language of their choosing.
- The website allows the user to enter new data directly into the *JSON* result instead of a traditional form.
- Querying the base url of the API will return all the endpoints and their filters.
- The website has a documentation page for all relevant information on using the API.


### Features left to Implement
- In the current version of the API there is little to no security, 
I would like to add a key/token to verify users for data manipulation and
limit queries.
- I would like to add more query string filters to search for more specific records.
- I would like to add more endpoints such as organisations and ships.

## Technologies Used

- [Python3](https://www.python.org/)
    - **Python3** was used for validation and querying the database as well as parsing the data from the wiki.

- [MySQL](https://www.mysql.com/)
    - **MySQL** was used to store the tables and columes of data for the API.

- [Flask](https://palletsprojects.com/p/flask/)
    - **Flask** was used to create the endpoints, handle 404 pages and output the API data.

- [Javascript](https://www.javascript.com/)
    - **Javascript** was used to retrieve and send data to the API and hide/show elements.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - **CSS3** was used to add custom styles and positioning of the HTML elements.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** was used to layout the basic structure of the website.

- [Bootstrap](https://getbootstrap.com/)
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

I only tested the API endpoints using the **GET** method. As i was connected to my live
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
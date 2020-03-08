# The Expanse - RESTful API
Data Centric Development Milestone Project - Code Institute

## Table Of Contents:
- [Demo](#demo)<br>
- [UX](#ux)<br>
    * [User Stories](#user-stories)<br>
    * [Strategy](#strategy)<br>
    * [Scope](#scope)<br>
    * [Structure](#structure)<br>
    * [Skeleton](#skeleton)<br>
    * [Surface](#surface)<br>
- [Error Codes](#error-codes)<br>
- [Database Schema](#database-schema)<br>
- [Features](#features)<br>
- [Features left to Implement](#features-left-to-implement)<br>
- [Technologies Used](#technologies-used)<br>
- [Testing](#testing)<br>
    * [Manual Testing](#manual-testing)<br>
    * [Automated Testing](#automated-testing)<br>
    * [Known Bugs](#known-bugs)<br>
- [Deployment](#deployment)<br>
- [Credits](#credits)<br>
    * [Content](#content)<br>
    * [Media](#media)<br>
    * [Acknowledgements](#acknowledgements)<br>

## Demo
You can try the live version of the API [Here](https://expanse-api.herokuapp.com/)<br><br>
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/demo.png" alt="Responsiveness" width="80%">
</p>

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

- As a user I should have relevant information available to me about the API.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Three/raw/master/screenshots/docs.png" alt="Documents Page" width="60%">
</p>

#### Strategy
I wanted to create a RESTful API using python3, flask and MySQL. To showcase this I also
wanted to created a simple website that would allow you to test the endpoints and add,
edit or delete records.

#### Scope
I wanted users to be able to test out the API without writing any code or using a development tool such as **Postman**.
And if when they were ready to start using the API that there was an informative documentation available for the API.
The website is simple in design, you can search for the resource, add a new resource or edit/delete an existing resource.

As for the API itself, I wanted it to be as easy to use as possible, if a users input was invalid in anyway I wanted to 
send back a response that would be user friendly and point them in the right direction on what went wrong in their request.
I was originally aiming for another two endpoints that would add more relational data, and make use of the relational database. 
Unfortunately as the data I extracted from the wiki was 'dirty data' and needed to be validated. I then scrapped a few fields that
would have utilized the relational database. I still feel as though there is enough there to showcase the API and sets a foundation 
add more.

#### Structure
- ##### Website
    For the index page of the website I wanted to keep it simple and straight to the point.

    At the top of the page is the navigation bar with the two pages linked, this changes into a hamburger
    button on smaller screens. Then I have a hero image with a jumbotron containing the sites name.

    The user is then presented with a search bar under the hero image. Right below that is the results 
    box which is pre-filled on the first load with the API's base url's resource. This is a directory
    of endpoints and their corresponding filters.

    Under the results is a short about section that gives a brief description of the API and it's resources.
    This is followed by "How to use" section which points the user the sites documentation for further information
    on the API and how to use it.

    On the documentation pages, the User is presented with a menu on the left and the main content on the right.
    The User can select any of the menu items and the page will scroll to the corresponding section.

    Finally in the footer we have social links to Github, Linkedin and the Github branch of this project.

- ##### API

    On a GET request of any of the endpoints resources the user will be presented with a JSON object, like the one below:
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

    Each endpoint has certain filters that the user can use to query specific resources.

    ##### Filters:
    ###### people:
    - offset:<br />
        As the default amount of results returned is 25, this allows users to get results beyond this point.<br /><br />
    - name:<br />
        Searches resources by its `name`, if blank will return all. If no match is found error message is returned.<br /><br />
    - status:<br />
        Searches resources by `status`, if input is not `alive`, `deceased` or `unknown` an error message will be returned.<br /><br />
    - gender:<br />
        Searches resources by `gender`, if input is not `male`, `female` or `unknown` an error message will be returned.<br />
    
    ###### locations:
    - offset:<br /><br />
    - name:<br /><br />
    - systems:<br />
        Searches resources by `system`, works similar to the `name` filter.<br />

    ###### systems:
    - offset:<br /><br />
    - name:<br /><br />

    For more information on these filters you can view the documentation on the website [here](https://expanse-api.herokuapp.com/documentation#filters).

    #### CRUD Functionality:
    ##### Website
    There is two ways to manipulate the data in the API, you can do it directly by sending HTTP requests to the API or
    you can use the website as an interface. On the website when the user goes to add or edit a resource they will be 
    provided with a form within the JSON result. I find this to be the easiest way for the user to understand what data
    needs to go where. To delete a resource the user simply has to search for the resource using the `id` and click delete.

    ##### Directly
    When a user wants to Add, Edit or Delete a resource using a direct path to the API. They simply need to send the keys/values
    in JSON format with the appropriate request method. Below I will give examples of what the request would look like for each
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

    If these requests are successful you will receive a JSON response back with a code and message. 
    Otherwise an error message will be sent back with details of what went wrong.

#### Skeleton
[Index Wireframe](https://github.com/gazzamc/Milestone-Project-Three/blob/master/wireframes/index.pdf)<br>
[docs Wireframe](https://github.com/gazzamc/Milestone-Project-Three/blob/master/wireframes/docs.pdf)<br>
[404 Wireframe](https://github.com/gazzamc/Milestone-Project-Three/blob/master/wireframes/404.pdf)<br>

#### Surface
I went with very neutral colours to make it look easy on the eye, as this is a simple
testing site for the API I didn't think it needed a lot to standout. The buttons are coloured
appropriately for what they do. Edit being yellow as a warning, delete being red etc. As
bootstrap had these built-in styles I didn't do anything custom in the CSS.

## Error Codes
Below is the full list of error codes used throughout the API.

| HTTP code 	| Message(s)                                              	| Further Info                         	|
|-----------	|---------------------------------------------------------	|--------------------------------------	|
| 200       	| N/A (Data shown)                                        	| Request Successful.                  	|
|           	| Record successfully deleted                             	|                                      	|
|           	| Record was successfully altered                         	|                                      	|
| 201       	| Record created in database                              	| Resource Created Successfully.       	|
| 204       	| Cannot delete record as it does not exist               	| No Content Found.                    	|
| 400       	| Bad Request. One or more fields not supplied or invalid 	| Client error, Usually input related. 	|
|           	| Bad Request. Data must be in JSON format                	|                                      	|
|           	| Bad Request. Status must be alive, deceased or unknown  	|                                      	|
|           	| Bad Request. Gender must be male, female or unknown     	|                                      	|
|           	| Bad Request. Query string unrecognised                  	|                                      	|
| 403       	| Duplicate, Record was not created in database           	| Request Forbidden.                   	|
| 404       	| Invalid EndPoint                                        	| Resource Not Found.                  	|
|           	| Record does not exist                                   	|                                      	|
|           	| Page does not exist                                     	|                                      	|
|           	| No records found for query {query}                      	|                                      	|
| 503       	| Cannot connect to database                              	| Server-Side Error                    	|

## Database schema
Below you can find the schema of each table along with the datatypes for each field.

|        	|      **people**      	|         	|                	|
|--------	|:----------------:	|---------	|----------------	|
| *Fields* 	|       *Type*       	|   *Key*   	|      *Extra*     	|
| id     	| int(11) unsigned 	| primary 	| auto_increment 	|
| name   	| varchar(50)      	|         	|                	|
| status 	| varchar(9)       	|         	|                	|
| gender 	| varchar(7)       	|         	|                	|
| desc   	| text             	|         	|                	|
<br />

|        	|      **locations**      	|         	|                	|
|--------	|:----------------:	|---------	|----------------	|
| *Fields* 	|       *Type*       	|   *Key*   	|      *Extra*     	|
| LocationID  | int(11) unsigned 	| primary 	| auto_increment 	|
| name   	| varchar(50)      	|         	|                	|
| population 	| varchar(20)       	|         	|                	|
| SystemID 	| int(11) unsigned 	|  Foreign	|                	|
| desc   	| text             	|         	|                	|
<br />

|        	|      **systems**      	|         	|                	|
|--------	|:----------------:	|---------	|----------------	|
| *Fields* 	|       *Type*       	|   *Key*   	|      *Extra*     	|
| SystemID     	| int(11) unsigned 	| primary 	| auto_increment 	|
| name   	| varchar(50)      	|         	|                	|
| desc   	| text             	|         	|                	|
| planets 	| int(3) unsigned 	|         	|                	|

As I'm using ClearDB on Heroku the auto_increment increases by '10', Unfortunately this
cannot be changed with the permissions I have to the database. But it doesn't affect the
application. This is just a note to explain the high count of ID's on the resources.

## Features
- Users can filter the data using *query strings*, such as by *name*, *status*, *gender* etc.
- Users can retrieve single records using the ID of said record in the URI.
- Users can Add, Edit and Delete records from the database.
- The API has input validation to prevent users from entering the wrong type of data.
- If there is an error processing the request the API will display an error code with an appropriate error message.
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
    - **MySQL** was used to store the tables and columns of data for the API.

- [Flask](https://palletsprojects.com/p/flask/)
    - **Flask** was used to create the endpoints, handle 404 pages and output the API data.

- [Javascript](https://www.javascript.com/)
    - **Javascript** was used to retrieve and send data to the API and hide/show elements.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - **CSS3** was used to add custom styles and positioning of the HTML elements.

- [Bootstrap](https://getbootstrap.com/)
    - **Bootstrap** was used to layout the basic structure of the website.

- [Font Awesome](https://fontawesome.com/)
    - **Font Awesome** is used for the logo icons.


## Testing
The website was tested in chrome, firefox and edge for responsiveness. 
The majority of my testing consisted of using the developer tools in chrome while working on the website design. 
As for testing the API endpoints I used the [**Postman Chrome Extension**](https://www.postman.com/), 
this allowed me to test all the different methods (GET, PUT, POST, DELETE) 
and check that I got the appropriate response back.

### Manual Testing
As I was building the website for the API I was able to extensively test it. Since I was connecting
to my API with JavaScript and retrieving the data as an end-user would. I was able to find some bugs that I
later patched and returned an appropriate responds code/message.

#### Website
On first load of the index page the results box is filled with the API's base urls resource. If I
search for any of the endpoints I get back the appropriate JSON data. This also adds a ADD RECORD button to
the bottom right of the results box (middle in smaller devices).

##### EndPoints
- Searching an invalid endpoint returns a `404` and a message in the results `"Invalid EndPoint"`.
- When searching a valid endpoint an *Add Resource* button will appear under the results.
    - Clicking this button will replace the JSON result with a form (With the same JSON layout, a drop down of `systems` appears when adding `location`).
        - A *Save* and *Cancel* button will appear below the results section.
            - Clicking the save button will bring up a modal to confirm the new resource.
                - If you fail to enter anything but `desc` an appropriate error message will appear below the results section.
                - If you fail to enter anything but `alive`, `deceased` or `unknown` in the `status` fields (`people`), 
                    an appropriate error message will appear below the results section.
                - If you fail to enter anything but `male`, `female` or `unknown` in the `gender` fields (`people`), 
                    an appropriate error message will appear below the results section.
                - If you fail to enter an `integer` in the `planets` field (`systems`), 
                    an appropriate error message will appear below the results section.
                - If you fail to enter a `string` containing a digit (first character is ignored incase of `<` `>` signs) in the `population` field (`locations`), 
                    an appropriate error message will appear below the results section.
                - If you successfully enter all necessary fields a success message `"Record created in database"` will appear in the results box.
    - Clicking the *Cancel* button will refresh the results and bring you back to the original endpoint results.
- When searching a specific resource using the `id` e.g.. `people/1`, Edit and Delete buttons will appear below the result.
    - When clicking the delete button a modal will appear to confirm the deletion of the resource.
        - If you click *YES* the modal will close and the resource will be deleted. A JSON message confirming that will appear in the results box.
        - If you click *NO* the modal will close.
    - If you click the *Edit* button, the JSON result will be replaced with a form but keeping the same structure. 
        The two previous buttons will disappear and a *Cancel* and *Save* button now appears below the result box.
        - If you click save without entering any information a modal will appear once again.
            - Clicking *YES* will make the modal disappear and an appropriate error message will appear below the results box.
        - If you click save and enter invalid data.
            - Clicking *YES* will make the modal disappear and an appropriate error message will appear below the results box.
        - If you click save and enter only one of the fields.
            - Clicking *YES* will make the modal disappear and successful message will appear in the results box in JSON format.
            - Any fields not entered wont be overwritten.
- If you input an invalid `id` in the endpoint you will get a `404` message `"Record does not exist"`.
- If you input an `id` that isn't an integer you will get a `400` message `"Bad Request. ID must be an integer"`.

##### Filters
- Searching an endpoint with an invalid filter will return a `400` message `"Bad Request. Query string unrecognised"`.
- If the query you used for the filter can't find a record it will return a `404` message `"No records found for query '{query}'"`.
- If you use the pagination filter `offset` and go out of range of the results you will get a `404` error message `"Page does not exist"`.
- If your filter search is successful you will get a `count` of the resources matching your query. The `id` and the `name` of the query in JSON (`status`, `gender` and `system` will also be included when searched).
    - Except for the `offset` filter, this will simply show you the next 25 results after your set offset. So it will return like a normal endpoint search.

##### Site functionality
- All links were tested and they work as intended, all external links have `target="_blank"` and open a separate tab.
- All menu links on the documentation page scroll to the appropriate content.
- All elements are responsive when changing resolutions in chrome dev tools.
- Example code/JSON scales with resolution on documentation page.
- Back to top button works as intended and doesn't block content.
- No elements/content overlaps when changing resolutions.

#### API

#### Bugs
- In the lowest breakpoint in the chrome dev tools the search bar is misaligned.

### Automated Testing
I did do some basic unit testing using pythons *unittest* and *nose* modules.
These tests can be found in the `api_test.py` file. In order to run these tests 
you will need to connect to a working database to get the appropriate response that
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

I only tested the API endpoints using the **GET** method. As I was connected to my live
database I didn't want to automate tests that would alter or delete records. Unfortunately I couldn't find a way to setup a temporary database for testing my **CRUD** functionality. The
closest thing I found for database testing was a **Mock** module which didn't suit my needs. 
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
- [This](http://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/) article helped me understant the unittest module and allowed me to do my own tests.
- [This](https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript) exampled helped me prettify the JSON data when outputting it to the end user.
- [This](https://stackoverflow.com/questions/8866053/stop-reloading-page-with-enter-key) example helped me stop the page from reloading when the user pressed the enter key in the search bar.
- [This](https://stackoverflow.com/questions/42050765/sql-how-to-replace-foreign-key-column-with-data-from-referenced-table) example helped me with joining data between tables
- [This](https://stackoverflow.com/questions/37255313/what-is-a-right-way-for-rest-api-response) helped me when trying to figure out the right way to respond to certain requests.
- [This](https://stackoverflow.com/questions/16908943/display-json-returned-from-flask-in-a-neat-way) helped when trying to return the JSON with the correct indentation in the flask response
- I would also like to thank my Mentor Aaron Sinnott for letting me know about the fetch() function when calling the API.
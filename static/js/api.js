/**
 * api.js
 * This file contains all the API
 * calls for each HTTP request methods
 */


/**
 * This functions calls the API
 * and returns the response JSON data.
 * @param {string} endpoint 
 * @param {string} method 
 * @param {JSON Object} data 
 * @function apiCall
 */
async function apiCall(endpoint="", method='GET', data=null){
    let response;
    let jsonResult;
    let headers;
    let options;

    if (endpoint != ""){
        endpoint = "/" + endpoint;
    }

    headers = {'Content-Type': 'application/json'};
    options = {method: method, headers: headers, body: data};
    response = await fetch(baseUrl + endpoint, options);
    jsonResult = await response.json();

    return jsonResult;
}

/**
 * Gets the JSON data of the corresponding
 * endpoint then displays it in the results
 * box. Hides/Shows buttons depending on the
 * results fetched.
 * @param {string} endpoint 
 * @function getData
 */
async function getData(endpoint=""){

    let jsonResult = await apiCall(endpoint);

    /* Check if single record, then show buttons */
    /* https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript */
    document.getElementById("jsonRes").innerText = JSON.stringify(jsonResult, null, 2);

    if(jsonResult.results == 1){
        if(addBtn.offsetLeft > 0 || saveBtn.offsetLeft > 0 ||
            cancelBtn.offsetLeft > 0){
            toggleBtn(addBtn, "hide");
            toggleBtn(saveBtn, "hide");
            toggleBtn(cancelBtn, "hide");
        }

        toggleBtn(editBtn, "show");
        toggleBtn(deleteBtn, "show");

    } else if (jsonResult.results > 1){
        toggleBtn(addBtn, "show");

        if(editBtn.offsetLeft > 0 || deleteBtn.offsetLeft > 0 ||
        saveBtn.offsetLeft > 0 || cancelBtn.offsetLeft > 0){
            toggleBtn(editBtn, "hide");
            toggleBtn(saveBtn, "hide");
            toggleBtn(deleteBtn, "hide");
            toggleBtn(cancelBtn, "hide");
        }
    }else{
        if(addBtn.offsetLeft > 0 || editBtn.offsetLeft > 0 || 
        deleteBtn.offsetLeft > 0 || saveBtn.offsetLeft > 0){
            toggleBtn(addBtn, "hide");
            toggleBtn(editBtn, "hide");
            toggleBtn(saveBtn, "hide");
            toggleBtn(deleteBtn, "hide");
        }
    }

    /* Remove error message if still showing */
    if(document.getElementById("errMess").innerText != undefined){
        document.getElementById("errMess").innerText = "";
    }
}

/**
 * This function takes the inputted data
 * from the edit/add forms and sends the 
 * request to apiCall function.
 * @param {Boolean} newRec
 * @function editRecord 
 */
async function editRecord(newRec=false){

    let data = {};
    let method = 'PUT';
    
    if(!newRec){
        data.id = parseInt(endpointDataSplt[1]);
    }else{
        method = 'POST';
    }

    data.name = document.getElementById("name").value.toLowerCase();
    data.desc = document.getElementById("desc").value.toLowerCase();

    if(endpoint == "people"){
        data.status = document.getElementById("status").value.toLowerCase();
        data.gender = document.getElementById("gender").value.toLowerCase();

    } else if(endpoint == "locations"){
        data.population = document.getElementById("pop").value;
        data.system = document.getElementById("system").value;

    } else if(endpoint == "systems"){
        data.planets = parseInt(document.getElementById("planets").value);

    }

    let json = JSON.stringify(data);
    let jsonResult = await apiCall(endpoint, method, json);

    if(jsonResult.code == 200 || jsonResult.code == 201){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("saveBtn").className = "hideBtn";
    } else{
        document.getElementById("errMess").innerHTML = jsonResult.message;
    }
}

/**
 * This function send the delete
 * request to the apiCall function
 * @function deleteRecord
 */
async function deleteRecord(){

    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    let json = JSON.stringify(data);
    let jsonResult = await apiCall(endpoint, 'DELETE', json);

    if(jsonResult.code == 200){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("editBtn").className = "hideBtn";
        document.getElementById("deleteBtn").className = "hideBtn";
    } else{
        document.getElementById("errMess").innerHTML = "There was an issue deleting the record";
    }
}

/**
 * This function fetches the 
 * system names from apiCall and 
 * returns them in an array.
 * @function getSystemNames
 */
async function getSystemNames() {

    let response = await fetch(baseUrl + "/systems");
    let tempsysNames = await response.json();
    
    return tempsysNames.data;
}
async function apiCall(endpoint="", method='GET', data=null){
    let response;
    let jsonResult;
    let headers;
    let options;

    if (endpoint != ""){
        endpoint = "/" + endpoint
    }

    headers = {'Content-Type': 'application/json'};
    options = {method: method, headers: headers, body: data};
    response = await fetch(baseUrl + endpoint, options);
    jsonResult = await response.json();

    return jsonResult;
}

async function getData(endpoint=""){

    let jsonResult = await apiCall(endpoint);

    /* Check if single record, then show buttons */
    /* https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript */
    document.getElementById("jsonRes").innerText = JSON.stringify(jsonResult, null, 2);

        if(jsonResult['results'] == 1){
            if(document.getElementById("addBtn").offsetLeft > 0 ||
                document.getElementById("saveBtn").offsetLeft > 0){
                document.getElementById("addBtn").className = "hideBtn";
                document.getElementById("saveBtn").className = "hideBtn";
            }

            document.getElementById("editBtn").className = "showBtn";
            document.getElementById("deleteBtn").className = "showBtn";

        } else if (jsonResult['results'] > 1){
            document.getElementById("addBtn").className = "showBtn";

            if(document.getElementById("editBtn").offsetLeft > 0 || 
            document.getElementById("deleteBtn").offsetLeft > 0 ||
            document.getElementById("saveBtn").offsetLeft > 0){
                document.getElementById("editBtn").className = "hideBtn";
                document.getElementById("deleteBtn").className = "hideBtn"; 
                document.getElementById("saveBtn").className = "hideBtn";
            }
        }else{
            if(document.getElementById("addBtn").offsetLeft > 0 || 
            document.getElementById("editBtn").offsetLeft > 0 || 
            document.getElementById("deleteBtn").offsetLeft > 0 ||
            document.getElementById("saveBtn").offsetLeft > 0){
                document.getElementById("addBtn").className = "hideBtn";  
                document.getElementById("editBtn").className = "hideBtn";
                document.getElementById("deleteBtn").className = "hideBtn"; 
                document.getElementById("saveBtn").className = "hideBtn";
            }
        }
}

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

    if(jsonResult['code'] == 200 || jsonResult['code'] == 201){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("saveBtn").className = "hideBtn";
    } else{
        document.getElementById("errMess").innerHTML = jsonResult['message'];
    }
}

async function deleteRecord(){

    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    let json = JSON.stringify(data);
    let jsonResult = await apiCall(endpoint, 'DELETE', json);

    if(jsonResult['code'] == 200){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("editBtn").className = "hideBtn";
        document.getElementById("deleteBtn").className = "hideBtn";
    } else{
        document.getElementById("errMess").innerHTML = "There was an issue deleting the record"
    }
}

async function getSystemNames() {

    let response = await fetch(baseUrl + "/systems");
    let tempsysNames = await response.json();
    
    return tempsysNames['data'];
}
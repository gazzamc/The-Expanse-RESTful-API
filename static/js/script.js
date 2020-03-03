var baseUrl = window.location.href + "api";
baseUrl = baseUrl.replace("?", "").replace("#", "");
var endpoint;
var endpointDataSplt;
var headers = {'Content-Type': 'application/json'};

async function getData(endpoint=""){
    let response;
    let jsonResult;

    if (endpoint != ""){
        endpoint = "/" + endpoint
    }

        response = await fetch(baseUrl + endpoint);
        jsonResult = await response.json();

    /* Check if single record, then show buttons */
    /* https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript */
    document.getElementById("jsonRes").innerText = JSON.stringify(jsonResult,null,2);

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

function showEdit(){
    let jsonResult = document.getElementById("jsonRes").innerHTML;
    let splitBr = jsonResult.split("<br>");
    let replaceText;
    let textBoxHTML;

    splitBr.forEach((value, index) => {
        if(endpoint == "people"){
            if(index == 6){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="name" placeholder='+ replaceText +'></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 7){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="status" placeholder='+ replaceText +'></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 8){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    if(!isNaN(replaceText)){
                        replaceText = "\"" + replaceText + "\"";
                    }
                    textBoxHTML = '<input type="text" id="gender" placeholder='+ replaceText +'></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 9){
                    origText = splitBr[index].split(":")[1];
                    replaceText = splitBr[index].split(":")[1].replace('\\"', '').replace('\\"', '').split("\"")[1];
                    textBoxHTML = '"<textArea rows="4" cols="50" id="desc" placeholder="'+ replaceText +'"></textArea>"';
                    jsonResult = jsonResult.replace(origText, textBoxHTML);
            }
        }else if(endpoint == "systems"){
            if(index == 6){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="name" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 7){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    replaceText.replace('"', '');
                    textBoxHTML = '<textArea rows="4" cols="50" id="desc" placeholder="'+ replaceText +'"></textArea>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 8){
                    replaceText = splitBr[index].split(":")[1].replace(",", "");
                    textBoxHTML = '<input type="text" id="planets" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
        }
    });

    document.getElementById("jsonRes").innerHTML = jsonResult;
    document.getElementById("editBtn").className = "hideBtn";
    document.getElementById("deleteBtn").className = "hideBtn";
    document.getElementById("saveBtn").className = "showBtn";
}

async function editRecord(){

    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    data.name = document.getElementById("name").value.toLowerCase();
    data.desc = document.getElementById("desc").value.toLowerCase();

    if(endpoint == "people"){
        data.status = document.getElementById("status").value.toLowerCase();
        data.gender = document.getElementById("gender").value.toLowerCase();

    } else if(endpoint == "locations"){
        data.population = document.getElementById("population").value;
        data.systemId = document.getElementById("systemsId").value;

    } else if(endpoint == "systems"){
        data.planets = document.getElementById("planets").value;

    }

    let options = {method: 'PUT', headers: headers, body: json};
    let json = JSON.stringify(data);
    let response = await fetch(baseUrl + "/" + endpoint, options);
    let jsonResult = await response.json();

    if(jsonResult['code'] == 200){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("saveBtn").className = "hideBtn";
    } else{
        document.getElementById("errMess").innerHTML = jsonResult['message'];
    }
}

function deleteRecord(){

/*     request.open('DELETE', baseUrl + "/" + endpointDataSplt[0], true)
    request.setRequestHeader('Content-type','application/json; charset=utf-8'); */

    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    let json = JSON.stringify(data);

    let response = fetch(baseUrl + "/" + endpoint, {method: 'DELETE', json});
    let jsonResult = response.json();

    if(jsonResult['code'] == 200){
        document.getElementById("jsonRes").innerHTML = JSON.stringify(jsonResult,null,2);
        document.getElementById("editBtn").className = "hideBtn";
        document.getElementById("deleteBtn").className = "hideBtn";
    } else{
        console.log(jsonResult);
        document.getElementById("errMess").innerHTML = "There was an issue deleting the record"
    }

/*     request.onload = function(){
        if(request.status == 200){
            let jsonRes = JSON.parse(this.response);
            if(jsonRes['code'] == 200){
                document.getElementById("jsonRes").innerHTML = JSON.stringify(JSON.parse(this.response),null,2);
                document.getElementById("editBtn").className = "hideBtn";
            	document.getElementById("deleteBtn").className = "hideBtn";
            } else{
                document.getElementById("errMess").innerHTML = "There was an issue deleting the record"
            }
        }
    }
    request.send(json); */
}

async function getSystemNames() {

    let response = await fetch(baseUrl + "/systems");
    let tempsysNames = await response.json();
    
    return tempsysNames['data'];
}

async function addRecord(){
    if(endpoint == "people"){

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "status": "<input type=" + "text" + " id=" + "status" + "></input>",
            "gender": "<input type=" + "text" + " id=" + "gender" + "></input>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        }

    } else if(endpoint == "locations"){
        let systems = await getSystemNames();
        let dropdown = "";

        systems.forEach(element => {
            dropdown += "<option value=" + element['name'] + ">" + element['name'] + "</option>";
        });

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "population": "<input type=" + "text" + " id=" + "pop" + "></input>",
            "system": "<select id=" + "system" + ">" + dropdown + "</select>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        }

    } else if(endpoint == "systems"){
        form = {
            "name": "<input type=\"text\" id=\"name\"></input>",
            "planets": "<input type=\"text\" id=\"planets\"></input>",
            "desc": "<textArea rows=\"4\" cols=\"50\" id=\"desc\"></textArea>",
        }

    }

    document.getElementById("jsonRes").innerHTML = JSON.stringify(form, null, 2);
}

/* Button event Listeners */
/* https://stackoverflow.com/questions/8866053/stop-reloading-page-with-enter-key */
document.getElementById("apiSearchForm").addEventListener("submit", function(e){

    let endpointData = document.getElementById("apiSearch").value;

    /* validate input */
    endpointDataSplt = endpointData.split("/");
    endpoint = endpointDataSplt[0];

    if(endpoint != "people" && endpoint != "systems" && endpoint != "locations"){
        endpoint = ""
    }

    getData(endpointData);
    e.preventDefault();
}, false);

document.getElementById("editBtn").addEventListener("click", function(){
    showEdit();
});

document.getElementById("addBtn").addEventListener("click", function(){
    addRecord();
    document.getElementById("saveBtn").className = "showBtn";
    document.getElementById("addBtn").className = "hideBtn";
});

document.getElementById("saveBtn").addEventListener("click", function(){
    if(document.getElementById("errMess").innerText != undefined){
        document.getElementById("errMess").innerText = "";
    }

    if(endpointDataSplt[1] == undefined){
        if(confirm("Are you sure you want to add this record?")){
            "editRecord();"
        }
    }else{
        if(confirm("Are you sure you want to edit this record?")){
            editRecord();
        }
    }
});

document.getElementById("deleteBtn").addEventListener("click", function(){
    if(confirm("Are you sure you want to delete this record?")){
        deleteRecord();
    }
});


window.onload = getData();
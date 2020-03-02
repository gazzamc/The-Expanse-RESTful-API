var request = new XMLHttpRequest();
var baseUrl = window.location.href + "api";
var endpoint;
var endpointDataSplt;

baseUrl = baseUrl.replace("?", "").replace("#", "");

function getData(endpoint=""){
    if (endpoint != ""){
        endpoint = "/" + endpoint
    }

    request.open('GET', baseUrl + endpoint, true)

    request.onload = function(){

        if(request.status == 200){
            /* Check if single record, then show buttons */
            let results = JSON.parse(this.response);

            /* https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript */
            document.getElementById("jsonRes").innerText = JSON.stringify(results,null,2);

            if(results['results'] == 1){
                if(document.getElementById("addBtn").offsetLeft > 0){
                    document.getElementById("addBtn").className = "hideBtn";
                }
                if(document.getElementById("saveBtn").offsetLeft > 0){
                    document.getElementById("saveBtn").className = "hideBtn";
                }
                document.getElementById("editBtn").className = "showBtn";
                document.getElementById("deleteBtn").className = "showBtn";
            } else if (results['results'] > 1){
                document.getElementById("addBtn").className = "showBtn";
            }
        }
    }

    request.send();
}
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

function editRecord(){
    request.open('PUT', baseUrl + "/" + endpointDataSplt[0], true)
    request.setRequestHeader('Content-type','application/json; charset=utf-8');
    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    data.name = document.getElementById("name").value;
    data.desc = document.getElementById("desc").value;

    if(endpoint == "people"){
        data.status = document.getElementById("status").value;
        data.gender = document.getElementById("gender").value;

    } else if(endpoint == "locations"){
        data.population = document.getElementById("population").value;
        data.systemId = document.getElementById("systemsId").value;
    } else if(endpoint == "systems"){
        data.planets = document.getElementById("planets").value;
    }

    let json = JSON.stringify(data);

    request.onload = function(){
        if(request.status == 200){
            let jsonRes = JSON.parse(this.response);
            if(jsonRes['code'] == 200){
                document.getElementById("jsonRes").innerHTML = JSON.stringify(JSON.parse(this.response),null,2);
                document.getElementById("saveBtn").className = "hideBtn";
            } else{
                document.getElementById("errMess").innerHTML = jsonRes['message'];
            }
        }
    }
    request.send(json);

/*     document.getElementById("saveBtn").className = "hideBtn";
    document.getElementById("jsonRes").innerHTML = "Saved!" */

}

function deleteRecord(){
    request.open('DELETE', baseUrl + "/" + endpointDataSplt[0], true)
    request.setRequestHeader('Content-type','application/json; charset=utf-8');

    let data = {};
    data.id = parseInt(endpointDataSplt[1]);
    let json = JSON.stringify(data);

    request.onload = function(){
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
    request.send(json);
}

/* Button event Listeners */
document.getElementById("editBtn").addEventListener("click", function(){
    showEdit();
});

document.getElementById("saveBtn").addEventListener("click", function(){
    if(document.getElementById("errMess").innerText != undefined){
        document.getElementById("errMess").innerText = "";
    }
    
    if(confirm("Are you sure you want to edit this record?")){
        editRecord();
    }
});

document.getElementById("deleteBtn").addEventListener("click", function(){
    if(confirm("Are you sure you want to delete this record?")){
        deleteRecord();
    }
});


window.onload = getData();
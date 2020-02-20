var request = new XMLHttpRequest();
var baseUrl = window.location.href + "api/";

baseUrl = baseUrl.replace("?", "").replace("#", "");

function getData(endpoint="people"){
    request.open('GET', baseUrl + endpoint, true)

    request.onload = function(){

        if(request.status == 200){
            document.getElementById("jsonRes").innerText = this.response;
        }
    }

    request.send();
}

document.getElementById("apiSearchForm").addEventListener("submit", function(e){

    let endpointData = document.getElementById("apiSearch").value;

    /* validate input */
    endpointDataSplt = endpointData.split("/");
    endpoint = endpointDataSplt[0];

    if(endpoint != "people" && endpoint != "systems" && endpoint != "planets"){
        endpoint = ""
    }

    getData(endpointData);
    e.preventDefault();
}, false);

window.onload = getData();
var request = new XMLHttpRequest();
var baseUrl = window.location.href + "api";

baseUrl = baseUrl.replace("?", "").replace("#", "");

function getData(endpoint=""){
    if (endpoint != ""){
        endpoint = "/" + endpoint
    }

    request.open('GET', baseUrl + endpoint, true)

    request.onload = function(){

        if(request.status == 200){
            /* https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript */
            document.getElementById("jsonRes").innerText = JSON.stringify(JSON.parse(this.response),null,2); ;
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

window.onload = getData();
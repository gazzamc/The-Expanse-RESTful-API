// declare baseUrl variable
let baseUrl = "https://8080-a33b8b63-0e2e-4354-8ba2-ab17d2c1ce1a.ws-eu01.gitpod.io/api";

// Functions that takes in the endpoint, method (default=GET) and JSON data.
async function apiCall(endpoint = "", method = 'GET', data = null) {
    // declare local variables
    let response;
    let jsonResult;
    let headers;
    let options;

    // Add trailing slash if endpoint is not empty
    if (endpoint != "") {
        endpoint = "/" + endpoint;
    }

    // set content type to JSON
    headers = { 'Content-Type': 'application/json' };
    //Set options for request
    options = { method: method, headers: headers, body: data };
    // fetch results, add await to wait for results to return
    response = await fetch(baseUrl + endpoint, options);
    // Unpack JSON result
    jsonResult = await response.json();

    // Return JSON result
    return jsonResult;
}

// call function
// since its a get request theres no need for the last two params
async function getFirstPerson(){
    let people = await apiCall("people");
    console.log(JSON.stringify(people.data[0]));
}

document.getElementById("backToTop").addEventListener("click", function(){
    getFirstPerson();
});
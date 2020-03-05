var baseUrl = window.location.href + "api";
baseUrl = baseUrl.replace("?", "").replace("#", "");
var endpoint;
var endpointDataSplt;

window.onload = getData();
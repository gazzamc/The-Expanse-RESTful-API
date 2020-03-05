var baseUrl = window.location.href + "api";
baseUrl = baseUrl.replace("?", "").replace("#", "");
var endpoint;
var endpointDataSplt;
var addBtn = document.getElementById("addBtn");
var saveBtn = document.getElementById("saveBtn");
var editBtn = document.getElementById("editBtn");
var cancelBtn = document.getElementById("cancelBtn");
var deleteBtn = document.getElementById("deleteBtn");

window.onload = getData();
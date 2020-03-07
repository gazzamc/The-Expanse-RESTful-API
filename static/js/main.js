/**
 * main.js
 * This holds all the global variables and calls
 * the api on window load.
 */

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
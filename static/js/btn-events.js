/***
 * btn-events.js
 * This file contains all the event
 * listeners for the button clicks
 */

/**
 * This function hides/shows the
 * buttons on the website
 * @param {Object} button 
 * @param {String} toggle 
 * @function toggleBtn
 */
function toggleBtn(button, toggle){

    if(toggle == "show"){
       button.classList.remove("hideBtn");
       button.classList.add("showBtn");
    } else{
       button.classList.remove("showBtn");
       button.classList.add("hideBtn");
    }
}

/* Button event Listeners */
/* https://stackoverflow.com/questions/8866053/stop-reloading-page-with-enter-key */

/* Search Box */
document.getElementById("apiSearchForm").addEventListener("submit", function(e){

    let endpointData = document.getElementById("apiSearch").value;

    /* validate input */
    endpointDataSplt = endpointData.split("/");
    endpoint = endpointDataSplt[0];

    if(endpoint != "people" && endpoint != "systems" && endpoint != "locations"){
        endpoint = "";
    }

    getData(endpointData);
    e.preventDefault();
}, false);

/* Edit Btn */
editBtn.addEventListener("click", function(){
    showEdit();
});

/* Add Btn */
addBtn.addEventListener("click", function(){
    showAddRecord();
    toggleBtn(saveBtn, "show");
    toggleBtn(cancelBtn, "show");
    toggleBtn(addBtn, "hide");
});

/* Save Btn */
saveBtn.addEventListener("click", function(){
    if(document.getElementById("errMess").innerText != undefined){
        document.getElementById("errMess").innerText = "";
    }

    if(endpointDataSplt[1] == undefined){
        /* Change modal content */
        document.getElementById("modalTitle").innerText = "Add Resource";
        document.getElementById("modalBody").innerText = "Are you sure you want to add this resource?";
        document.getElementById("modal").style.display = "inherit";
    }else{
        /* Change modal content */
        document.getElementById("modalTitle").innerText = "Edit Resource";
        document.getElementById("modalBody").innerText = "Are you sure you want to edit this resource?";
        document.getElementById("modal").style.display = "inherit";
    }
});

/* Delete Btn */
deleteBtn.addEventListener("click", function(){
    /* Change modal content */
    document.getElementById("modalTitle").innerText = "Delete Resource";
    document.getElementById("modalBody").innerText = "Are you sure you want to delete this resource?";
    document.getElementById("modal").style.display = "inherit";
});

/* Cancel Btn */
cancelBtn.addEventListener("click", function(){
    let endpointData;

    if(endpointDataSplt[1] == undefined){
        endpointData = endpointDataSplt[0];
    }else{
        endpointData = endpointDataSplt[0] + "/" + endpointDataSplt[1];
    }

    getData(endpointData);
});

/* Modal buttons */
/* Yes */
document.getElementById("modalYes").addEventListener("click", function(){
    document.getElementById("modal").style.display = "none";

    if(endpointDataSplt[1] == undefined){
        editRecord(true);
    }else{
        if(editBtn.offsetLeft > 0){
            deleteRecord();
        }else{
            editRecord();
        }
    }
});
/* No */
document.getElementById("modalNo").addEventListener("click", function(){
    document.getElementById("modal").style.display = "none";
});
/* Close */
document.getElementById("modalClose").addEventListener("click", function(){
    document.getElementById("modal").style.display = "none";
});
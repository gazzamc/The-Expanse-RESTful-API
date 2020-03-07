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
        if(confirm("Are you sure you want to add this record?")){
            editRecord(true);
        }
    }else{
        if(confirm("Are you sure you want to edit this record?")){
            editRecord();
        }
    }
});

/* Delete Btn */
deleteBtn.addEventListener("click", function(){
    if(confirm("Are you sure you want to delete this record?")){
        deleteRecord();
    }
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
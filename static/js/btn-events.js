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
    showAddRecord();
    toggleBtn(saveBtn, "show");
    toggleBtn(cancelBtn, "show");
    toggleBtn(addBtn, "hide");
});

document.getElementById("saveBtn").addEventListener("click", function(){
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

document.getElementById("deleteBtn").addEventListener("click", function(){
    if(confirm("Are you sure you want to delete this record?")){
        deleteRecord();
    }
});

document.getElementById("cancelBtn").addEventListener("click", function(){
    let endpointData;

    if(endpointDataSplt[1] == undefined){
        endpointData = endpointDataSplt[0];
    }else{
        endpointData = endpointDataSplt[0] + "/" + endpointDataSplt[1];
    }

    getData(endpointData);
});
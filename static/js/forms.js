/***
 * forms.js
 * This contains all the functions that
 * transforms the JSON data into a form
 * when a user clicks the edit/add buttons.
 */

/**
 * This function splits the JSON data by <br> element,
 * then loops through and replaces the JSON value
 * with an input field and the original value as placeholder.
 * @function showEdit
 */
async function showEdit(){
    let jsonResult = document.getElementById("jsonRes").innerHTML;
    let splitBr = jsonResult.split("<br>");
    let replaceText;
    let textBoxHTML;
    let systems;
    let dropdown;
    let id;

    /* get system names before loop for drop down*/
    if(endpoint == "locations"){
        systems = await getSystemNames();
        dropdown = "";

        systems.forEach(element => {
            dropdown += "<option value=" + element.name + ">" + element.name + "</option>";
        });
    }

    /* looping through array of JSON data */
    splitBr.forEach((value, index) => {
        try{
            /* Setting input fields to replace later */
            replaceText = splitBr[index].split(":")[1];
            inputHTML = '<input type="text" id="{n}" placeholder="{r}"></input>';
            textBoxHTML = '<textArea rows="4" cols="50" id="{n}" placeholder="{r}"></textArea>';

        }catch(TypeError){}
            if(index == 6){
                    inputHTML = inputHTML.replace("{n}", "name").replace("{r}", replaceText.split("\"")[1]);
                    jsonResult = jsonResult.replace(replaceText, inputHTML);
            }
            else if(index == 7){
                    if(endpoint == "people" ||  endpoint == "locations"){
                        if(endpoint == "people"){
                            id = "status";
                        }else{
                            id = "population";
                        }
                        replaceText = replaceText.split("\"")[1];
                    }
                    else if(endpoint == "systems"){
                        id = "planets";
                        replaceText = replaceText.replace(",", "");
                    } 

                    inputHTML = inputHTML.replace("{n}", id).replace("{r}", replaceText);
                    jsonResult = jsonResult.replace(replaceText, inputHTML);
            }
            else if(index == 8){
                    if(endpoint == "people"){
                        id = "gender";
                        replaceText = replaceText.split("\"")[1];
                    }
                    else if(endpoint == "systems"){
                        id = "desc";
                        replaceText = replaceText.split("\"")[1].replace('"', '');
                        inputHTML = textBoxHTML;
                    }
                    else if(endpoint == "locations"){
                        replaceText = replaceText.replace(",", "");
                    } 

                    if(endpoint != "locations"){
                        inputHTML = inputHTML.replace("{n}", id).replace("{r}", replaceText);
                    } else{
                        inputHTML = '<select id="system">" '+ dropdown +' "</select>';
                    }
                    jsonResult = jsonResult.replace(replaceText, inputHTML);
            }
            else if(index == 9){
                id = "desc";
                inputHTML = textBoxHTML;

                if(endpoint == "people"){
                    origText = replaceText;
                    replaceText = replaceText.replace('\\"', '').replace('\\"', '').split("\"")[1];
                } else if(endpoint == "locations"){
                    replaceText = replaceText.split("\"")[1].replace('"', '');
                }

                textBoxHTML = inputHTML.replace("{n}", id).replace("{r}", replaceText);

                if(endpoint == "locations"){
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
                } else if(endpoint == "people"){
                   jsonResult = jsonResult.replace(origText, textBoxHTML);
                }
            }
    });

    document.getElementById("jsonRes").innerHTML = jsonResult;
    toggleBtn(editBtn, "hide");
    toggleBtn(deleteBtn, "hide");
    toggleBtn(saveBtn, "show");
    toggleBtn(cancelBtn, "show");
}

/**
 * When clicked this replaces the JSON
 * with input values, depending the endpoint
 * these fields will vary.
 * @function showEdit
 */
async function showAddRecord(){
    if(endpoint == "people"){

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "status": "<input type=" + "text" + " id=" + "status" + "></input>",
            "gender": "<input type=" + "text" + " id=" + "gender" + "></input>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        };

    } else if(endpoint == "locations"){
        let systems = await getSystemNames();
        let dropdown = "";

        systems.forEach(element => {
            dropdown += "<option value=" + element.name + ">" + element.name + "</option>";
        });

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "population": "<input type=" + "text" + " id=" + "pop" + "></input>",
            "system": "<select id=" + "system" + ">" + dropdown + "</select>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        };

    } else if(endpoint == "systems"){
        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "planets": "<input type=" + "text" + " id=" + "planets" + "></input>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        };

    }
    document.getElementById("jsonRes").innerHTML = JSON.stringify(form, null, 2);
}
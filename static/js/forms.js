/***
 * forms.js
 * This contains all the functions that
 * transforms the JSON data into a form
 * when a user edits/adds new data.
 */

async function showEdit(){
    let jsonResult = document.getElementById("jsonRes").innerHTML;
    let splitBr = jsonResult.split("<br>");
    let replaceText;
    let textBoxHTML;
    let systems;
    let dropdown;

    /* get system names before loop */
    if(endpoint == "locations"){
        systems = await getSystemNames();
        dropdown = "";

        systems.forEach(element => {
            dropdown += "<option value=" + element['name'] + ">" + element['name'] + "</option>";
        });
    }

    splitBr.forEach((value, index) => {
        if(endpoint == "people"){
            if(index == 6){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="name" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 7){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="status" placeholder='+ replaceText +'></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 8){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    if(!isNaN(replaceText)){
                        replaceText = "\"" + replaceText + "\"";
                    }
                    textBoxHTML = '<input type="text" id="gender" placeholder='+ replaceText +'></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 9){
                    origText = splitBr[index].split(":")[1];
                    replaceText = splitBr[index].split(":")[1].replace('\\"', '').replace('\\"', '').split("\"")[1];
                    textBoxHTML = '"<textArea rows="4" cols="50" id="desc" placeholder="'+ replaceText +'"></textArea>"';
                    jsonResult = jsonResult.replace(origText, textBoxHTML);
            }
        }else if(endpoint == "systems"){
            if(index == 6){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="name" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 7){
                    replaceText = splitBr[index].split(":")[1].replace(",", "");
                    textBoxHTML = '<input type="text" id="planets" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 8){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    replaceText.replace('"', '');
                    textBoxHTML = '<textArea rows="4" cols="50" id="desc" placeholder="'+ replaceText +'"></textArea>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
        } else if(endpoint == "locations"){
            if(index == 6){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="name" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            if(index == 7){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    textBoxHTML = '<input type="text" id="population" placeholder="'+ replaceText +'"></input>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 8){
                    replaceText = splitBr[index].split(":")[1].replace(",", "");
                    textBoxHTML = '<select id="system">" '+ dropdown +' "</select>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
            else if(index == 9){
                    replaceText = splitBr[index].split(":")[1].split("\"")[1];
                    replaceText.replace('"', '');
                    textBoxHTML = '<textArea rows="4" cols="50" id="desc" placeholder="'+ replaceText +'"></textArea>';
                    jsonResult = jsonResult.replace(replaceText, textBoxHTML);
            }
        }
        
    });

    document.getElementById("jsonRes").innerHTML = jsonResult;
    toggleBtn(editBtn, "hide");
    toggleBtn(deleteBtn, "hide");
    toggleBtn(saveBtn, "show");
    toggleBtn(cancelBtn, "show");
}

async function showAddRecord(){
    if(endpoint == "people"){

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "status": "<input type=" + "text" + " id=" + "status" + "></input>",
            "gender": "<input type=" + "text" + " id=" + "gender" + "></input>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        }

    } else if(endpoint == "locations"){
        let systems = await getSystemNames();
        let dropdown = "";

        systems.forEach(element => {
            dropdown += "<option value=" + element['name'] + ">" + element['name'] + "</option>";
        });

        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "population": "<input type=" + "text" + " id=" + "pop" + "></input>",
            "system": "<select id=" + "system" + ">" + dropdown + "</select>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        }

    } else if(endpoint == "systems"){
        form = {
            "name": "<input type=" + "text" + " id=" + "name" + "></input>",
            "planets": "<input type=" + "text" + " id=" + "planets" + "></input>",
            "desc": "<textArea rows=" + "4" + " cols=" + "50" + " id=" + "desc" + "></textArea>"
        }

    }

    document.getElementById("jsonRes").innerHTML = JSON.stringify(form, null, 2);
}
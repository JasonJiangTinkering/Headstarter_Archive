var els = document.getElementsByClassName("random_color");
for (var i = 0; i < els.length; i++) {
    let randomColor = Math.floor(Math.random()*16777215).toString(16);
    els.item(i).style.backgroundColor = "#" + randomColor;
}


function loadFile(url, callback) {
    return PizZipUtils.getBinaryContent(url, callback);
}
// Parse Resumes and add them to the sortable list
for (const i in users){
    const text = loadFile(
        '/media/'+ users[i].resume,
        function (error, content) {
            
            if (error) {
                throw error;
            }
            var zip = new PizZip(content);
            var doc = new window.docxtemplater(zip);
            return parse_doc(doc.getFullText(), i, '/media/'+ users[i].resume); 
        }
    );}

function parse_doc(text, i, link) {
    console.log(text);
    users[i]["keywords"] = {}
    totalScore = 0;
    for (const [key, value] of Object.entries(weighting)){
        // major catagories
        major_catagory_title = key;
        major_catagory_weight = value[0];
        major_sumed_reward = 0
        users[i]["keywords"][major_catagory_title] = [0, {}]
        for (const [small_key, small_value] of Object.entries(value[1])){
            minor_title = small_key;
            minor_regex = new RegExp(small_value[0], "gi");
            minor_target = small_value[1];
            minor_type = small_value[2];
            minor_reward = small_value[3];
            users[i]["keywords"][major_catagory_title][1][minor_title] = {}
            // find the total reward percentage 
            minor_final_reward = 0
            score = 0
            var finalfoundmatches = [...text.matchAll(minor_regex) ];
            if (null == finalfoundmatches){
                finalfoundmatches = []
            }
            switch (minor_type) {
                case 'UC': // num of occurances
                    score = finalfoundmatches.length
                    break;
                case 'UT': // quality of occurances
                    for (i in finalfoundmatches) {
                        //grab the number
                        num = finalfoundmatches[i][0].match(/[0-9]+/)
                        score += num
                    }
                default:
                    break;
            }
            users[i]["keywords"][major_catagory_title][1][minor_title]['matches'] = finalfoundmatches;
            if (score > minor_target){
                score = minor_target;
            }
            minor_final_reward = minor_reward * (score / minor_target);
            major_sumed_reward += minor_final_reward
            users[i]["keywords"][major_catagory_title][1][minor_title]['percentage'] = minor_final_reward
        }
        users[i]["keywords"][major_catagory_title][0] = major_sumed_reward * major_catagory_weight
        totalScore += users[i]["keywords"][major_catagory_title][0]
    }
    users[i]['totalScore'] = totalScore;
    console.log(users);
    // add user details to list
    $("#resume_details").append(`   
    <tr onclick="window.location.href = '`+link+`'">
        <td></td>
        <td>`+ users[i].id +`</td>
        <td>`+ users[i]['totalScore'] +`</td>
        <td>`+ users[i]['name'] +`</td></a>
    </tr>`)
}
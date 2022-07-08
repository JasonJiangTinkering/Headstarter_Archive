var els = document.getElementsByClassName("random_color");
for (var i = 0; i < els.length; i++) {
    let randomColor = Math.floor(Math.random()*16777215).toString(16);
    els.item(i).style.backgroundColor = "#" + randomColor;
}

function loadFile(filePath) {
    console.log(filePath);
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
      result = xmlhttp.responseText;
    }
    return result;
  }

function loadFile(url, callback) {
    PizZipUtils.getBinaryContent(url, callback);
}
// Parse Resumes and add them to the sortable list
console.log();
for (i in applications_set){
    // file = loadFile('/media/'+ applications_set[i])
    // content = file
    // console.log(file);

    loadFile(
        '/media/'+ applications_set[i],
        function (error, content) {
            if (error) {
                throw error;
            }
            var zip = new PizZip(content);
            var doc = new window.docxtemplater(zip);
            var text = doc.getFullText();
            console.log(text);
            alert("Text is " + text);
        }
    );

}
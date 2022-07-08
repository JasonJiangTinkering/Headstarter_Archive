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

// Parse Resumes and add them to the sortable list
for (i in applications_set){
    file = loadFile('/media/'+ applications_set[i])
    console.log(file);
    var zip = new JSZip(content);
    var doc=new Docxtemplater().loadZip(zip)
    var text= doc.getFullText();
    console.log(text);

}
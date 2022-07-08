var els = document.getElementsByClassName("random_color");
for (var i = 0; i < els.length; i++) {
    let randomColor = Math.floor(Math.random()*16777215).toString(16);
    els.item(i).style.backgroundColor = "#" + randomColor;
}
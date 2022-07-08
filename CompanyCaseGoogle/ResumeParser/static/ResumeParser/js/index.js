var toggle = false;
var mode_cover = document.querySelector("#cover");
function modeToggle(){
    toggle = !toggle;
    if (toggle){
        mode_cover.style.left = 0
    }else{
        mode_cover.style.left = '8rem'
    }
}

function go_to(id){
    console.log(submit_base);
    console.log(review_base);
    if (toggle){
        console.log("go to review");
        window.location.href = review_base + id;
    }else{
        console.log("go to submit");
        window.location.href = submit_base + id;
    }
}
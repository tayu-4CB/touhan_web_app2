console.log("holle1")
document.getElementById("user_panel").style.visibility = hidden;
function show_login_form(){
    let element = document.getElementById("user_panel");
    document.querySelector("#user_panel").classList.toggle("show");
    let status = element.style.visibility;
    if (status == "hidden"){
        element.style.visibility = "visible";
    }else{
        element.style.visibility = "hidden";
    }
}

function show_menu(){
    console.log("showmenue")
}
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


function tabSwitch(){

    let active_tab_element = document.getElementsByClassName('is_active');
    console.log(active_tab_element[0]);
    document.getElementsByClassName('is_active')[0].classList.remove("is_active");
    event.target.classList.add("is_active");
    console.log(event.target)

    document.getElementsByClassName("is_show")[0].classList.remove("is_show");
    const array_tabs = Array.prototype.slice.call(document.getElementsByClassName('tab'));
    const index = array_tabs.indexOf(event.target);
    document.getElementsByClassName("panel")[index].classList.add("is_show");

    console.log("holle");
}

function check_all(bool){
    let element = document.querySelectorAll(".is_show > div > label > .selecter");
    const num = element.length;
    //console.log(element);
    //console.log(num);
    for(i=0; i<num; i++){
        console.log(element[i].checked)
        element[i].checked = bool;
    }
}

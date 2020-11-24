function myFunction(){
    document.getElementById('myDropdown').classList.toggle('show');
}

function respDrop(){
    document.getElementById('respDropdown').classList.toggle('show');
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')){
        const dropdowns = document.getElementsByClassName('dropdown-content');
        for (let openDropdown of dropdowns){
            if (openDropdown.classList.contains('show')){
                openDropdown.classList.remove('show');
            }
        }
    }
}
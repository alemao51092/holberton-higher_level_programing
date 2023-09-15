const header = document.querySelector("header");
const divStyle = document.querySelector("div");

function changeColor() {
    header.style.color = "red";
}

divStyle.addEventListener("click", changeColor);
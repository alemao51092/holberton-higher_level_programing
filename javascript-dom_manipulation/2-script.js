const header = document.querySelector("header");
const divStyle = document.querySelector("div");

function changeColor() {
  header.classList.add("red");
}

divStyle.addEventListener("click", changeColor);
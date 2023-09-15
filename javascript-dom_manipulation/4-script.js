const addItem = document.getElementById("add_item");
const list = document.querySelector(".my_list");

function add_AnItem() {
  const tiny = document.createElement("li");
  tiny.textContent = "Item";
  list.appendChild(tiny);
}

addItem.addEventListener("click", add_AnItem);
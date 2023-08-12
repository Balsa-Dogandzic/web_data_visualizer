//Navigacija
let checkBox = document.getElementById("check");
let collapse = document.getElementById("collapse");

collapse.addEventListener("click", () => {
  checkBox.checked = false;
});

//Footer
document.getElementById("year").innerHTML = new Date().getFullYear();

//console.log("hello world");
//const btn_menu = document.getElementById("btn_menu");
const header_toggle = document.querySelector("#header_toggle");
const header = document.querySelector(".header");
const body = document.querySelector("body");
//const overlay = document.querySelector(".overlay");
const fadeElement = document.querySelectorAll(".has-fade");

header_toggle.addEventListener("click", function () {

  //console.log("clicked");

  if (header.classList.contains("open")) {
    header.classList.remove("open");
    body.classList.remove("noscroll");
    fadeElement.forEach(function (element) {
      element.classList.remove("fade-in");
      element.classList.add("fade-out");

    });

  } else {
    header.classList.add("open");
    body.classList.add("noscroll");
    fadeElement.forEach(function (element) {
      element.classList.add("fade-in");
      element.classList.remove("fade-out");
    });

  }
});
const menuButton = document.getElementById("mobile-menu-button");
const mobileMenue = document.getElementById("mobile-menu");
const html = document.getElementById("html");
const closeButton = document.getElementById("mobile-menu-close");
const header = document.getElementById("header");

menuButton.addEventListener("click", () => {
    
    scrollTo(0, 0);
  mobileMenue.classList.remove("hidden");
  header.classList.add('hidden')
  html.classList.add("overflow-y-hidden");
});

mobileMenue.addEventListener("click", () => {

  mobileMenue.classList.add("hidden");
  header.classList.remove('hidden')
  html.classList.remove("overflow-y-hidden");
});

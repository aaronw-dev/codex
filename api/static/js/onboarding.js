const pathCards = document.querySelectorAll(".path_card")

pathCards.forEach(element => {
    element.addEventListener("click", (e) => {
        localStorage.setItem("selected_lang", element.getAttribute("lang"))
        localStorage.setItem("setup", true)
        location.href = "/app";
    })
});
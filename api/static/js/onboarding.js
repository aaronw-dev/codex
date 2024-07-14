const pathCards = document.querySelectorAll(".path_card")

pathCards.forEach(element => {
    console.log(element)
    element.addEventListener("click", (e) => {
        //location.href = "./app.html";
        location.reload()
        localStorage.setItem("selected_lang", element.getAttribute("lang"))
    })
});
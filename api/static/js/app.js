if (localStorage.getItem("setup") == null) {
    location.href = "/onboarding"
}

fetch(`/courses/${localStorage.getItem("selected_lang")}/1`)
    .then(data => data.json())
    .then(json => console.log(json))
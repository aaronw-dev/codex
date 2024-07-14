if (localStorage.getItem("setup") == null) {
    location.href = "/onboarding"
}
const courseTitle = document.getElementById("course-title")
var courseInfo;
async function init() {
    await fetch(`/courses/${localStorage.getItem("selected_lang")}/1`)
        .then(data => data.json())
        .then(json => courseInfo = json)
    console.lot(courseInfo)
}
init()
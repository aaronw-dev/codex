if (localStorage.getItem("setup") == null) {
    location.href = "/onboarding"
}
function smoothScroll(element) {
    element.scrollIntoView({
        behavior: 'smooth'
    });
}
const courseTitle = document.getElementById("course-title")
const componentContainer = document.querySelector(".component-container")
var courseInfo;
var componentIndex = 0;
async function init() {
    await fetch(`/courses/${localStorage.getItem("selected_lang")}/1`)
        .then(data => data.json())
        .then(json => courseInfo = json)
    console.log(courseInfo)
    courseTitle.innerHTML = courseInfo.name
}
init()

const lessonPanel = document.getElementById("lesson")
async function openLesson() {
    document.getElementById("component-title").innerHTML = courseInfo.name
    await courseInfo.lessons.slice(0, -1).forEach(element => {
        const componentDiv = document.createElement('div');
        componentDiv.className = 'component';
        const contentDiv = document.createElement('div');
        contentDiv.className = 'component-content';

        const questionSpan = document.createElement('span');
        questionSpan.id = 'component-question';
        questionSpan.textContent = element.name;
        contentDiv.appendChild(questionSpan);

        const paragraphP = document.createElement('p');
        paragraphP.id = 'component-paragraph';
        paragraphP.textContent = element.content;
        contentDiv.appendChild(paragraphP);

        componentDiv.appendChild(contentDiv);

        const continueButton = document.createElement('button');
        continueButton.className = 'component_continue';
        continueButton.textContent = 'Continue';
        componentDiv.appendChild(continueButton);

        componentContainer.appendChild(componentDiv);
    });

    let index = 1;
    await componentContainer.children.childNodes.forEach(element => {
        element.querySelector(".component_continue").addEventListener("click", (e) => {
            smoothScroll(componentContainer.children[index])
        })
        index++;
    })
    lessonPanel.style.top = "0px"
    lessonPanel.style.zIndex = 100;
}
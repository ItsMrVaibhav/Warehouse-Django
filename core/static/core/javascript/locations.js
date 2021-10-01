function addLocation(element) {
    if (locationForm.classList.contains("hide")) {
        locationForm.classList.remove("hide")
        element.innerText = "Close";
        element.classList.remove("btn-success")
        element.classList.add("btn-danger")
    } else {
        locationForm.classList.add("hide")
        element.innerText = "Add Location";
        element.classList.add("btn-success")
        element.classList.remove("btn-danger")
    }
}

function locationsSearch(input) {
    locations.forEach(location => {
        let text = location.querySelector(".table-card-title").innerText.toLowerCase();
        location.querySelectorAll(".table-text").forEach(html => {
            text += " " + html.innerText.toLowerCase();
        });

        if (text.includes(input.value.toLowerCase())) {
            location.classList.remove("hide");
        } else {
            location.classList.add("hide");
        }
    });
}

const locations = [...document.querySelectorAll(".location")];
const locationForm = document.getElementById("locationForm");
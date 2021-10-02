function updateProductsList(element) {
    locationsProducts.forEach(select => {
        if (select.dataset.location === element.value) {
            select.disabled = false;
            select.closest(".form-group").classList.remove("hide");
        } else {
            select.disabled = true;
            select.closest(".form-group").classList.add("hide");
        }
    });
}

function addProductMovement(element) {
    if (productMovementForm.classList.contains("hide")) {
        productMovementForm.classList.remove("hide")
        element.innerText = "Close";
        element.classList.remove("btn-success")
        element.classList.add("btn-danger")
    } else {
        productMovementForm.classList.add("hide")
        element.innerText = "Add Location";
        element.classList.add("btn-success")
        element.classList.remove("btn-danger")
    }
}

function productMovementsSearch(input) {
    productMovements.forEach(pMovement => {
        let text = pMovement.querySelector("#productName").innerText.toLowerCase();
        pMovement.querySelectorAll(".table-text").forEach(html => {
            text += " " + html.innerText.toLowerCase();
        });
        console.log(text);

        if (text.includes(input.value.toLowerCase())) {
            pMovement.classList.remove("hide");
        } else {
            pMovement.classList.add("hide");
        }
    });
}

const productMovements = [...document.querySelectorAll(".product-movement")];
const locationsProducts = [...document.querySelectorAll(".locations-products")];
const productMovementForm = document.getElementById("productMovementForm");
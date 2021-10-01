function toggleTableDescription(element) {
    const description = element.closest(".table-card-content").querySelector(".table-card-description");
    const descriptionLine = element.closest(".table-card-content").querySelector(".table-card-description-line");
    
    if (description.classList.contains("hide")) {
        description.classList.remove("hide");
        descriptionLine.classList.remove("hide");
        element.innerText = "Hide Description";
    } else {
        description.classList.add("hide");
        descriptionLine.classList.add("hide");
        element.innerText = "Show Description";
    }
}

function addProduct(element) {
    if (productForm.classList.contains("hide")) {
        productForm.classList.remove("hide")
        element.innerText = "Close";
        element.classList.remove("btn-success")
        element.classList.add("btn-danger")
    } else {
        productForm.classList.add("hide")
        element.innerText = "Add Product";
        element.classList.add("btn-success")
        element.classList.remove("btn-danger")
    }
}

function productsSearch(input) {
    products.forEach(product => {
        const text = product.querySelector(".table-card-title").innerText.toLowerCase();
        
        if (text.includes(input.value.toLowerCase())) {
            product.classList.remove("hide");
        } else {
            product.classList.add("hide");
        }
    });
}

const products = [...document.querySelectorAll(".product")];
const productForm = document.getElementById("productForm");
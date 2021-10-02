function productsSearch(input) {
    locations.forEach(location => {
        let text = location.querySelector(".table-card-title").innerText;
        location.querySelectorAll(".table-text").forEach(html => {
            text += " " + html.innerText;
        });
        const products = location.querySelectorAll(".product-name");
        const quantities = location.querySelectorAll(".product-quantity");
        products.forEach(html => {
            text += " " + html.innerText;
        });
        quantities.forEach(html => {
            text += " " + html.innerText;
        });
        text = text.toLowerCase();

        if (text.includes(input.value.toLowerCase())) {
            location.classList.remove("hide");
        } else {
            location.classList.add("hide");
        }
    });
}

const locations = [...document.querySelectorAll(".location")];
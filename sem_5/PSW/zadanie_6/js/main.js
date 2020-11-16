// 7
function soldItem() {
    const btn = document.getElementById("button_buy");
    if (!btn) return;
    btn.addEventListener(
        "click",
        function () {
            const img = document.getElementById("prodimage");
            img.setAttribute("src", "images/sold.jpg");
            img.setAttribute("alt", "sold");
        },
        false
    );
}

// 5
function pinCode() {
    while (true) {
        const pin = parseInt(prompt("What is your PIN-code?"));
        if (pin === 123456) {
            return;
        }
        alert("Invalid PIN-code");
    }
}

// 4
function getRandomPrice() {
    return Math.floor(Math.random() * 10000) / 100;
}

// 3
function changePrice(e) {
    const p = parseFloat(prompt("Please provide a price"));
    if (p) {
        e.nextSibling.nextSibling.innerHTML = p;
    }
    alert(p ? "Price was changed!" : "Price wasnt changed!");
}

// 2
function addProducts() {
    const products = [
        {
            title: "Mi Band 5",
            image: "images/product1.jpg",
        },
        {
            title: "Huawei",
            image: "images/product4.jpg",
        },
        {
            title: "Coffee machine",
            image: "images/product2.jpg",
        },
        {
            title: "UltraComfort Sit",
            image: "images/product3.jpg",
        },
    ];

    const resentProducts = document.getElementById("resent-products");
    if (!resentProducts) {
        return;
    }

    for (const product of products) {
        const promo = Math.random() > 0.5;
        let color;

        switch (promo) {
            case !!0:
                color = "gray";
                break;
            case !!1:
                color = "red";
                break;
            default:
                color = "blue";
        }

        const prodNode = document.createElement("article");
        prodNode.classList.add("product");
        prodNode.innerHTML = `
		<a href="product.html">
			<img class="product__img" src="${product.image}" alt="${product.title}" />
		</a>
		<div>
			<a class="product__title" onclick="changePrice(this);" href="#">${
                product.title
            }</a>
			<h3 class="product__price" style="color: ${color}">${getRandomPrice()} ${
            color === "red" ? "(-10)" : ""
        } zł</h3>
		</div>`;
        resentProducts.appendChild(prodNode);
    }
}

function printLabels() {
    const labels = ["Technology", "Mobile", "IPhone 11"];
    const label = document.getElementById("label");

    if (!label) return;

    let lb = "";
    let i = 0;
    do {
        if (i !== 0) {
            lb += "/";
        }
        lb += `<span>${labels[i]}</span>`;
        i++;
    } while (i < labels.length);
    label.innerHTML = lb;
}



window.addEventListener(
    "load",
    function () {
        addProducts();
        soldItem();
        printLabels();
    },
    false
);

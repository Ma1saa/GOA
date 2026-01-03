const mainDiv = document.getElementById("main")

fetch('https://fakestoreapi.com/products')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        data.forEach(product => {
            mainDiv.innerHTML += `<div class="card">
            <h3>${product.title}</h3>
            <img src="${product.image}" alt="">
            <p>$${product.price}</p>
            <button> ADD TO CART </button>
            </div>`
        })
    })
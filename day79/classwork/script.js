const h1 = document.querySelector("h1")
const p = document.querySelector("p")
const img = document.querySelector("img")
const button = document.querySelector("button")

fetch("https://fakestoreapi.com/products")
    .then(resp => resp.json())
    .then(data => {
        console.log(data)
        h1.textContent = data[0].title
        p.textContent = data[0].description
        img.src = data[0].image
        button.textContent = data[0].price + " $"
    })
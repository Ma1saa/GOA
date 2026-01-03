const h1 = document.querySelector('h1')
const p = document.querySelector('p')
const img = document.querySelector('img')

fetch('https://fakestoreapi.com/products/1')
    .then(response => response.json())
    .then(data => {
        h1.innerText = data.title
        p.innerText = `$${data.price}`
        img.src = data.image
    })
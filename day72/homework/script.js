const btn1 = document.getElementById('btn1')
const p1 = document.getElementById('p1')
const div1 = document.getElementById('div1')
const h1 = document.getElementById('h1')
const p2 = document.getElementById('p2')
const btn2 = document.getElementById('btn2')
const img1 = document.getElementById('img1')
const p3 = document.getElementById('p3')
const p4 = document.createElement('p')
const pText = document.createTextNode('Hello World!')
const p5 = document.createElement('p5')
const p6 = document.createElement('p6')
const div2 = document.getElementById('div2')
const btn3 = document.getElementById('btn3')
const p7 = document.getElementById('p7')
const btn4 = document.getElementById('btn4')
const img2 = document.getElementById('img2')
p4.appendChild(pText)
let x = 0

btn1.addEventListener('click', () => {
    p1.textContent = 'button clicked!'
})

div1.addEventListener('pointerover', () => {
    div1.style.backgroundColor = 'red'
})
div1.addEventListener('pointerout', () => {
    div1.style.backgroundColor = ''
})

h1.addEventListener('click', () => {
    h1.style.fontSize = '300px'
})
h1.addEventListener('dblclick', () => {
    h1.style.fontSize = ''
})
h1.addEventListener('pointerover', () => {
    console.log('Mouse i here!')
})

btn2.addEventListener('click', () => {
    x++
    p2.textContent = x
})

img1.addEventListener('pointerover', () => {
    img1.style.scale = 1.5
})
img1.addEventListener('pointerout', () => {
    img1.style.scale = 1
})

p3.addEventListener('pointerover', () => {
    document.body.appendChild(p4)
})
p3.addEventListener('pointerout', () => {
    document.body.removeChild(p4)
})

document.body.addEventListener('pointerdown', event => {
    event.target.style.backgroundColor = 'black'
})
document.body.addEventListener('pointerup', event => {
    event.target.style.backgroundColor = ''
})

p5.addEventListener('click', () => {
    p6.style.display = 'block'
})

btn3.addEventListener('click', () => {
    const p7 = document.createElement('p')
    const pText = document.createTextNode('Hello World!')
    p7.appendChild(pText)
    div2.appendChild(p7)
})

function removeItem(btn) {
  btn.parentElement.remove();
}

p7.addEventListener('pointerover', () => {
    p7.style.display = 'none'
    const p8 = document.createElement('p')
    const pText = document.createTextNode('Hello World!')
    p8.appendChild(pText)
    document.body.appendChild(p8)
})

btn4.addEventListener('click', () => {
    img2.src = 'Untitled2.jpg'
})
btn4.addEventListener('dblclick', () => {
    img2.src = 'Untitled.jpg'
})
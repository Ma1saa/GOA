const btn1 = document.getElementById('btn1')
const p1 = document.getElementById('p1')
const div1 = document.getElementById('div1')
const h1 = document.getElementById('h1')
const p2 = document.getElementById('p2')
const btn2 = document.getElementById('btn2')
const img1 = document.getElementById('img1')
const btn3 = document.getElementById('btn3')
const itemList = document.getElementById('itemList')
const btn4 = document.getElementById('btn4')
const btn5 = document.getElementById('btn5')
const input1 = document.getElementById('input1')
const submit = document.getElementById('submit')
const div2 = document.getElementById('div2')
const btn6 = document.getElementById('btn6')
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
btn3.addEventListener('click', () => {
    const li = document.createElement('li')
    li.textContent = 'Item ' + x
    itemList.appendChild(li)
    x++
})
btn4.addEventListener('click', () => {
    itemList.removeChild(itemList.lastElementChild)
})
btn5.addEventListener('click', () => {
    const li = document.createElement('li')
    li.textContent = 'new element'
    itemList.replaceChild(li , itemList.lastElementChild)
})
submit.addEventListener('click', () => {
    const p = document.createElement('p')
    p.textContent = input1.value
    div2.appendChild(p)
    input1.value = ''
})
btn6.addEventListener('click', () => {
    div2.remove('p')
})

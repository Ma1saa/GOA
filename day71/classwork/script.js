function pAdder() {
    let div = document.getElementById('div')
    let p = document.createElement('p')
    let pText = document.createTextNode('hello')

    p.appendChild(pText)

    div.appendChild(p)
}

function replacer() {
    let btn = document.createElement('button')
    btn.textContent = 'click'

    document.getElementById('div1').replaceChild(btn, h1)
}

let btn2 = document.createElement("button")
let btn3 = document.createElement('button')
let btn4 = document.createElement('button')

btn2.textContent = 'click me4'
btn3.textContent = 'click me5'
btn4.textContent = 'click me6'

document.body.appendChild(btn2)
document.body.appendChild(btn3)
document.body.appendChild(btn4)

btn2.onclick = function (){
    console.log('clicked')
}
btn3.onmouseover = function (){
    console.log('hovered')
}
btn4.onmouseout = function (){
    console.log('mouse out')
}
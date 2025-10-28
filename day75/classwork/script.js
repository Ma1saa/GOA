const ol = document.getElementById('ol')
let soppingList = ['milk', 'bread', 'eggs', 'cheese']
names = ['mate', 'dito', 'alex', 'john']
const img1 = document.createElement('img')
const img2 = document.createElement('img')
const img3 = document.createElement('img')


imges = [img1, img2, img3]
imgesSrc = ['Untitled1.jpg', 'Untitled2.jpg', 'images.jpg']

for(let i = 0; i < imges.length; i++) {
    imges[i].src = imgesSrc[i]
}

for (let i = 0; i < names.length; i++) {
    console.log(names[i] + ' hello')
}

for(let i = 0; i < soppingList.length; i++) {
    let li = document.createElement('li')
    let text = document.createTextNode(soppingList[i])
    li.appendChild(text)
    ol.appendChild(li)
}


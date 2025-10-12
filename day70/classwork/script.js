function addP() {
    let p = document.createElement("p");
    let pText = document.createTextNode("hello");
    let div = document.getElementById("div");
    p.appendChild(pText);
    div.appendChild(p);
}

let h1 = document.createElement("h1");
let h1Text = document.createTextNode("hello");
h1.appendChild(h1Text);
h1.style.color = "red";
h1.style.fontSize = "20px";
h1.style.fontFamily = "Arial, Helvetica, sans-serif";
document.body.appendChild(h1);


let h2 = document.createElement("h2");
let h2Text = document.createTextNode("hello");
h2.appendChild(h2Text);
h2.style.color = "blue";
h2.style.fontSize = "20px";
h2.style.fontFamily = "Arial, Helvetica, sans-serif";
document.body.appendChild(h2);


function addImg() {
    let img = document.createElement("img");
    img.src = "Untitled.jpg";
    img.style.width = "200px";
    img.style.height = "200px";
    document.body.appendChild(img);
}
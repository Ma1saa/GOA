const p = document.createElement("p");
const text = document.createTextNode("This is added by JavaScript");
p.appendChild(text);
document.body.appendChild(p);

const h2 = document.createElement("h2");
h2.textContent = "Welcome!";
document.getElementById("myDiv").appendChild(h2);

const newDiv = document.createElement("div");
newDiv.style.backgroundColor = "blue";
newDiv.textContent = "This is a blue div";
document.body.appendChild(newDiv);

const button = document.createElement("button");
button.textContent = "Click Me";
document.getElementById("myDiv").appendChild(button);

const p1 = document.createElement("p");
const span = document.createElement("span");
span.textContent = "Important!";
span.style.color = "red";
p1.appendChild(span);
document.body.appendChild(p1);
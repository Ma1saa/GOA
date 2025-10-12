document.getElementById("addParaBtn").addEventListener("click", () => {
     const p = document.createElement("p")
     p.textContent = "New paragraph added."
     document.body.appendChild(p)
})

document.getElementById("removeParaBtn").addEventListener("click", () => {
    const paras = document.querySelectorAll("p")
    if (paras.length > 0) paras[paras.length - 1].remove()
})

const hoverDiv = document.getElementById("hoverDiv")
hoverDiv.addEventListener("mouseenter", () => hoverDiv.style.backgroundColor = "lightblue")

const hoverDiv2 = document.getElementById("hoverDiv2")
hoverDiv2.addEventListener("mouseleave", () => hoverDiv2.style.backgroundColor = "lightgray")

document.getElementById("textInput").addEventListener("input", e => console.log(e.target.value))

document.getElementById("myForm").addEventListener("submit", e => {
    e.preventDefault()
    alert(document.getElementById("formInput").value)
})

document.getElementById("replaceBtn").addEventListener("click", () => {
    const oldP = document.getElementById("replaceP")
    const newP = document.createElement("p")
    newP.textContent = "This is a new paragraph."
    oldP.replaceWith(newP)
})

document.getElementById("hideBtn").addEventListener("dblclick", e => e.target.style.display = "none")

const followDiv = document.getElementById("followDiv")
document.addEventListener("mousemove", e => {
    followDiv.style.left = e.pageX + "px"
    followDiv.style.top = e.pageY + "px"
})

const toggleBtn = document.getElementById("toggleImgBtn")
let img
toggleBtn.addEventListener("click", () => {
    if (!img) {
        img = document.createElement("img")
        img.src = "Untitled.jpg"
        document.body.appendChild(img)
    } else {
        img.remove()
        img = null
    }
})
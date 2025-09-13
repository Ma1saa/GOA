function color_changer(){
    document.getElementById("p").style.color = "red"
}

function even_odd() {
    let input = document.getElementById("input").value
    if (input % 2 === 0) {
        console.log("even")
    } else {
        console.log("odd")
    }
}

document.getElementById('p2').style.display = "none"

function text_changer() {
      document.getElementById("p1").style.display = "none"
      document.getElementById("p2").style.display = "block"
}

function admin_checker() {
    let input = document.getElementById("input1").value
    if (input === "admin") {
        document.body.style.background = "green"
    } else {
        document.body.style.background = "red"
    }
}

function prompt_alert() {
    let prompt1 = prompt("name:")
    alert("hello " + prompt1)
}

function prompt_age() {
    alert('welcome')
    let prompt2 = prompt("age:")
    console.log('your age is', prompt2)
}
const input = document.getElementById("input1")
const button = document.getElementById("btn1")
const messages = document.getElementById("message_area")

button.addEventListener("click", sendMessage)

function sendMessage() {
    if (!input.value.trim()) return

    addMessage(input.value, "user")
    input.value = ""

    setTimeout(() => {
        addMessage("hello how are you", "bot")
    }, 1000)
}

function addMessage(text, sender) {
    const p = document.createElement("p")
    p.textContent = text
    p.id = sender
    messages.appendChild(p)

    messages.scrollTop = messages.scrollHeight
}

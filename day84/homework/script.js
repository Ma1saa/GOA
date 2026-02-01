const input = document.getElementById("input1")
const button = document.getElementById("btn1")
const messages = document.getElementById("message_area")

button.addEventListener("click", sendMessage)
function sendMessage() {
    const userText = input.value.trim()
    if (!userText) return

    addMessage(userText, "user")
    input.value = ""

    // bot responds instantly
    const botReply = getBotResponse(userText)
    addMessage(botReply, "bot")
}

function addMessage(text, sender) {
    const p = document.createElement("p")
    p.textContent = text
    p.id = sender
    messages.appendChild(p)

    messages.scrollTop = messages.scrollHeight
}

function getBotResponse(message) {
    const msg = message.toLowerCase()

    if (msg.includes("hello") || msg.includes("hi")) {
        return "Hey How can I help you?"
    }

    if (msg.includes("how are you")) {
        return "I'm doing great Thanks for asking!"
    }

    if (msg.includes("name")) {
        return "I'm GMessage Bot"
    }

    if (msg.includes("bye")) {
        return "Goodbye Have a nice day!"
    }

    if (msg.includes("help")) {
        return "Sure! Tell me what you need help with"
    }

    // default response
    return "I don't understand that"
}

function revWords(word) {
    return word.split("").reverse().join("")
}

let fruits = [ "apple", "banana", "cherry"]
fruits.slice(0,2)

for(const fruit of fruits){
    console.log(fruit)
}

let text = "i love coding"

for(const word of text.split(" ")){
    console.log(word)
}

let numbers = [1,2,3,4,5]
console.log(numbers.reverse().join("-"))

let names = ["mate", "dito", "alex"]
console.log(names.slice(1).join(" "))
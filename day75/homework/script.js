let nums = [1,2,3,4,5,6,7,8,9,10]

function numss(){
    for(let i = 0; i < nums.length; i++) {
        console.log(nums[i])
    }
}

let names = ['mate', 'dito', 'alex', 'john']
for(let i = 0; i < names.length; i++) {
    console.log(`${names[i]}  ${i}`)
}

let num2 = [1,2,3,4,5,6,7,8,9,10]
for(let i = 0; i < num2.length; i++) {
    console.log(num2[i]*2)
}

let strNums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']

function listElementCounter(){
    let sumOfElements = ""
    for(let i = 0; i < strNums.length; i++) {
        sumOfElements++
    }
    console.log(sumOfElements)
}

nums3 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for(let i = 0; i < nums3.length; i++) {
    sum += nums3[i]
}
console.log(sum)
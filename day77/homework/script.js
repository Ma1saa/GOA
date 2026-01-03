let nums = [1,2,3,4,5,6,7,8,9,10]

let numm = nums.map((num, i) => i % 2 === 0 ? num+i : num-i)

console.log(numm)

let strns = ['mate', 'john', 'bob', 'jane']

let revStr = strns.map(str => {
    return str[strns.length - 1] + str.slice(1, -1) + str[0]
})

console.log(revStr)

console.log(strns.map(str => {
    return `${str}(${str.length})`
}))

let nums2 = [1,26,33,42,51,6,7,88,9,10]

let num = nums2.map(num => num > 10 ? Math.floor(num*num) : num)

console.log(num)

fullNames = ['Mate Maisuradze', 'John Jonishvili', 'Bob Bobadze', 'Jane Lobjanidze']

console.log(fullNames.map(fullName => `${fullName.split(' ')[0].toLowerCase()}.${fullName.split(' ')[1].toLowerCase()}@example.com`))


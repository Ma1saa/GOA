let nums = [1,2,3,4,5,6,7,8,9,10]
let strings = ['mate', 'john', 'bob', 'jane']

nums.map(num => {
    console.log(num*2)
})

strings.map(str => console.log(str.toUpperCase()))

strings.map(str => console.log(str[0]))

let squar_nums = nums.map(num => num*num)
console.log(squar_nums)

strings.map(str => console.log("hello mr. " + str))


let arr = [1, 2, 3, 4];
let newList = [];

arr.map(num => {
  const value = num + 5;
  console.log(value);
  newList.push(value);
});

console.log(newList);
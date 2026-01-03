let container = document.getElementById('user')


const user = {
    name: 'alex maisuradze',
    role: 'students',
    age: 15,
    isOnline: Math.random() > 0.5
}



let content = `
    <h3 id='nameHeading'>${user.name}</h3>
   <p>Role: ${user.role}</p>
   <p>Age: ${user.age}</p>

   <button onClick='alert("Viewing ${user.name}")'>View Profile</button>

   <div style="width: 100px; height: 100px" id="isOnline" ></div>
`


container.innerHTML = content


let isOnline1 = document.getElementById('isOnline')

if (user.isOnline) {
    isOnline1.style.background = 'green'
} else {
    isOnline1.style.background = 'red'
}
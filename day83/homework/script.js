function roverCommands(commands) {
     let x = 0, y = 0

     commands.split('-').map( char => {
         let command = char.slice(0, 2)
         let value = char.slice(2)

         if (command === 'UP') {
             y += value
         } else if (command === 'DO') {
             y -= value
         } else if (command === 'LE') {
             x -= value
         } else if (command === 'RI') {
             x += value
         } else {
             return 'Incorrect Input!'
         }

     })

     console.log(x, y)
 }

 roverCommands('UP5-DO4-RI9-LE1')
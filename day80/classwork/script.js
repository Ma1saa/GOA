let h1 = document.querySelector('h1')
let p = document.querySelector('p')
let img = document.querySelector('img')

let movie = 'shrek'
let apiKey = "38c8a267e25940bf35aa75921cdd6af2"

// https://image.tmdb.org/t/p/w400/

fetch(`https://api.themoviedb.org/3/search/movie?api_key=
${apiKey}&query=${encodeURIComponent(movie)}`)
    .then(resp => resp.json())
    .then(data => {
        console.log(data.results[0])
        
        h1.textContent = data.results[0].title
        p.textContent = data.results[0].release_date
        img.src =  `https://image.tmdb.org/t/p/w400/${data.results[0].poster_path}`
        
    })



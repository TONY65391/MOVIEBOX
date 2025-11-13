
const nav = document.querySelector('header nav');
const subMenu = document.querySelector('header .sub-menu');
nav.onclick = () => {
    nav.classList.toggle('open');
    subMenu.classList.toggle('open');
}


const container = document.querySelector('.container');
const API_KEY = '05d5c4c8e843e9277522fcbd6dbc07ea';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMG_PATH = 'https://image.tmdb.org/t/p/w500';

async function getMovies(){
    const response = await fetch(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=sandman`)
    const data = await response.json()
    console.log(data)
    return data.results
}
getMovies()
const API_KEY = `05d5c4c8e843e9277522fcbd6dbc07ea`;
const container = document.querySelector('.container');
const BASE_URL = 'https://api.themoviedb.org/3';
const IMG_PATH = 'https://image.tmdb.org/t/p/w500';


const nav = document.querySelector('header nav');
nav.onclick = () => {
    nav.classList.toggle('open');
}
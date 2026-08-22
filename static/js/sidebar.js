const grid = document.querySelector('.upbar_grid');
const upbar_co = document.querySelector('.upbar_con');
const sidebar = document.querySelector('.sidebar');
const upbar_profile_img  = document.querySelector('.upbar_icons .upbar_profile_img');
const profile_bar = document.querySelector('.profile_bar');
const notification = document.querySelector('.notification_con');
const upbar_notification = document.querySelector('.upbar_notification');
const container = document.querySelector('.container');
const moon = document.querySelector('.as-moon');
const moon_fill = document.querySelector('.as-moon-fill');
const body = document.body;
const currentTheme = localStorage.getItem('theme');




// Apply stored theme
if (currentTheme === 'dark') {
    body.classList.add('active'); // active = dark mode
    moon.classList.remove('active');
    moon_fill.classList.add('active');
  } else {
    body.classList.remove('active'); // light mode
    moon.classList.add('active');
    moon_fill.classList.remove('active');
  }
  

moon.addEventListener('click', function () {
    moon.classList.remove('active');
    moon_fill.classList.add('active')
    body.classList.add('active');
    localStorage.setItem('theme', 'dark');
})


moon_fill.addEventListener('click', function () {
    moon_fill.classList.remove('active');
    moon.classList.add('active')
    body.classList.remove('active');
    localStorage.setItem('theme', 'light');
})

        
upbar_notification.addEventListener('click', function() {
    notification.classList.toggle('active');
    profile_bar.classList.remove('active')
})


upbar_profile_img.addEventListener('click', function() {
    profile_bar.classList.toggle('active');
    console.log('clicked')
    notification.classList.remove('active')
})


grid.addEventListener('click', function() {
    sidebar.classList.toggle('active');
    upbar_co.classList.toggle('active')
    console.log('clicked')
})


container.addEventListener('click', function() {
    notification.classList.remove('active')
    profile_bar.classList.remove('active')
    sidebar.classList.remove('active')
})
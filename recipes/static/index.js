const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.menu');
const menuNav = document.querySelector('.menu-nav');
const menuItems = document.querySelectorAll('.menu-item');

let showMenu = false;

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu() {
  if (!showMenu) {
    menuBtn.classList.add('close');
    menu.classList.add('show');
    menuNav.classList.add('show');
    menuItems.forEach(item => item.classList.add('show'));

    showMenu = true;
  } else {
    menuBtn.classList.remove('close');
    menu.classList.remove('show');
    menuNav.classList.remove('show');
    menuItems.forEach(item => item.classList.remove('show'));

    showMenu = false;
  }
}
const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();

    const targetId = link.getAttribute('href');
    const target = document.querySelector(targetId);
    const offsetTop = target.offsetTop;

    window.scrollTo({
      top: offsetTop,
      behavior: 'smooth'
    });
  });
});

const search = document.querySelector('#search-input');
const recipeItem = document.querySelectorAll('.recipe-item');

searchInput.addEventListener('keyup', e => {
  const searchString = e.target.value.toLowerCase();

  recipeItems.forEach(item => {
    const itemTitle = item.querySelector('.recipe-title').textContent.toLowerCase();
    const itemIngredients = item.querySelector('.recipe-ingredients').textContent.toLowerCase();

    if (itemTitle.includes(searchString) || itemIngredients.includes(searchString)) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
});
const searchInput = document.querySelector('#search-input');
const recipeItems = document.querySelectorAll('.recipe-item');

searchInput.addEventListener('keyup', e => {
  const searchString = e.target.value.toLowerCase();

  recipeItems.forEach(item => {
    const itemTitle = item.querySelector('.recipe-title').textContent.toLowerCase();
    const itemIngredients = item.querySelector('.recipe-ingredients').textContent.toLowerCase();

    if (itemTitle.includes(searchString) || itemIngredients.includes(searchString)) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
});





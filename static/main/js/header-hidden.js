let header = document.getElementsByClassName('header')[0];
let scrollPosition = 0;

window.addEventListener('scroll', function () {
  let currentScroll = window.pageYOffset;

  if (currentScroll < scrollPosition && currentScroll >= 25) {
    // Прокрутка вверх на 15 пикселей или более - показать класс
    header.classList.remove('hide');
  } else if (currentScroll >= 100) {
    // Прокрутка вниз или неполная прокрутка вверх - скрыть класс
    header.classList.add('hide');
  }

  scrollPosition = currentScroll;
});

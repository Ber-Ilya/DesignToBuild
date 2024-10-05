function openBurger() {
    document.querySelector('.header').classList.toggle('__burger');
}

function openFormPopup() {
    const popup = document.querySelector('.popup');
    let element_fixed = document.querySelector('.element-fixed')
    popup.classList.toggle('__active');
    element_fixed.classList.toggle('__active');
  }




const filter = document.querySelector('.filter');
const filterConfig = document.querySelector('.filter_config');

filter.addEventListener('click', (e) => {
    if (e.target.tagName === 'BUTTON') {
        const platform = e.target.dataset.platform;
        if (platform === 'all') {
            filterConfig.classList.remove('__android', '__ios', '__desktop');
            Array.prototype.forEach.call(filter.children, (button) => {
                button.classList.remove('active');
            });
            e.target.classList.add('active');
        } else {
            filterConfig.classList.remove('__android', '__ios', '__desktop');
            filterConfig.classList.add(`__${platform}`);
            Array.prototype.forEach.call(filter.children, (button) => {
                button.classList.remove('active');
            });
            e.target.classList.add('active');
        }
    }
});



//Клик по странице
window.addEventListener('click', function(event){
    
    const counterWrapper = event.target.closest('.details-wrapper');
    // Проверка на нажатие по кнопке корзина
    if(event.target.hasAttribute('data-cart')){
        const card = event.target.closest('.card');
        const btn_hidden = counterWrapper.querySelector('[button__hidden]')
        const counter_open = counterWrapper.querySelector('[data-open-counter]')

        btn_hidden.style.display = "none"
        counter_open.style.display = "flex"

        const productInfo = {
            id: card.dataset.id,
            title: card.querySelector('.card__title').innerText,
            weight: card.querySelector('.card__weight').innerText,
            price: card.querySelector('.card__price--common').innerText,
            counter: card.querySelector('[data-counter]').innerText,
        }
    }
})
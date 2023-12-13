window.addEventListener('click', function(event){
    if (event.target.hasAttribute('data-cart')){
        const card = event.target.closest('.card');
        
        const productInfo = {
            id: card.dataset.id,
            imgSrc: card.querySelector('.product-img').getAttribute('src'),
            title: card.querySelector('.item-title').innerText,
            weight: card.querySelector('.price__weight').innerText,
            price: card.querySelector('.price__currency').innerText,
            counter: card.querySelector('[data-counter]').innerText,
        }
        console.log(productInfo)
    }
})
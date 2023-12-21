const cartWrapper = document.querySelector('.cart-wrapper');
window.addEventListener('click', function(event){
    if (event.target.hasAttribute('data-cart')){
        const card = event.target.closest('.card');
        
        const productInfo = {
            id: card.dataset.id,
            imgSrc: card.querySelector('.product-img').getAttribute('src'),
            title: card.querySelector('.card__title').innerText,
            weight: card.querySelector('.card__weight').innerText,
            price: card.querySelector('.card__price--common').innerText,
            new_price: card.querySelector('.card__price--common').innerText,
            counter: card.querySelector('[data-counter]').innerText,
        };
        console.log(productInfo)
        const cartItemHTML = `<div class="cart-item" data-id="${productInfo.id}">
				<div class="cart-item__top">
					<div class="cart-item__img">
						<img src="${productInfo.imgSrc}" alt="${productInfo.title}">
					</div>
					<div class="cart-item__desc">
						<div class="cart-item__title">${productInfo.title}</div>
										<!-- cart-item__details -->
						<div class="cart-item__details">

							<div class="items items--small counter-wrapper">
								<button class="items__control" data-action="minus">-</button>
						        <div class="items__current" data-counter>${productInfo.counter}</div>
						        <button class="items__control" data-action="plus">+</button>
							</div>

							<div class="price">
								<div class="price__currency">${productInfo.price} ₽</div>
							</div>

						</div>
										<!-- // cart-item__details -->

					</div>
				</div>
			</div>`;
    
        cartWrapper.insertAdjacentHTML('beforeend', cartItemHTML);
    }
    
})
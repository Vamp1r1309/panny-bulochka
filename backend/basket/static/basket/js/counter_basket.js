// Добавляем прослушку на всем окне
window.addEventListener('click', function (event) {

	let counter;
	// Находим обертку счетчика
	if (event.target.dataset.action === 'plus_cart' || event.target.dataset.action === 'minus_cart'){
		// Находим обертку счетчика
		// const btn_hidden = event.target.closest('.button')
		const counterWrapper = event.target.closest('.count__controls');
		// Находим div с числом счетчика
		counter = counterWrapper.querySelector('[data-counter-cart]');
		// // Проверяем является ли элемент кнопкой плюс
		if (event.target.dataset.action === 'plus_cart'){
			counter.innerText = ++counter.innerText;
		}

		// // Проверяем является ли элемент кнопкой минус
		if (event.target.dataset.action === 'minus_cart'){
			if (parseInt(counter.innerText) > 1) {
				counter.innerText = --counter.innerText;
			}
			
		}
	}
});

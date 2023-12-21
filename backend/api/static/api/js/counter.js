// Добавляем прослушку на всем окне
window.addEventListener('click', function (event) {

	let counter;
	// Находим обертку счетчика
	if (event.target.dataset.action === 'plus' || event.target.dataset.action === 'minus'){
		// Находим обертку счетчика
		// const btn_hidden = event.target.closest('.button')
		const counterWrapper = event.target.closest('.details-wrapper');
		// Находим div с числом счетчика
		counter = counterWrapper.querySelector('[data-counter]');
		// Проверяем является ли элемент кнопкой плюс
		if (event.target.dataset.action === 'plus'){
			counter.innerText = ++counter.innerText;
		}

		// Проверяем является ли элемент кнопкой минус
		if (event.target.dataset.action === 'minus'){
			if (parseInt(counter.innerText) > 1) {
				counter.innerText = --counter.innerText;
			}
			else{
				const btn_hidden = counterWrapper.querySelector('[button__hidden]')
				const counter_open = counterWrapper.querySelector('[data-open-counter]')
				btn_hidden.style.display = "block"
				counter_open.style.display = "none"
			}
		}
	}
});

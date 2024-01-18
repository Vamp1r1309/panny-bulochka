$(document).on('click', '#add-button', function(e){
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url: '{% url "basket:add_to_cart" %}',
		data: {
			product_id: $('#add-button').val(),
			product_quantity: $('#select').text(),
			csrfmiddlewaretoken: '{{ csrf_token }}',
			action: 'post'
		},
		success: function(response){
			document.getElementById('lbCartCount').textContent = response.qty
		},
		error: function(response){
			console.log(response);
		},
	})
})
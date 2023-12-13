window.addEventListener('click', function(event){
    if (event.target.hasAttribute('navbar'))
    {
        let clickMenu = event.target.closest('.scrollmenu')
        alert("Вы нажали на clickMenu")
    }
})
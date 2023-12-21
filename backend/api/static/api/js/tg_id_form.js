let tg = window.Telegram.WebApp;
window.addEventListener('click', function(event){
    if (event.target.closest('.id_telegram')){
        const id_telegram = event.target.closest('.id_telegram');
        id_telegram.value = tg.initData;
    }
})
"use strict"

const TELEGRAM_BOT_TOKEN = '';
const TELEGRAM_CHAT_ID = '';
const API = `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`;

async function SendOrderTelegram(event){
    event.preventDefault();
    const orderButton = document.querySelector("btn-cont button");
    console.log(orderButton);
}
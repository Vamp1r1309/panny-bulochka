from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from panny_bot.utils import StateForm
from panny_bot.config import db


async def get_form(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введи свое имя:")
    await state.set_state(StateForm.GET_NAME)
    await callback.answer()


async def get_form_year(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Рады познакомиться {message.text}!\nТеперь введи дату рождения\nПример: 22.02.2022")
    await state.set_state(StateForm.GET_YEAR)

async def get_form_phone(message: Message, state: FSMContext):
    await state.update_data(years=message.text)
    await message.answer("Номер телефона:")
    await state.set_state(StateForm.GET_PHONE)

async def end_form(message: Message, state:FSMContext):
    await state.update_data(phone=message.text)
    context_data = await state.get_data()
    name = context_data["name"]
    year = context_data['years']
    phone = context_data['phone']
    await db.add_users(chat_id=message.from_user.id, name=name, year=year, phone=phone)
    await message.answer(f"{name}!, мы рады познакомиться с тобой! Теперь ты будешь в числе самых первых получать все самые горячие акции, скидки и знакомится с нашими новинками. Также здесь ты можешь узнать информацию о нас, ознакомиться с меню и сделать заказ. ")


async def complite_cmd(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()


async def complite_error(callback: CallbackQuery,bot: Bot, state: FSMContext):
        await state.clear()


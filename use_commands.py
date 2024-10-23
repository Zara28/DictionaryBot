from aiogram import types, Bot, F
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import bot.__init__ as m
from db_scripts import getCategory, getAnswer, getQuestion


async def cmd_start(message: Message):
    await message.reply("Привет!\nЯ ваш бот помощник по самым популярным вопросам!")


async def cmd_help(message: Message):
    str = "Мои возможности:\r\n"
    str += ("Введи /категории и получи список доступных категорий вопросов, а дальше просто нажимай кнопки!\r\n"
            "Не нашел своего вопроса? Введи /задать вопрос и свой вопрос через пробел - тебе обязательно ответят!\r\n"
            "Хочешь предложить вопрос и ответ? Введи /предложить и вводи!")
    await message.reply(str)


async def cat(message: types.Message):
    cats = getCategory()
    builder = InlineKeyboardBuilder()
    buttons = []
    for data in cats:
        buttons.append([])
        buttons[-1].append(types.InlineKeyboardButton(
            text=str(data[1]),
            callback_data=f"questions | {data[0]}"))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        "Категории вопросов",
        reply_markup=keyboard
    )

@m.dp.callback_query()
async def callback(callback):
    if 'questions' in callback.data:
        await questions(callback, callback.data.split(' | ')[1])
    else:
        await answer(callback, callback.data.split(' | ')[1])

async def questions(callback, id):
    quest = getQuestion(id)
    builder = InlineKeyboardBuilder()
    buttons = []
    for data in quest:
        buttons.append([])
        buttons[-1].append(types.InlineKeyboardButton(
            text=str(data[1]),
            callback_data=f"answer | {data[0]}"))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer()
    await callback.message.answer(
        "Вопросы",
        reply_markup=keyboard
    )

async def answer(callback, id):
    ans = getAnswer(id)
    await callback.answer()
    await callback.message.answer(
        str(ans)
    )
from random import Random

import bot
from aiogram import types, Bot, F
# from docx import Document
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import bot.__init__ as m
from config import ADMIN
from db_scripts import getCategory, getAnswer, getQuestion, addAnswer


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
            callback_data=f"answer | {data[0]}"))
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
    quest = getQuestion(id, True)
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


async def quest(message: types.Message):
    await m.bot.send_message(chat_id=ADMIN, text=message.text + " от " + message.from_user.full_name)
    await message.answer("Ваш вопрос был отправлен администратору")


async def add(message: types.Message):
    rand = Random()
    t = message.text.replace("\r\n", ":").replace("/add", "").replace("\n", ":")
    text = t.split(":")
    quest = ""
    ans = ""
    cat = ""
    type = ""
    for i in text:
        if(i.lower() == "вопрос"):
            quest = text[text.index(i) + 1]
        if(i.lower() == "ответ"):
            ans = text[text.index(i) + 1]
            type = 2
        if(i.lower() == "категория"):
            cat = text[text.index(i) + 1]
    # if message.photo is not None or message.document is not None:
    #     document = Document(message.document)
    #     ans = f"{rand.random(100)}file.docx"
    #     document.save(ans)
    #     type = 3

    categories = getCategory()
    for i in categories:
        print(i[1])
        print(cat)
        if str(i[1]) == str(cat).replace(" ", ''):
            cat = i[0]
            break

    addAnswer(cat, type, quest, ans)

    await message.answer("Ваш вопрос отправлен на согласование")
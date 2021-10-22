from contextlib import AsyncExitStack
from loader import bot, dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, message
from aiogram.dispatcher.filters import Command
# from keyboards.default.default_keyboard import phone
from keyboards.inline.inline_keyboard import initial_choice, categories
from aiogram.dispatcher import FSMContext
from states.text_states import Journalist, Speaker
import re
from aiogram import types
import database
from config.config import admin_id

@dp.message_handler(Command("start"), state="*")
async def greeting(message: Message, state=FSMContext):
    """
    Initial greeting function that presents the user with two choices:
    are they a journalist, or are they a speaker.
    Args:
        message (Message): aiogram Message class.
        state ([type], optional): [description]. Defaults to FSMContext.
    """    
    await state.finish()
    await message.answer("Выберите вашу роль:", reply_markup=initial_choice)

@dp.callback_query_handler(text='speaker')
async def ask_speaker_questions(call: CallbackQuery):
    """[summary]

    Args:
        call (CallbackQuery): [description]
    """    
    await bot.answer_callback_query(callback_query_id=call.id)
    await call.message.edit_reply_markup(reply_markup=categories)
    await call.message.answer('Отлично! Введите, пожалуйста, ваше ФИО:')
    #await Speaker.name.set()

@dp.message_handler(state=Speaker.name)
async def ask_for_name(message: Message, state = FSMContext):
    """[summary]

    Args:
        message (Message): [description]
        state ([type], optional): [description]. Defaults to FSMContext.
    """
    answer = message.text    
    await state.update_data(name = answer)
    await message.answer('Введите номер телефона:')
    await Speaker.next()

@dp.message_handler(state=Speaker.phone)
async def ask_for_phone(message: Message, state = FSMContext):
    """[summary]

    Args:
        message (Message): [description]
        state ([type], optional): [description]. Defaults to FSMContext.
    """
    answer = message.text
    await state.update_data(phone = answer)
    await message.answer('Введите почту:')
    await Speaker.next()    

@dp.message_handler(state=Speaker.email)
async def ask_for_email(message: Message, state = FSMContext):
    """[summary]

    Args:
        message (Message): [description]
        state ([type], optional): [description]. Defaults to FSMContext.
    """

    user = types.User.get_current()
    chat_id = user.id

    email = message.text
    data = await state.get_data()
    full_name = data.get('name')
    phone = data.get('phone')

    database.add_user('speakers', chat_id, full_name, phone, email)

    await message.answer('Спасибо!')
    await state.finish()    

#--------------------------------------------------------------------------

@dp.callback_query_handler(text='journalist')
async def ask_speaker_questions(call: CallbackQuery):
    """[summary]

    Args:
        call (CallbackQuery): [description]
    """    
    await bot.answer_callback_query(callback_query_id=call.id)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Отлично! Введите, пожалуйста, ваше ФИО:')
    await Journalist.name.set()

@dp.message_handler(state=Journalist.name)
async def ask_for_name(message: Message, state = FSMContext):
    """[summary]

    Args:
        message (Message): [description]
        state ([type], optional): [description]. Defaults to FSMContext.
    """
    answer = message.text    
    await state.update_data(name = answer)
    await message.answer('Введите ваше издание:')
    await Journalist.next()

@dp.message_handler(state=Journalist.company)
async def ask_for_phone(message: Message, state = FSMContext):
    """[summary]

    Args:
        message (Message): [description]
        state ([type], optional): [description]. Defaults to FSMContext.
    """
    answer = message.text
    await state.update_data(phone = answer)
    await message.answer('Введите почту:')
    await Journalist.next()
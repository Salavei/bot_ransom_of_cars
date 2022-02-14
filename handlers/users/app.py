from main import *
from aiogram.dispatcher.filters.builtin import CommandStart
from filter.admin import IsAdmin
from keyboards.default.markup import *
from utils.func_async import *
from fsm.fsm import start_fsm


@dp.message_handler(commands=['admin'])
async def command_start(message: types.Message):
    if not await IsAdmin().check(message):
        if not db.why_get_admin(message.from_user.id):
            db.get_admin(message.from_user.id, True)
            await message.answer('⚠️ Вход в админ режим ⚠️', reply_markup=keyboard_admin)
        else:
            db.get_admin(message.from_user.id, False)
            await message.answer('❌ Выход из админ режима ❌', reply_markup=keyboard_all_users)
    else:
        db.get_admin(message.from_user.id, False)
        await message.answer('❌ Вы не админ, команда не будет работать ❌', reply_markup=keyboard_all_users)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_subscriber(message.from_user.id):
        if not db.check_confirm(message.from_user.id):
            await message.answer(f'Подтвердите согласие!!', reply_markup=await confirm_data_users(message.from_user.id))
    else:
        await message.answer(f'🔙🔙', reply_markup=keyboard_all_users)


async def error(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        "Оставить объявление": start_fsm,
        "Посмотреть объявления": view_all_add,
        "Мои объявления": view_my_add,

    }
    data_admin = {
        'Объявления для Верификации': admin_view_add,
    }
    await data.get(message.text, error)(message)
    await data_admin.get(message.text, error)(message)

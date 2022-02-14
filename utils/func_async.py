from handlers.users.app import *
from main import *
from aiogram import types
from keyboards.inline.inline_keyboards import *


async def view_all_add(message: types.Message):
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    brand_name = set(db.show_all_name_())
    dd = []
    for j in brand_name:
        dd.append(*j)
    for i in range(len(dd)):
        inline_btn = InlineKeyboardButton(f'{dd[i]}', callback_data=f'SEARCH_{dd[i]}')
        inline_kb_full.add(inline_btn)
    if db.show_all_add_():
        await message.reply(text='Объявления', reply_markup=inline_kb_full)
    else:
        await message.answer(text='Обьявления отсутствуют')


async def view_my_add(message: types.Message):
    data = {
        1: 'Остановить',
        0: 'Активировать',
    }
    if db.show_all_add_my(message.from_user.id):
        for un in db.show_all_add_my(message.from_user.id):
            id, brand, model_year, mileage, cost, number_phone, allow, _, _ = un
            await message.answer(
                text=f'Брэнд: {brand}\nМодель + год: {model_year}\nПробег: {mileage}\nЦена: {cost}'
                     f'\nНомер телефона: {number_phone}', reply_markup=await keyboards_ad_user(id, data[allow]))
    else:
        await message.answer(text='Обьявления отсутствуют')


async def admin_view_add(message: types.Message):
    if db.show_all_add_adm():
        for un in db.show_all_add_adm():
            id, brand, model_year, mileage, cost, number_phone, allow, allow_admin, _ = un
            await message.answer(
                text=f'Брэнд: {brand}\nМодель + год: {model_year}\nПробег: {mileage}\nЦена: {cost}'
                     f'\nНомер телефона: {number_phone}', reply_markup=await admin_keyboards_ad(id))
    else:
        await message.answer(text='Обьявления отсутствуют для админа!!')

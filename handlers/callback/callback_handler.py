from main import *
from aiogram import types
from keyboards.default.markup import keyboard_all_users


@dp.callback_query_handler(lambda call: 'SEARCH_' in call.data)
async def view_inline_block_car(call: types.CallbackQuery):
    for un in db.show_all_inline_(call.data.split('_')[-1]):
        _, brand, model_year, mileage, cost, number_phone, allow, _, _ = un
        await bot.send_message(call.from_user.id,
                               text=f'Брэнд: {brand}\nМодель + год: {model_year}\nПробег: {mileage}\nЦена: {cost}'
                                    f'\nНомер телефона: {number_phone}')


@dp.callback_query_handler(lambda call: 'OK_' in call.data)
async def accept_user(call: types.CallbackQuery):
    db.add_subscriber(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️", reply_markup=keyboard_all_users)


@dp.callback_query_handler(lambda call: 'stop_start_ad_' in call.data)
async def user_successful_stor_start(call: types.CallbackQuery):
    db.user_info_stor_start(call.data.split('_')[-1], allow=(not (db.how_status_ad(call.data.split('_')[-1]))))
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'admin_confirm_ad_' in call.data)
async def confirm_adm(call: types.CallbackQuery):
    db.adm_successful_confirmation(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'ad_admin_dell_' or 'dell_ad_in' in call.data)
async def dell_adm(call: types.CallbackQuery):
    db.adm_dell_ad(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️")

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *


class FSMcreate_ad(StatesGroup):
    brand = State()
    model_year = State()
    mileage = State()
    cost = State()
    number_phone = State()


async def start_fsm(message: types.Message):
    await FSMcreate_ad.brand.set()
    await message.answer('Напишите брен Вашей машины:')


@dp.message_handler(state=FSMcreate_ad.brand)
async def write_brand(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['brand'] = message.text
    await FSMcreate_ad.next()
    await message.answer('Введите модель + год:')


@dp.message_handler(state=FSMcreate_ad.model_year)
async def write_model_year(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_year'] = message.text
    await FSMcreate_ad.next()
    await message.answer('Введите пробег:')


@dp.message_handler(state=FSMcreate_ad.mileage)
async def write_mileage(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mileage'] = message.text
    await FSMcreate_ad.next()
    await message.answer('Введите цену:')


@dp.message_handler(state=FSMcreate_ad.cost)
async def write_mileage(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cost'] = message.text
    await FSMcreate_ad.next()
    await message.answer('Введите номер телефона:')


@dp.message_handler(state=FSMcreate_ad.number_phone)
async def write_mileage(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_phone'] = message.text
    db.add_my_ad_fsm(message.from_user.id, data['brand'], data['model_year'], data['mileage'], data['cost'],
                     data['number_phone'])
    await message.answer('Ваше объявление составлено!!')
    await state.finish()

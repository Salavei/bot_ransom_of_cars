from aiogram.types import KeyboardButton
from aiogram import types

# user_button
btn_leave_ad = KeyboardButton("Оставить объявление")
btn_view_ad = KeyboardButton("Посмотреть объявления")
btn_my_ad = KeyboardButton("Мои объявления")

# btn_back = KeyboardButton("🔙")

keyboard_all_users = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all_users.add(btn_leave_ad, btn_view_ad, btn_my_ad)

# admin button
admin_confirm = KeyboardButton('Объявления для Верификации')
keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.add(admin_confirm)

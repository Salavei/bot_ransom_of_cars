from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def confirm_data_users(tg_id) -> InlineKeyboardMarkup:
    """Одобрить обработку личных данных"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('✅ согласие на обработку личных данных', callback_data=f'OK_{tg_id}'),
            ]
        ]
    )
    return keyboard


async def keyboards_ad_user(id_an, allow) -> InlineKeyboardMarkup:
    """Остановка/Активация и Удаления объявлений для пользователя"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'stop_start_ad_{id_an}'),
                InlineKeyboardButton('❌ Удалить', callback_data=f'dell_ad_{id_an}'),
            ]
        ]
    )
    return keyboard


async def admin_keyboards_ad(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'admin_confirm_ad_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'ad_admin_dell_{id_an}'),
            ]
        ]
    )
    return keyboard


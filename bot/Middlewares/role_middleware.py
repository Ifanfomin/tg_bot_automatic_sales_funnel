from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from bot.config import config

class RoleMiddleware(BaseMiddleware):
    def __init__(self):
        super(RoleMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id

        # Проверка, является ли пользователь администратором
        if str(user_id) in config.ADMINS:
            data['role'] = 'admin'
        # Проверка, является ли пользователь ассистентом
        elif str(user_id) in config.ASSISTANTS:
            data['role'] = 'assistant'
        # Если пользователь не является ни администратором, ни ассистентом, он считается простым пользователем
        elif str(user_id) in config.SUPER_USERS:
            data['role'] = 'super_users'
        else:
            data['role'] = 'user'

# Пример использования в хендлерах
# async def admin_only_command(message: Message, role: str):
#     if role == 'admin':
#         await message.answer("Команда доступна только администраторам.")
#     else:
#         await message.answer("У вас нет доступа к этой команде.")
#
#
# async def assistant_or_admin_command(message: Message, role: str):
#     if role in ['admin', 'assistant']:
#         await message.answer("Команда доступна только администраторам и ассистентам.")
#     else:
#         await message.answer("У вас нет доступа к этой команде.")
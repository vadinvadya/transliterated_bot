import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

bot = Bot(token='7832827756:AAHlvomwWxVVu3vK83q1FFjXl_NOadjt8aU')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)



@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def proccess_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text.upper()
    translit_dict = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}
    transliterated_text = ''
    for i in text:
        if i in translit_dict:
            transliterated_text += translit_dict[i]
        else:
            transliterated_text += i
    text_title = transliterated_text.title()        
    # transliterated_text = translit(value=text, language_code='ru', reversed=True)
    logging.info(f'{user_name} {user_id} написал: {text}')
    await message.answer(text=text_title)

if __name__ == '__main__':
    dp.run_polling(bot)

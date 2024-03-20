import telebot
from telebot.types import Message
from keyboards import *
from telebot.types import ReplyKeyboardRemove
from config import *

bot = telebot.TeleBot(TOKEN)

STATE_NAME, STATE_PHONE, STATE_JOB, STATE_RESUME = range(4)

user_info = {}


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id,
                     f"Assalomualeykum,Abba marketing vakansiya botiman\nЗдравствуйте, я бот Abba marketing vacancy.")
    bot.send_message(chat_id, "Muloqot tilini tanlang:🇺🇿\nВыберите язык:🇷🇺", reply_markup=main_btn())


@bot.message_handler(func=lambda message: message.text == '🇺🇿 Uz | Ўз 🇺🇿')
def start(message):
    user_info[message.chat.id] = {}
    bot.send_message(message.chat.id, "Ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_name)


def save_name(message):
    user_id = message.chat.id
    user_info[user_id]["name"] = message.text
    bot.send_message(user_id, "Raqamingizni jo'nating")
    bot.register_next_step_handler(message, save_phone)


def save_phone(message):
    user_id = message.chat.id
    user_info[user_id]["phone"] = message.text
    bot.send_message(user_id, "Pastdagi yo'nalishlardan birini tanlang", reply_markup=job_selection_markup())
    bot.register_next_step_handler(message, save_job)


def save_job(message):
    user_id = message.chat.id
    user_info[user_id]["job"] = message.text
    bot.send_message(user_id, "Rezyumeyingizni jo'nating (PDF, JPEG, yoki PNG formatda):",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_resume)


def save_resume(message):
    user_id = message.chat.id
    if message.content_type == 'document':
        file_info = bot.get_file(message.document.file_id)
        file_extension = file_info.file_path.split('.')[-1].lower()
        if file_extension in ['pdf', 'jpeg', 'jpg', 'png']:
            file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
            user_info[user_id]["resume"] = file_url
            send_to_channel(user_id)
            return
    bot.send_message(user_id, "Noto'g'ri format. Iltimos PDF, JPEG, yoki PNG formatda jo'nating.")
    bot.register_next_step_handler(message, save_resume)


def send_to_channel(user_id):
    if user_id in user_info:
        info = user_info[user_id]
        if all(key in info for key in ["name", "phone", "job", "resume"]):
            text = f"Ism Familya: {info['name']}\nTelefon raqam: {info['phone']}\nJob: {info['job']}\nRezyume: {info['resume']}"
            bot.send_message(CHANNEL_ID, text)
            bot.send_message(user_id, "Raxmat! Ma'lumotlaringiz yetkazildi! Tez orada aloqaga chiqamiz")
            return
    bot.send_message(user_id, "Hamma ma'lumotlarni yozing!")

@bot.message_handler(func=lambda message: message.text == '🇷🇺 Ru | Ру 🇷🇺')
def start(message):
    user_info[message.chat.id] = {}
    bot.send_message(message.chat.id, "Введите ваше имя", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_name1)


def save_name1(message):
    user_id = message.chat.id
    user_info[user_id]["name"] = message.text
    bot.send_message(user_id, "Пожалуйста, введите ваш номер телефона:")
    bot.register_next_step_handler(message, save_phone1)


def save_phone1(message):
    user_id = message.chat.id
    user_info[user_id]["phone"] = message.text
    bot.send_message(user_id, "Пожалуйста, выберите работу из списка ниже:", reply_markup=job_selection_markup())
    bot.register_next_step_handler(message, save_job1)


def save_job1(message):
    user_id = message.chat.id
    user_info[user_id]["job"] = message.text
    bot.send_message(user_id, "Пожалуйста, загрузите ваше резюме (PDF, JPEG, yoki PNG):",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_resume1)


def save_resume1(message):
    user_id = message.chat.id
    if message.content_type == 'document':
        file_info = bot.get_file(message.document.file_id)
        file_extension = file_info.file_path.split('.')[-1].lower()
        if file_extension in ['pdf', 'jpeg', 'jpg', 'png']:
            file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
            user_info[user_id]["resume"] = file_url
            send_to_channel1(user_id)
            return
    bot.send_message(user_id, "Неверный формат файла. Пожалуйста, загрузите резюме в формате PDF, JPEG или PNG")
    bot.register_next_step_handler(message, save_resume1)


def send_to_channel1(user_id):
    if user_id in user_info:
        info = user_info[user_id]
        if all(key in info for key in ["name", "phone", "job", "resume"]):
            text = f"Ism Familyasi: {info['name']}\nTelefon raqam: {info['phone']}\nYo'nalish: {info['job']}\nRezyume: {info['resume']}"
            bot.send_message(CHANNEL_ID, text)
            bot.send_message(user_id, "Ваша информация отправлена в канал.")
            return
    bot.send_message(user_id, "Вы не предоставили полную информацию.")



bot.polling()

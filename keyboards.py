from telebot.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove


def main_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🇺🇿 Uz | Ўз 🇺🇿"), KeyboardButton("🇷🇺 Ru | Ру 🇷🇺"))

    return markup


def job_selection_markup():
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(KeyboardButton("SMM"), KeyboardButton("Branding"), KeyboardButton("Dasturchilik"),
           KeyboardButton("Boshqa Soha"))

    return markup

def job_selection_markup1():
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(KeyboardButton("СММ"), KeyboardButton("Брендинг"), KeyboardButton("Программирование"),
           KeyboardButton("Другое направление"))

    return markup

def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Raqam jo'natish",request_contact=True))

    return markup





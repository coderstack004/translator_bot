import telebot
from googletrans import Translator

translator = Translator()

bot = telebot.TeleBot('5107814255:AAGVACw5mWp2Nkf_qBAKaBTwvZtunHKWkMQ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom. Tarjimon botiga xush kelibsiz. Bu botda siz ['Uzbek'-'Rus'-'English'] tillarda gaplarni tarjima qilishingiz mumkin.\n\n")

@bot.message_handler(content_types=['text'])
def send_text(message):
    uz = translator.translate(message.text, dest='uz')
    ru = translator.translate(message.text, dest='ru')
    en = translator.translate(message.text, dest='en')
    
    bot.send_message(message.chat.id, f"*O'zbekcha:* {uz.text}", parse_mode='Markdown')
    bot.send_message(message.chat.id, f"*Русский:* {ru.text}", parse_mode='Markdown')
    bot.send_message(message.chat.id, f"*English:* {en.text}", parse_mode='Markdown')
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
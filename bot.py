import telebot
from config import currency, TOKEN, commands
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=[commands['start']])
def send_welcome(message):
    text = "Чтобы узнать стоимость конвертации валюты введите \n<имя валюты> " \
           "<в какую валюту перевести> <количество переводимой валюты>" \
           "\nУвидеть список всех доступных валют: /values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=[commands['help']])
def send_welcome(message):
    text = "Список доступных команд можно посмотреть в меню." \
           "\nДля конвертации введите <валюту которую хотите перевести> <в какую валюту перевести> " \
           "<количество валюты>." \
           "\nНапример 'евро доллар 15'"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=[commands['values']])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for value in currency.keys():
        text = "\n" .join((text, value, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        for command in commands:
            if value[0][0] == "/" and value != '/' + command[0]:
                raise APIException("Указана неверная команда")

        if len(value) != 3:
            raise APIException("Передано неверное количество параметров.")

        quote, base, amount = value
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}.")
    else:
        text = f"Цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

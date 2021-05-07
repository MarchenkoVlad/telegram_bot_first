import telebot
import config
import parse
import json

bot = telebot.TeleBot(config.token)

def get_news():
    data = parse.parse()
    title_news = [i['title'] for i in data]
    return title_news

@bot.message_handler(commands=['start'])
def send_news(message):
    title_news = get_news()
    print(title_news)
    title_news = [f'{i+1}. {j} \n' for i, j in enumerate(title_news)]
    bot.reply_to(message, ''.join(title_news))


if __name__ =='__main__':
    bot.infinity_polling()
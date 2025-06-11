import telebot
import requests
import random, os
import time 
bot = telebot.TeleBot("")
img=os.listdir("./photo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Я Эко бот вот моя команда /sorter")



@bot.message_handler(commands=['sorter'])
def sort(message):
    bot.reply_to(message,"Привет я бот который помогает изучить распределение мусора")
    time.sleep(5)
    bot.reply_to(message,"1. Пластик Что сюда относится: \n Бутылки от воды, напитков, молока (с маркировкой PET, PE-HD, PP) \n Упаковка от продуктов (контейнеры, пакеты, плёнка) \n"
                 "Как подготовить: \n Снимите крышки (их можно сдать отдельно, если они металлические). \n Ополосните от остатков пищи. \n Сплющите бутылки и упаковку, чтобы занимали меньше места. \n Что нельзя: \n Грязную упаковку с остатками еды Игрушки, трубы, CD-диски (это не перерабатываемый пластик)")
    with open("./photo/plastik.jpg","rb") as f:
                bot.send_photo(message.chat.id, f)
    time.sleep(20)
    bot.reply_to(message,"2. Бумага и картон Что сюда относится: \n Газеты, журналы, офисная бумага \n Коробки от товаров, упаковочный картон \n Бумажные пакеты, книги (без обложек) \n "
                 "Как подготовить:\n Удалите скотч, скрепки, плёнку.\n Расправьте коробки, чтобы экономить место. \n Жирную или мокрую бумагу выбрасывайте в общий мусор \n Что нельзя: \n Чеки, ламинированную бумагу, салфетки, обои")
    with open("./photo/paper.webp","rb") as f:
                bot.send_photo(message.chat.id, f)
    time.sleep(20)
    bot.reply_to(message,"3. Стекло \n Что сюда относится: \n Бутылки от напитков, банки от консервов \n Стеклянная тара от косметики (без дозаторов) \n "
                "Как подготовить: \n Промойте от остатков содержимого. \n Снимите крышки (металлические можно сдать в металл). \n Не разбивайте стекло – это опасно для работников сортировки. \n Что нельзя: \n Лампочки \n Зеркала \n Хрусталь \n Керамику")
    with open("./photo/steklo.webp","rb") as f:
                bot.send_photo(message.chat.id, f)
    time.sleep(20)
    bot.reply_to(message,"4. Металл \n Что сюда относится: \n Алюминиевые и жестяные банки \n Крышки от банок и бутылок \n Фольга (если чистая) \n Как подготовить: \n Промойте банки от остатков пищи. \n По возможности сплющите. \n Что нельзя: \n Батарейки \n Баллончики из-под аэрозолей")
    with open("./photo/metal.png","rb") as f:
                bot.send_photo(message.chat.id, f)





@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()




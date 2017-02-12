# -*- coding:utf-8 -*-
import telebot
import time
import threading
import sigaebot_private as bot_private

thread_active = False



def remove_none(text):
    if text is None:
        return ""
    else:
        return text


bot = telebot.TeleBot(bot_private.id['botid'])


@bot.message_handler(commands=['pink'])
def check_activate(message):
    bot.reply_to(message, "bot activation is stable ㄴ")

def tr():
    global thread_active
    thread_active = True
    time.sleep(30)
    thread_active = False



@bot.message_handler(func=lambda alwaysTrue: True)
def alwaysTure(message):
    try:
        print(message, end='\n\n')
        for key1, value1 in bot_private.callHuman.items():
            for key0, value0 in bot_private.id.items():
                if key1 in message.text:
                    if value1 == key0:
                        bot.send_message(str(value0),key1 + "님 {}가 너 불러 \n 메세지 내용 : {}".format(
                            str(message.from_user.first_name) + remove_none(message.from_user.last_name), message.text))
                        print("call")
        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value())
                return
            if "ㅋㅋㅋㅋㅋㅋㅋㅋ" in message.text:
                if not thread_active:
                    t = threading.Thread(target=tr)
                    bot.send_message(message.chat.id, 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                    t.start()

    except Exception as e:
        print(e)


bot.polling()
import telepot
token = '1317215167:AAFkZ1MrMLG8OAM_pMFiUdK14hNApi7a8W8'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You great '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)

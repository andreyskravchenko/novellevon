from telegram import Bot

class Actor:

    def __init__(self, token):

        self.interface = Bot(token=token)

    def say_hello (self, chat_id):
        me = self.interface.get_me()
        self.interface.sendMessage(chat_id=chat_id, text='Hello, I am' + me.first_name)



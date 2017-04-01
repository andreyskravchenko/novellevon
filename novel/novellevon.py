from telegram.ext import Updater, CommandHandler
from telegram import Bot, ReplyKeyboardMarkup

class Novellevon:

    token = "341359640:AAEKpn84nmSqs9fDY05IrJwwMvJNZz__8eo"

    def __init__(self):
        self.updater = Updater(self.token)
        dispatcher = self.updater.dispatcher

        # Create commands actions
        startHndlr = CommandHandler('start', self.start)
        pauseHndlr = CommandHandler('pause', self.pause)
        restartHndlr = CommandHandler('restart', self.restart)
        continueHndlr = CommandHandler('continue', self.renew)
        dispatcher.add_handler(startHndlr)
        dispatcher.add_handler(pauseHndlr)
        dispatcher.add_handler(restartHndlr)
        dispatcher.add_handler(continueHndlr)

    def start(self, bot, update):
        chatId = update.message.chat_id
        keyboardButtons = [['/pause']]
        keyboardMarkup = ReplyKeyboardMarkup(keyboardButtons)
        bot.sendMessage(chat_id=chatId,
                        text="has started",
                        reply_markup=keyboardMarkup)
        
    def pause(self, bot, update):
        chatId = update.message.chat_id
        keyboardButtons = [['/continue'], ['/restart']]
        keyboardMarkup = ReplyKeyboardMarkup(keyboardButtons)
        bot.sendMessage(chat_id=chatId,
                        text="has paused",
                        reply_markup=keyboardMarkup)
        
    def restart(self, bot, update):
        chatId = update.message.chat_id
        keyboardButtons = [['/pause']]
        keyboardMarkup = ReplyKeyboardMarkup(keyboardButtons)
        bot.sendMessage(chat_id=chatId,
                        text="has restarted",
                        reply_markup=keyboardMarkup)
        
    def renew(self, bot, update):
        chatId = update.message.chat_id
        keyboardButtons = [['/pause']]
        keyboardMarkup = ReplyKeyboardMarkup(keyboardButtons)
        bot.sendMessage(chat_id=chatId,
                        text="has continued",
                        reply_markup=keyboardMarkup)

    def listen(self):
        self.updater.start_polling()

    def about_myself(self):
        print(self.api.getMe())
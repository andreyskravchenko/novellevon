from telegram import Bot

class Novellevon:

    token = "341359640:AAEKpn84nmSqs9fDY05IrJwwMvJNZz__8eo"

    def __init__(self):
        self.api = Bot(self.token)

    def listen(self):
        updates = self.api.getUpdates()

        for update in updates:
            print update.message.text

    def about_myself(self):
        print(self.api.getMe())
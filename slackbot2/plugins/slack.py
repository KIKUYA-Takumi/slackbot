# -*- coding: utf-8 -*-
from slackbot.bot import listen_to


class Reply:
    def __init__(self):
        self.counter = 0

    def increase(self):
        self.counter += 1
        return self.counter


r = Reply()


@listen_to('(.*)')
def refrection(message, something):
    message.reply('まじで？')

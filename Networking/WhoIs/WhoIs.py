__author__ = 'angelo'
from SocketRequester import SocketRequester
from ConsoleDisplayer import ConsoleDisplayer

class WhoIs:

    def __init__(self, url, requester = SocketRequester(), displayer = ConsoleDisplayer()):
        self.url = url
        self.requester = requester
        self.displayer = displayer


    def go(self):
        result = self.requester.doWhoIs(self.url)
        if result:
            self.displayer.display(result)
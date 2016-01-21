import threading
import os
import logging

class InterfacesManager:
    interface = []
    def __init__(self):
        logging.debug("Starting InterfaceManager...")

    def mainLoop(self):
        for item in self.interface:
            logging.debug("Starting " + item.getInterfaceName())
            item.loop()

    def startInterface(self):
        threading.Thread(target=self.mainLoop).start()

import threading
from libs import NakLogger
from libs import ConfigManager

class InterfacesManager:
    interface = []
    def __init__(self):
        NakLogger.debug("Loading InterfaceManager...")
        for item in ConfigManager.getConfig("INTERFACE","names").split(','):
            NakLogger.debug("Loading " + item + " Interface")
        NakLogger.debug("Loading InterfaceManager End.")

    def mainLoop(self):
        for item in self.interface:
            NakLogger.debug("Starting " + item.getInterfaceName())
            item.loop()

    def startInterface(self):
        threading.Thread(target=self.mainLoop).start()

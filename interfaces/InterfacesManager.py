import threading
from libs import NakLogger
from libs import ConfigManager

class InterfacesManager:
    interfaces = []
    def __init__(self):
        NakLogger.debug("Loading InterfaceManager...")
        interfaceClassName = ""
        for item in ConfigManager.getConfig("INTERFACE","names").split(','):
            NakLogger.debug("Loading " + item + " Interface")
            interfaceClassModule = "interfaces." + item.capitalize() + "Interface"
            interfaceClassName = item.capitalize() + "Interface"
            mod = __import__(interfaceClassModule)
            submod = getattr(mod, interfaceClassName)
            klass = getattr(submod, interfaceClassName)
            self.interfaces.append(klass())
        NakLogger.debug("Loading InterfaceManager End.")

    def mainLoop(self):
        for item in self.interfaces:
            NakLogger.debug("Starting " + item.getInterfaceName())
            item.loop()

    def startInterface(self):
        threading.Thread(target=self.mainLoop).start()

import os
import logging
import libs

from libs import ConfigManager
from libs import NakLogger
from interfaces.InterfacesManager import InterfacesManager

#logger = NakLogger()
#config = ConfigManager()

class App:
    """ Entry point of the Application """
    def __init__(self):
        NakLogger.debug('Starting MARVIN...')
        ConfigManager.loadConf()
        self.loadInterfaces()

    def loadInterfaces(self):
        self.interfaceManager = InterfacesManager()
        self.interfaceManager.startInterface();

    def startEngine(self):
        NakLogger.debug("...")

# START POINT
'''
Logic :
Start App => LoadConf => StartInterfaces => Wait-Threaded-Loop
If message into loop => Thread Start Engine => Parser => Knifer => Meaner => Answer => end turn => Wait-Threaded-Loop
If message console "stop-marvin-0" => Write Cached Database => Shutdown App
'''
app = App();

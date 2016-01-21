import os
import logging
import libs

from libs import ConfigManager,NakLogger
from interfaces.InterfacesManager import InterfacesManager

class App:

    def __init__(self):
        NakLogger.consoleDebugActive(True)
        NakLogger.debug('Starting MARVIN...')
        ConfigManager.loadConf()
        self.loadInterfaces()

    def loadInterfaces(self):
        self.interfaceManager = InterfacesManager()
        self.interfaceManager.startInterface();

# START POINT
'''
Logic :
Start App => LoadConf => StartInterfaces => Wait-Threaded-Loop
If message into loop => Thread Start Engine => Parser => Knifer => Meaner => Answer => end turn => Wait-Threaded-Loop
If message console "stop-marvin-0" => Write Cached Database => Shutdown App
'''
app = App();

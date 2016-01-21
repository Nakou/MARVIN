import os
import logging

from libs.ConfigManager import ConfigManager
from interfaces.InterfacesManager import InterfacesManager

class App:
    """ Entry point of the Application """
    def __init__(self):
        logging.basicConfig(filename='logInfo.log', level=logging.DEBUG)
        logging.debug("Starting MARVIN...")
        self.config = ConfigManager()
        #self.config.setApp(self)
        self.config.loadConf()
        self.loadInterfaces()

    def loadInterfaces(self):
        self.interfaceManager = InterfacesManager()
        self.interfaceManager.startInterface();

    def startEngine(self):
        logging.debug("...")
        #STILL NOTHING

# START POINT
App();

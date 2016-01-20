import os
from libs.ConfigManager import ConfigManager
class App:
    """ Entry point of the Application """
    def __init__(self):
        self.config = ConfigManager()
        #self.config.setApp(self)
        self.config.loadConf()

# START POINT
App();

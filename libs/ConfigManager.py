import os
import logging
class ConfigManager:
    configparser = __import__('configparser')
    confDir = "etc/"
    mainConfFileName = "ai.conf.ini"

    def __init__(self):
        self.config = self.configparser.ConfigParser()

    def loadConf(self):
        if (os.path.isfile(self.confDir + self.mainConfFileName) == False):
            #GenerateDefaultConf
            logging.warning("No confFile, generating default conf...")
            self.executeDefaultConfiguration()
        logging.debug("Loading...")

    def setApp(self,app):
        self.app = app

    def executeDefaultConfiguration(self):
        logging.debug("Creating default configuration...")
        self.config['DEFAULT']['test'] = "test"
        with open(self.confDir+self.mainConfFileName, 'w') as configfile:
            self.config.write(configfile)

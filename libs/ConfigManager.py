import os
class ConfigManager:
    configparser = __import__('configparser')
    confDir = "etc/"
    mainConfFileName = "ai.conf.ini"

    def __init__(self):
        self.config = self.configparser.ConfigParser()

    def loadConf(self):
        if (os.path.isfile(self.confDir + self.mainConfFileName) == False):
            #GenerateDefaultConf
            self.executeDefaultConfiguration()
        print("Loading...")

    def setApp(self,app):
        self.app = app

    def executeDefaultConfiguration(self):
        print("Creating default configuration...")
        self.config['DEFAULT']['test'] = "test"
        with open(self.confDir+self.mainConfFileName, 'w') as configfile:
            self.config.write(configfile)

import os
from libs import NakLogger

configparser = __import__('configparser')
confDir = "etc/"
mainConfFileName = "generalconf.ini"
config = configparser.ConfigParser()

def loadConf():
    if (os.path.isfile(confDir + mainConfFileName) == False):
        #GenerateDefaultConf
        NakLogger.warn("No confFile, generating default conf...")
        executeDefaultConfiguration()
    NakLogger.debug("Loading...")

def getConfig(category,key):
    config.read(confDir + mainConfFileName)
    return config[category][key]

def executeDefaultConfiguration():
    NakLogger.debug("Creating default configuration...")

    config['MARVIN'] = {}
    config['MARVIN']['name'] = "Marvin"
    #---------------- INTERFACES -----------------
    config['INTERFACE'] = {}
    config['INTERFACE']['names'] = 'console,slack'
    config['INTERFACE']['currentName'] = 'marvin,marvin'
    #---------------- ENGINE -----------------
    config['ENGINE'] = {}
    config['ENGINE']['type'] = 'default'
    config['ENGINE']['name'] = 'default'
    #------------ DATABASE ACCESS ------------
    config['DAO'] = {}
    config['DAO']['type'] = 'default'
    # Standard access info non needed but for another engine in sql-like database
    config['DAO']['address'] = '127.0.0.1'
    config['DAO']['port'] = '0'
    config['DAO']['database'] = 'none'
    config['DAO']['login'] = 'none'
    config['DAO']['password'] = 'none'

    with open(confDir+mainConfFileName, 'w') as configfile:
        config.write(configfile)

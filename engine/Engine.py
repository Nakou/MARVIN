from libs import NakLogger
from libs import ConfigManager
from engine import Parser

class Engine:
    def __init__(self,entryInterface):
        self.entryInterface = entryInterface

    def start(self,message):
        NakLogger.debug("Engine here, message from " + self.entryInterface.getInterfaceName() + " - \"" + message + "\" received!")
        wordList = Parser.parser(message)
        #Knifer
        #Meaner
        #AnswerMaker
        answer = "Ok"
        self.entryInterface.outCom(answer)

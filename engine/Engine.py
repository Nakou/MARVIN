from libs import NakLogger
from libs import ConfigManager

class Engine:
    def __init__(self,entryInterface):
        self.entryInterface = entryInterface

    def start(self,message):
        NakLogger.debug("Engine here, message from " + self.entryInterface.getInterfaceName() + " - \"" + message + "\" received!")
        #Parser
        #Knifer
        #Meaner
        #AnswerMaker
        answer = "Ok"
        self.entryInterface.outCom(answer)

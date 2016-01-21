from interfaces.AbstractInterface import AbstractInterface
from interfaces.User import User

class ConsoleInterface(AbstractInterface):

    def __init__(self):
        self.user = User("Console")

    def loop(self):
        inputContent = "VOID"
        while (inputContent != "stop"):
            inputContent = input("MARVIN>")
            if (inputContent != "stop" and inputContent != "" and not(inputContent.isspace())):
                self.inCom(inputContent)
                print("endEngine")
        print("endLoop")
        print("Shutting Down : console Interface.")

    def getInterfaceName(self):
        return "CONSOLE"

    def outCom(self, message):
        print(message)

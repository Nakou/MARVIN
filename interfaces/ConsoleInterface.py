from interfaces.AbstractInterface import AbstractInterface

class ConsoleInterface(AbstractInterface):

    def loop(self):
        inputContent = "VOID"
        while (inputContent != "stop"):
            inputContent = input("MARVIN>")
            self.inCom(inputContent)

        print("Stopped...")

    def getInterfaceName(self):
        return "CONSOLE"

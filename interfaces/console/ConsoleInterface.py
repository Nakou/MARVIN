class ConsoleInterface(AbstractInterface):

    def loop(self):
        inputContent = "VOID"
        if (inputContent != "stop"):
            inputContent = input("MARVIN>")

    def getInterfaceName(self):
        return "CONSOLE"

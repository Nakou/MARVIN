from engine.Engine import Engine
class AbstractInterface:
    def __init__(self):
        return

    def loop(self):
        raise NotImplementedError( "Should have implemented this" )

    def inCom(self, message):
        engine = Engine(self)
        engine.start(message)

    def outCom(self, message):
        raise NotImplementedError( "Should have implemented this" )

    def getInterfaceName(self):
        raise NotImplementedError( "Should be named" )

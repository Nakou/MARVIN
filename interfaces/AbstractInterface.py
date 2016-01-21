class AbstractInterface :

    def loop(self):
        raise NotImplementedError( "Should have implemented this" )

    def inCom(self, message, abstractUser):
            return

    def outCom(self, message):
        raise NotImplementedError( "Should have implemented this" )

    def getInterfaceName(self):
        raise NotImplementedError( "Should be named" )

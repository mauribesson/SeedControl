class Global:
    def __init__(self):
       #w : Windows
       #l : Linux
        self.OS= "w"

       #Debugg
        self.debugMode = True

    def getOS(self):
        return self.OS

    def setOS(self, so):
        self.SO = so

    def getDebugMode(self):
        return self.debugMode

    def setDebugMode(self, mode):
        self.debugMode = mode


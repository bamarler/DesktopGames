# Util class of useful methods
class Util:
    def __init__(self):
        pass
    
    # method to convert 0 to -1 and any other number to 1
    def convertNum(self, value):
        if (value == 0):
            return -1
        else:
            return 1
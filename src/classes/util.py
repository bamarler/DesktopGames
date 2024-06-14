import math

# useful methods

def __init__():
    pass

# method to convert 0 to -1 and any other number to 1
def convertNum(value):
    if (value == 0):
        return -1
    else:
        return 1
    
# method to check if a position is within a circle
def isWithinCircle(pos, circleX, circleY, radius):
    return radius > math.sqrt(math.pow(pos[0] - circleX, 2) + math.pow(pos[1] - circleY, 2))
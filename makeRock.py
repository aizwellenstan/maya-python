import maya.cmds
import random

def makeRock1():
    val = random.uniform(0.5, 2.0)
    poly = maya.cmds.polySphere(r=val)
    x = random.uniform(0.8, 1.5)
    y = random.uniform(0.8, 1.5)
    z = random.uniform(0.8, 1.5)
    maya.cmds.scale(x, y, z)
    ver = maya.cmds.polyListComponentConversion(poly[0], toVertex=True)
    verE = maya.cmds.filterExpand(ver, selectionMask=31)
    for obj in verE:
        x = random.uniform(-0.1, 0.1)
        y = random.uniform(-0.1, 0.1)
        z = random.uniform(-0.1, 0.1)
        maya.cmds.select(obj, r=True)
        maya.cmds.move(x, y, z, r=True)
        
if __name__ == '__main__':  
    makeRock1()

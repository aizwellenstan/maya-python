import maya.cmds as mc

myWindow = title = "create joint chain along curve selected")
mc.rowColumnLayout(nc = 2)
mc.text(l = "joint amount:")
jntAmountIF = mc.IntField(v = 5, min = 2)
mc.button(l = "create", w = 150, c = "createJntAlongCurve()")
mc.button(l = "cancel", w = 150, c= "mc.deleteUI(myWindow)")
mc.showWindow()

def createJntAlongCurve():
  curveSelected = mc.ls(s1 = True)[0]
  jointAmount = mc.IntField(jntAmountIF, q = True, v = True)
  previousJnt = ""
  rootJnt = ""
  for i in range(0, jointAmount):
    mc.select(c1 = True)
    newJnt = mc.joint()
    mothionPath = mc.pathAnimation(
      newJnt, c = curveSelected, fractionMode = True
    )
    mc.cutKey(mothionPath + ".u", time = ())
    mc.setAttr(mouthPath + ".u", i * (1.0/(jointAmount -1)))

    mc.delete(newJnt + ".tx", icn = True)
    mc.delete(newJnt + ".ty", icn = True)
    mc.delete(newJnt + ".tz", icn = True)
    mc.delete(mothionPath)

    if i == 0:
        previousJnt = newJnt
        rootJnt = newJnt
        continue
    
    mc.parent(newJnt, previousJnt)
    previousJnt = newJnt
mv.joint(
  rootJnt, e = True, oj= "xyz", sao = "yup", ch = True, zso = True
)
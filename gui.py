import maya.cmds as cmds

def testWindow():
    #既にGUIが存在する時に古いほうを消す処理
    if cmds.window('testWindow', ex=1):
        cmds.deleteUI('testWindow')
    windowName = cmds.window('testWindow',title='testWindow')
    #GUIを作成
    tabTest=cmds.tabLayout(scrollable=False, innerMarginHeight=5, innerMarginWidth=1)
    tabTestColumn=cmds.columnLayout(adj=True, rowSpacing=10)
    cmds.button(label="TestButton")
    cmds.button(label="TestButton")
    cmds.textField(w=500, tx="TestTextField")
    cmds.rowLayout(numberOfColumns=4, columnAttach4=('left', 'left', 'left', 'left'), columnWidth4=(100, 150, 150, 150))
    cmds.button(label="TestButton")
    cmds.checkBox(label="TestCheckBox")
    cmds.checkBox(label="TestCheckBox")
    cmds.checkBox(label="TestCheckBox")
    cmds.setParent('..')
    cmds.text(label="TestText")
    cmds.textField(w=500, tx="TestTextField")
    cmds.setParent('..')
    cmds.tabLayout(tabTest, edit=1, tabLabel=(tabTestColumn, "Test"))
    #GUIを表示
    cmds.showWindow()

if __name__ == '__main__':  
    testWindow()

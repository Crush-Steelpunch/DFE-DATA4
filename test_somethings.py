import lr_functions

def test1():
    assert lr_functions.gradescore(25, 50, 100) == 100

def test2():
    assert lr_functions.getmagic(5, 5, 25) == True
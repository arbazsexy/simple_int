from si import simint

def test_simpleInt_pos():
    assert simInt(2000,8,12) == 19200

def test_simpleInt_zer():
    assert simInt(10000,7,0) == 19200
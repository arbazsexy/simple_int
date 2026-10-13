from si import simint

def test_simpleInt_pos():
    assert simint(2000, 8, 12) == 1920.0 

def test_simpleInt_zer():
    assert simint(10000, 7, 0) == 0.0     
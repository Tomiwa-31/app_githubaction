
#pytest library checks ths specific test cases basesd on the math operations we supplied in he other file

from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5#test if 2+3 is 5
    assert add(-1,1) == 0
    
def test_sub():
    assert sub(5,3) == 2
    assert add(4,3) == 1
    assert add(3,3) == 0
    assert add(2,3) == -1

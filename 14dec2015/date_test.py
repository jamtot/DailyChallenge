from nose.tools import *
import datedilemma

def test_conversion():
    output1 = datedilemma.reformat('2016/3/5') 
    assert_equal(output1,'2016-03-05')

    output2 = datedilemma.reformat('03 5 16') 
    assert_equal(output2,'2016-03-05')

    output3 = datedilemma.reformat('9-9-09') 
    assert_equal(output3,'2009-09-09')

def test_fail():
    # runs with bad inputs
    output1 = datedilemma.reformat('2/3/5') 
    assert_equal(output1,'205-02-03')

    output1 = datedilemma.reformat('9/9/9/09') 
    assert_equal(output1,'209-09-09')

    assert_raises(IndexError,datedilemma.reformat,'1')   

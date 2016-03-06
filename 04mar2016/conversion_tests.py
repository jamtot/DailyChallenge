from nose.tools import *
import bintorli

def test_binary_to_rli():
    result1 = bintorli.bin_to_rli("0 0 1 0 0 0 0 1 1 1")
    result2 = bintorli.bin_to_rli("0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1")
    result3 = bintorli.bin_to_rli("1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1")
    
    assert_equal(result1, "2 3 7 10")
    assert_equal(result2, "8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    assert_equal(result3, "0 1 25 26 31 32")

def test_binary_to_rle():
    result1 = bintorli.bin_to_rle("0 0 1 0 0 0 0 1 1 1")
    result2 = bintorli.bin_to_rle("0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1")
    result3 = bintorli.bin_to_rle("1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1")
    
    assert_equal(result1, "2 0 3 2")
    assert_equal(result2, "8 0 0 2 0 3 0 1 0 0 0 0 0 5")
    assert_equal(result3, "0 0 23 0 4 0")

def test_rli_to_binary():
    result1 = bintorli.rli_to_bin("2 3 7 10")
    result2 = bintorli.rli_to_bin("8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    result3 = bintorli.rli_to_bin("0 1 25 26 31 32")
    
    assert_equal(result1, "0 0 1 0 0 0 0 1 1 1")
    assert_equal(result2, "0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1")
    assert_equal(result3, "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1")

def test_rle_to_binary():
    result1 = bintorli.rle_to_bin("2 0 3 2")
    result2 = bintorli.rle_to_bin("8 0 0 2 0 3 0 1 0 0 0 0 0 5")
    result3 = bintorli.rle_to_bin("0 0 23 0 4 0")
    
    assert_equal(result1, "0 0 1 0 0 0 0 1 1 1")
    assert_equal(result2, "0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1")
    assert_equal(result3, "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1")

def test_rle_to_rli():
    result1 = bintorli.rle_to_rli("2 0 3 2")
    result2 = bintorli.rle_to_rli("8 0 0 2 0 3 0 1 0 0 0 0 0 5")
    result3 = bintorli.rle_to_rli("0 0 23 0 4 0")

    assert_equal(result1, "2 3 7 10")
    assert_equal(result2, "8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    assert_equal(result3, "0 1 25 26 31 32")
    
def test_rli_to_rle():
    result1 = bintorli.rli_to_rle("2 3 7 10")
    result2 = bintorli.rli_to_rle("8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    result3 = bintorli.rli_to_rle("0 1 25 26 31 32")

    assert_equal(result1, "2 0 3 2")
    assert_equal(result2, "8 0 0 2 0 3 0 1 0 0 0 0 0 5")
    assert_equal(result3, "0 0 23 0 4 0")

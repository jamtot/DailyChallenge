from nose.tools import *
import bintorli

# tests for 'easy' part of challenge

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

# tests for 'medium' part of challenge

def test_rli_to_substring():
    result1 = bintorli.rli_to_subrli("0 9 2 3 7 10")
    result2 = bintorli.rli_to_subrli("5 14 8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    result3 = bintorli.rli_to_subrli("23 4 0 1 25 26 31 32")
    
    assert_equal(result1, "2 3 7 9")
    assert_equal(result2, "3 4 5 8 9 13 14")
    assert_equal(result3, "2 3 4")

def test_conversions():
    result1 =  bintorli.rli_to_bin(
               bintorli.rle_to_rli(
               bintorli.rli_to_rle(
               bintorli.bin_to_rli(
               "0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1"))))

    assert_equal(result1, "0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1")
    result2 = bintorli.rli_to_subrli("8 14 8 9 10 13 14 18 19 21 22 23 24 25 26 32")
    result3 = bintorli.rli_to_bin(result2)
    assert_equal(result3, "1 0 1 1 1 0 1 1 1 1 0 1 1 0")

def test_large():
    bigResult1 = bintorli.getfiletext("bigstring.txt")
    bigResult1 = bigResult1.replace("\n", "")

    bigResult2 = bintorli.bin_to_rli(bigResult1)
    bigResult3 = bintorli.rli_to_bin(bigResult2)
    
    assert_equal(bigResult1, bigResult3)


def test_large_sub():

    bigText = bintorli.getfiletext("bigstring.txt")
    bigConv = bintorli.bin_to_rli(bigText)

    bigData = (" ").join(['5','16', bigConv])
    bigResult1 = bintorli.rli_to_subrli(bigData)
    assert_equal(bigResult1, "0 4 11 13 14 16")
    
    bigResult2 = bintorli.rli_to_bin(bigResult1)

    assert_equal(bigResult2, "1 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1")

    bigData2 = (" ").join(['785','17', bigConv])
    bigResult3 = bintorli.rli_to_subrli(bigData2)

    assert_equal(bigResult3, "0 4 9 14 17")

    bigResult4 = bintorli.rli_to_bin(bigResult3)

    assert_equal(bigResult4, "1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0")

    bigData3 = (" ").join(['13075','17', bigConv])
    bigResult5 = bintorli.rli_to_subrli(bigData3)

    assert_equal(bigResult5, "0 4 10 11 14 17")

    bigResult6 = bintorli.rli_to_bin(bigResult5)

    assert_equal(bigResult6, "1 1 1 1 0 0 0 0 0 0 1 0 0 0 1 1 1")
    
#  tests for 'hard' part

def test_overwrite():
    result1 = bintorli.rli_overwrite("3 0 3 > 2 3 7 10")
    result2 = bintorli.rli_overwrite("3 1 3 > 2 3 7 10")
    result3 = bintorli.rli_overwrite("3 1 3 > 10")
    result4 = bintorli.rli_overwrite("3 1 3 > 0 10")
    result5 = bintorli.rli_overwrite("3 0 3 7 10 12 15 > 8 9 10 13 14 18 19 21 22 23 24 25 26 32")

    assert_equal(result1, "2 6 7 10")
    assert_equal(result2, "2 3 4 6 7 10")
    assert_equal(result3, "4 6 10")
    assert_equal(result4, "0 3 4 10")
    assert_equal(result5, "3 6 10 13 15 18 19 21 22 23 24 25 26 32")

def test_additional_overwrite():
    input1 = "6 1 4 7 11 12 15 16 19 > 0 1 5 7 8 10 14 16 17 18 19 20 24 34 36 37 40 42"
    assert_equal(bintorli.rli_overwrite(input1), bintorli.cheat_overwrite(input1))
    

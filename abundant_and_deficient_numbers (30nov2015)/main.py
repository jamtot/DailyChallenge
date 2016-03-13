input1 = """18
21
9"""

input2 = """111  
112 
220 
69 
134 
85"""

input3 = """6
28"""

def check_number(number):
    num_by_two = number*2
    sum_of_divisors = 0
    for i in xrange(1,number+1):
        if number%i == 0:
            sum_of_divisors+=i
    if (num_by_two > sum_of_divisors):
        deficiency = num_by_two-sum_of_divisors
        print "%d deficient by %d" % (number, deficiency)
    elif (num_by_two < sum_of_divisors):
        abundancy = sum_of_divisors-num_by_two
        print "%d abundant by %d" % (number, abundancy)
    else:
        print "%d perfect" % number

def get_input(input):
    nums = input.split()
    return nums

def process_input(input):
    nums = get_input(input)
    for num in nums:
        check_number(int(num))


if __name__ == "__main__":
    process_input(input1)
    process_input(input2)
    process_input(input3)

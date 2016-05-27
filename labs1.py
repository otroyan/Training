import re
import math

def is_simple(x):
    if x <= 2:
        return True
    if not x%2:
        return False
    for i in range(3, int(math.sqrt(x)+1)):
        if not x%i:
            return False
    return True

def max_simple(s_orig):
    if not s_orig:
        return None
    nums = [int(x) for x in re.findall(r'[0-9]+', s_orig)]
    if not nums:
        return None
    return max([x for x in nums if is_simple(x)])

if __name__ == "__main__":

    #s_orig = "ergewhj ehrg4g5hg83g751  445"
    s_orig = "31lsdlkl1543lll	1549	dd1553	ds1559	1571	1579	" \
              "1583	1597	1619d1621	1627sdfg	1637sdfs	1657"
    print("result", max_simple(s_orig))


    s_orig = "1kjkjkj------12 2 2 1 1 tttttttt"
    print("result", max_simple(s_orig))

    s_orig = "wwww"
    print("result", max_simple(s_orig))
# -*- coding: utf-8 -*-

"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:

    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)[2:]
        cmpl_bin_num = []
        for i in bin_num:
            if i == '1':
                cmpl_bin_num.append('0')
            else:
                cmpl_bin_num.append('1')
        cmpl_num = int(''.join(cmpl_bin_num), 2)
        return cmpl_num

    def findComplement1(self, num):
        """
        :type num: int
        :rtype: int
        """
        print (len(bin(num))) # bin(num) = 0b***
        return 2 ** (len(bin(num)) - 2) - 1 - num

    def findComplement2(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num

if __name__ == '__main__':
    print (Solution().findComplement2(4))



# 第二种方法是什么意思? 感觉还是很有必要学习 CSAPP 的...
# num + compl_num + 1 = 2^(len(bin(num) - 2 ))
# 第三种比较有意思, 先找个与 num 相对应了全是 1111 的 bin, 
# 然后 ^ 把 1 变 0, 0 变 1, 并直接输出对应的数. 这个就需要
# 对 二进制的特性有个了解, 知道怎么做出与 num 位数对应的 bin. 










# 
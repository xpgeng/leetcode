# -*- coding: utf-8 -*-

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = '{0:032b}'.format(n)
        revese_num =  int(bin_n[::-1], 2)
        print (revese_num)
if __name__ == '__main__':
    Solution().reverseBits(43261596)
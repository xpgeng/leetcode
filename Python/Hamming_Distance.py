# -*- coding: utf-8 -*-

"""
he Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = '{0:031b}'.format(x)
        bin_y = '{0:031b}'.format(y)
        
        k = 0
        for i in range(31):
            if bin_x[i] != bin_y[i]:
                k += 1
        return k

    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int()
        """
        print (x ^ y) # ????
        return bin(x ^ y).count('1')

if __name__ == '__main__':
    print (Solution().hammingDistance1(1, 4))
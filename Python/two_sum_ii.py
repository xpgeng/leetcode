# -*- coding: utf-8 -*-
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 

'''
class Solution(object):
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_length = len(numbers)
        for i in range(num_length):
            b = target - numbers[i]
            for j in numbers[i+1:]:
                if j == b:
                    return[i+1, numbers[i+1:].index(j) + i + 2]
                if j > b:
                    numbers.remove(j)

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while start < end:
            tmp_sum = numbers[start] + numbers[end]
            if tmp_sum == target:
                return [start+1, end+1]
            elif tmp_sum < target:
                start += 1
            else:
                end -= 1

"""
第一个太复杂了, 如果真正的结果是在最后几个的话,那么大概复杂度在 O(n^2)
第二个就简单很多, 复杂度在 O(n)

"""
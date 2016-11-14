"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}
        for n in nums:
            if n in d:
                d[n] =d[n]+1
            else:
                d[n] = 1

        result = []        
        for k in d:
            if d[k] == 2:
                result.append(k)
                
        return result

"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        
        for c in nums:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        result = []
       
        
        for Key, v in sorted(d.items(), key= lambda t : t[1], reverse= True):
            result.append(Key)
             
        return result[:k]

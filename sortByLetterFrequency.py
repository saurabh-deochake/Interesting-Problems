## Given a string, sort it in decreasing order based on the frequency of characters.

""" Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        d = {}
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        result = ""   
        for k, v in sorted(d.items(), key= lambda t : t[1], reverse= True):
            result = result + k * v
            
        return result

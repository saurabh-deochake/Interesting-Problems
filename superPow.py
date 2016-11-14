"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        
        power = "".join(str(x) for x in b)
        
        #Instead of using a ** power % 1337 we must use in-built function to calculate power
        # pow(base, exponent, modulo) calculates the same very efficiently
        return pow(a, int(power), 1337)
        
        
   

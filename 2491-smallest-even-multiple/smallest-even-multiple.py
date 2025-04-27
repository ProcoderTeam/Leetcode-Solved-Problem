class Solution(object):
    def smallestEvenMultiple(self, n):
        theNumber = n
        start=True
        while(start):
            if(theNumber%2==0 and theNumber%n==0):
                start = False
                return theNumber
            else:
                theNumber+=1
        """
        :type n: int
        :rtype: int
        """
        
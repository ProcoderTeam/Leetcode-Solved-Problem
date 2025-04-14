class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new=[False]*len(candies)
        for i in range(len(candies)):
               checked = candies[i] + extraCandies
               if checked >= max(candies):
                      new[i]=True
        return new

                    
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        for i in range(1,len(nums)):
            if nums[i]!= nums[i-1]:
                nums[k]=nums[i]
                #print(nums[k],i)
                k+=1

        return k


        
        return len(set(nums))
        """
        :type nums: List[int]
        :rtype: int
        """

        
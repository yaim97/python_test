class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0

        i=0
        for s in nums:
            if s!=val:
                nums[i]=s
                i+=1
        return i